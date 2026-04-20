# Script responsável pelo ChatBot.

import os

import argparse
import openai
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import redis
import json

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = "Você é uma IA monitora de Computação Gráfica, responda essa pergunta: {question}, com base nesse contexto: {context}. NÃO utilize informações de fora do contexto dado. A mensagem será impressa em um terminal simples, então NÃO use códigos de formatação."
RESUME_TEMPLATE = "Com base nesse histórico: [{history}], e nesse input: [{question}], crie APENAS um input resumindo o que o usuário deseja saber para ser utilizado em um agente de LLM. NUNCA responda a pergunta do usuário."

r = redis.from_url("redis://localhost:6379/0")

def redis_save_history(key, question, response):
    # Envia mensagem do usuário juntamente com a resposta do agente para o banco de dados, onde é armazenado o histórico de conversas.
    message = {"Usuário": question, "IA": response}
    r.rpush(key, json.dumps(message))
    # A instrução abaixo informa ao banco para manter apenas as últimas 5 conversas.
    r.ltrim(key, -5, -1)

def redis_load_history(key):
    # Recupera histórico de conversas do usuário.
    raw = r.lrange(key, 0, -1)
    texts = []

    # Junta todo o histórico em um único bloco de texto e retorna.
    for item in raw:
        msg = json.loads(item.decode())
        user = msg.get("Usuário", "")
        ai = msg.get("IA", "")

        texts.append(f"Usuário: {user}\nIA: {ai}")

    return "\n\n".join(texts)

def main(key, question):  
    """ 
    Checa se chave do usuário existe. Se sim, recupera histórico de conversas e envia juntamente com input para o agente de IA.
    O agente é responsável por analisar o input e o histórico e resumir em um input o que o usuário deseja.
    """
    if r.exists(key):
        history = redis_load_history(key)
        prompt_template = ChatPromptTemplate.from_template(RESUME_TEMPLATE)
        prompt = prompt_template.format(history=history, question=question)
        model = ChatOpenAI(model="gpt-4o-mini")
        response_text = model.invoke(prompt)
        query_text = response_text.content
    else:
        query_text = question

    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)

    # Busca informações com base na similaridade com o assunto da pergunta no banco de dados.
    results = db.similarity_search_with_score(query_text, k=5)
    if len(results) == 0 or results[0][1] < 0.5:
        return "Lamento, não possuo informações sobre esse assunto."

    # Cria o texto com o contexto a ser usado com base nas informações retornadas.
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    # Cria o prompt a ser enviado.
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)
    model = ChatOpenAI(model="gpt-4o-mini")
    # Retorna resposta do chatbot juntamente com as fontes utilizadas.
    response_text = model.invoke(prompt)
    sources = list(set([doc.metadata.get("source", None) for doc, _score in results]))
    redis_save_history(key, question, response_text.content)
    return (f"{response_text.content} \n Fontes: \n{sources}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("user_key")
    parser.add_argument("question")

    args = parser.parse_args()

    result = main(key=args.user_key, question=args.question)
    print(result)