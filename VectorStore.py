from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma #Küçük bir vektör veritabanı (embedding'lerle benzerlik aramak için)
from langchain_google_genai import GoogleGenerativeAIEmbeddings #Metinleri sayısal vektörlere çeviriyor
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()


documents = [
    Document(
        page_content="Dogs are great companions, known for their loyalty and friendliness.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Cats are independent pets that often enjoy their own space.",
        metadata={"source": "mammal-pets-doc"},
    ),
    Document(
        page_content="Goldfish are popular pets for beginners, requiring relatively simple care.",
        metadata={"source": "fish-pets-doc"},
    ),
    Document(
        page_content="Parrots are intelligent birds capable of mimicking human speech.",
        metadata={"source": "bird-pets-doc"},
    ),
    Document(
        page_content="Rabbits are social animals that need plenty of space to hop around.",
        metadata={"source": "mammal-pets-doc"},
    ),
]


#Burada:
#Her doküman vektörlere dönüştürülüyor (embedding)
#Bu vektörler Chroma veritabanına kaydediliyor
#(benzerlik araması yapmak için)
#Yani sistem artık “hangi metin, hangi soruya daha yakın” anlayabiliyor.
vector_store = Chroma.from_documents(
    documents = documents,
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
)


#Bu satır, en benzer dokümanı bulacak bir “çağrılabilir fonksiyon” oluşturuyor.
#Burada .bind(k=1) diyerek:
#Her sorguda sadece 1 en benzer dokümanı getir diyoruz.
retriever = RunnableLambda(vector_store.similarity_search).bind(k=1)

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)

message = """
Answer this question using the provided context only.
{question}

Context: {context}
"""

prompt = ChatPromptTemplate.from_messages(
    ["human",message]
)

#RunnablePassthrough() → soruyu olduğu gibi "question" kısmına geçiriyor
chain = {"context": retriever, "question":RunnablePassthrough()} | prompt | model

if __name__ == "__main__":
    #embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001").embed_query("dog")
    #print(vector_store.similarity_search_by_vector(embedding))

    #print(vector_store.similarity_search_with_score("dog"))

    #print(retriever.batch(["cat","shark"])) #En mantıklı olan dokümanı getiriyor.

    response = chain.invoke("tell me about cats")
    print(response.content)