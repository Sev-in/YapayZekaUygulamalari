from dotenv import load_dotenv, dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage

load_dotenv()

# temperature arttıkça yaratıcılık artar, azaldıkça kesinlik artar.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)
messages = [
    #{"system" : "You are a senior software engineer",
    #"user" : "What is a python?"}
    # Langchainin obje odaklı programlaması sayesinde daha işimiz daha basit
    # İngilizce yazınca daha iyi cevaplar aldığımız için ingilizce yazıyoruz.
    SystemMessage(content="Translate the following from English to Turkish"),
    HumanMessage(content="Hi!"),
]

if __name__ == "__main__":
    response = model.invoke(messages)
    print(response)
    print(response.content)
