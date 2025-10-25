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

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

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

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, #deneyerek bul
    chunk_overlap=200 #(parça çakışması veya bindirmesi) bağlam kaybını önler.
)
splits = text_splitter.split_documents(docs)
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
)

#Bu kod satırı, pasif olan vectorstore (vektör deposu) nesnenizi, aktif olarak arama yapabilen bir retriever (getirici) nesnesine dönüştürür.
retriever = vectorstore.as_retriever()

#langchain hub rag prompt yaz google'a
# hub'taki kullanıcıların hazırladığı promptları rahatlıkla hub.pull() ile çekebiliriz.
prompt = hub.pull("rlm/rag-prompt")

rag_chain = (
    {"context": retriever | format_docs, "question":RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)


if __name__ == '__main__':
    #print(docs)
    #print(format_docs(docs))

    for chunk in rag_chain.stream(
        "what is maximum inner product search?"
    ):
        print(chunk, end=" ",flush=True)