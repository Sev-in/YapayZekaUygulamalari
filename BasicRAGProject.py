import bs4
from dotenv import load_dotenv
from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)

loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",), #birden çok link verebilirsin
    bs_kwargs=dict(
        parse_only = bs4.SoupStrainer(
            class_ =("post-content","post-title","post-header") #html yapısını inceleyip yaz.
        )
    ),
)

docs = loader.load()

if __name__ == '__main__':
    print(docs)