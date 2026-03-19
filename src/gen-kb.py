# Script rseponsável por montar a base de conhecimento.

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import openai
from dotenv import load_dotenv
import os
import shutil

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")


CHROMA_PATH = "chroma"
DATA_PATH = "Docs"

def main():
    # Carrega os documentos da pasta de dados.
    loader = DirectoryLoader(DATA_PATH, glob="**/*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    # Divide os documentos em chunks.
    chunks = split_documents(documents)
    # Cria um banco de dados Chroma com os embeddings.
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH)
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(model="text-embedding-3-small"), persist_directory=CHROMA_PATH)

def split_documents(documents):
    # Define o tamanho dos chunks.
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 500,
        length_function= len,
        add_start_index= True
    )
    # Divide os documentos no tamanho especificado.
    chunks = text_splitter.split_documents(documents)
    return chunks

if __name__ == "__main__":
    main()