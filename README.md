

# 📌 Chatbot - Monitoria de Computação Gráfica

> _Esse projeto tem como objetivo desenvolver um chatbot para auxiliar na disciplina de Computação Gráfica, utilizando a abordagem de RAG (Retrieval Augmented Generation). O sistema utiliza materiais desenvolvidos pela professora e monitores, juntamente com livros de referência. O intuito é que o chatbot seja capaz de fornecer respostas precisas, contextualizadas e alinhadas ao conteúdo ministrado na sala de aula._

---

## 🧠 Objetivo Geral
Desenvolver um chatbot que utiliza material selecionado para auxiliar alunos durante a disciplina de Computação Gráfica.

## 🎯 Objetivos Específicos
- Garantir uma plataforma de estudo confiável, utilizando material personalizado alinhado com o conteúdo ministrado.
---

## 📈 Status Atual do Projeto
- **Status atual:** Em andamento  
---

## 👥 Equipe
| Nome | Função | Contato |
|------|--------|----------|
| Luana Batista da Cruz | Responsável | luana.batista@ufca.edu.br |
| Victor Cleyton de Andrade Chaves | Bolsista | victor.chaves@aluno.ufca.edu.br |
---

## 🧪 Métodos & Tecnologias Utilizadas
- **Python**: Linguagem de programação de alto nível, interpretada, multiparadigma, que suporta os estilos imperativo, orientado a objetos e funcional. Possui tipagem dinâmica e forte, sendo amplamente utilizada no desenvolvimento de aplicações devido à sua simplicidade, legibilidade e vasta disponibilidade de bibliotecas.

- **Langchain**: Framework de código aberto voltado ao desenvolvimento de aplicações baseadas em Large Language Models (LLMs). Oferece um conjunto abrangente de ferramentas que facilitam a orquestração de modelos, gerenciamento de contexto, integração com bases de conhecimento e implementação de fluxos como RAG.

- **Redis**: Sistema de banco de dados de código aberto orientado a estruturas de dados do tipo chave-valor, amplamente reconhecido por sua alta performance e baixa latência. Sua simplicidade de uso e rapidez o torna adequado para armazenamento temporário, cache e operações que exigem acesso eficiente aos dados.

- **GPT-4o Mini**: Modelo de inteligência artificial desenvolvido pela OpenAI, projetado para ser mais rápido e econômico em comparação a modelos maiores da mesma família. Indicado para aplicações que demandam boa capacidade de compreensão de linguagem natural, mas que não exigem raciocínio extremamente complexo, sendo especialmente adequado para o uso com agente baseados em LLMs.

- **Text-Embedding-3-Small**: Modelo de geração de embeddings de texto desenvolvido pela OpenAI, responsável por transformar textos em vetores numéricos que representam seu significado semântico. Esses vetores são fundamentais para a implementação de sistemas RAG, permitindo a realização de buscas semânticas eficientes e a recuperação de informações relevantes a partir de uma base de conhecimento.
---

## 📁 Estrutura do Projeto
```
📂 Chatbot-CG
 ├── 📁 docs                -> Documentação sobre o projeto 
 │
 ├── 📁 src                 -> Implementações, códigos e experimentos
 │
 └── 📄 README.md           -> Este arquivo
```
---

## ▶ Como Executar os Códigos
*Observação: Os scripts fazem uso de ferramentas da OpenAI, que consomem crédito, certifique-se de criar um arquivo .env e cadastrar sua chave na variável local OPENAI_API_KEY.*
- **gen-kb:** Crie uma pasta para o projeto e, dentro dela, uma pasta chamada *Docs*. Coloque todos os seus arquivos PDF dentro dessa pasta *Docs*. O script está configurado para procurar exatamente por esse nome. Ao final da execução, será criada uma pasta chamada *chroma* contendo o banco de dados SQLite e os arquivos binários com seus documentos processados.
- **chatbot:** É necessário que uma instância do banco de dados Redis esteja em execução. Certifique-se também que a pasta chroma com a base de dados exista. Execute o script passando como parâmetros a chave e pergunta do usuário. O script utiliza a chave para recuperar histórico do usuário no banco de dados. Ao final da execução é retornada a resposta do chatbot.
---

## 📊 Resultados Parciais / Relatórios
| Data | Progresso | Observações |
|------|-----------|-------------|
| 20/04/2026 | 100% concluído | A base do chatbot está completa. |
        
