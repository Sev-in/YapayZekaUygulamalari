from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory#Mesajları RAM üzerinde tutan geçici bir hafıza nesnesi.
from langchain_core.runnables.history import RunnableWithMessageHistory #Zinciri hafıza ile birleştiren “sarmalayıcı” (wrapper).
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder #Geçmiş konuşmaların gelecekte buraya yerleştirileceğini belirtir.

load_dotenv()

model = GoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.5,
)

#Geçmiş mesajları saklayıp her yeni istekte modele geri veriyoruz.
store = {}

def get_session_history(session_id : str) -> BaseChatMessageHistory: #String alıcaz geriye BaseChatMessageHistory döndürücez.
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You ara a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages")
        #Geçmiş konuşmaları (hem insan hem AI mesajlarını) burada otomatik olarak doldurmak üzere bir yer tutucu oluşturuyor.
])

chain = prompt | model
config = {"configurable" : {"session_id": "abcde123"}}
with_message_history = RunnableWithMessageHistory(chain, get_session_history)


# Tek tek çalıştırdım ve ismimi hatırlamadı çünkü daha hafızası yok.
#message0 = HumanMessage(content="Hello, my name is Şevin!")
#message1 = HumanMessage(content="What is my name?")

#Aynı sessionda olduğumuz için hatırladı. Ama her zaman bu şekilde kullanamayız.
#messages = [
#    HumanMessage(content= "Hello, my name is Şevin!"),
#    AIMessage(content= "Hello Şevin, how can ı help you?"),
#    HumanMessage(content= "What is my name?")
#]

if __name__ == "__main__":
    while True:
        user_input = input(">")
        for r in with_message_history.stream([
            HumanMessage(content=user_input)
        ],
            config = config,
        ):
            print(r)
        # invoke : cevabın tümünün hazır olmasını bekler.
        # stream : cevap oluştukça getirir.

        #response = with_message_history.stream([
        #    HumanMessage(content=user_input)
        #],
        #    config = config,
        #)
        #print(response)