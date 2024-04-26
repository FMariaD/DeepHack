from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
)
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings.gigachat import GigaChatEmbeddings
from langchain.chat_models.gigachat import GigaChat
from langchain.chains import RetrievalQA
import os
from config import GIGACHAT_TOKEN
from .pdf_reader import download_file


def create_db(user_id, agent_id, texts):
    if type(texts) != list:
        docs = text_splitter.create_documents([texts])
    else:
        docs = text_splitter.create_documents(texts)
    dir = os.path.join(DIR_PATH, user_id)
    os.makedirs(dir, exist_ok=True)

    path = os.path.join(dir, agent_id)
    Chroma.from_documents(docs, emb_model, persist_directory=path)


def create_agent(user_id, agent_name, articles):
    user_id = str(user_id)
    files = []
    for article in articles:
        file = download_file(article["pdf_link"])
        files.append(file)
    create_db(user_id, agent_name, files)


def get_answer(question, user_id, agent_id):
    user_id = str(user_id)
    dir = os.path.join(DIR_PATH, user_id)
    path = os.path.join(dir, agent_id)
    db = Chroma(persist_directory=path, embedding_function=emb_model)

    qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
    answer = qa_chain({"query": question})
    return answer


DIR_PATH = "model/agents_database/"

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,
    chunk_overlap=200,
)
emb_model = GigaChatEmbeddings(
    credentials=GIGACHAT_TOKEN, verify_ssl_certs=False, scope="GIGACHAT_API_CORP"
)
llm = GigaChat(
    credentials=GIGACHAT_TOKEN,
    model="GigaChat-Pro",
    scope="GIGACHAT_API_CORP",
    verify_ssl_certs=False,
)
