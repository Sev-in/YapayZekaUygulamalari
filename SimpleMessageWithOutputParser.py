from dotenv import load_dotenv, dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser #Çıktının nasıl işleneceğini belirtir.(String şeklinde burada)

load_dotenv()

# temperature arttıkça yaratıcılık artar, azaldıkça kesinlik artar.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)
messages = [
    SystemMessage(content="Translate the following from English to Turkish"),
    HumanMessage(content="Hi!"),
]

parser = StrOutputParser()
response = model.invoke(messages)
chain = model | parser #LCEL

if __name__ == "__main__":
    print(parser.invoke(response))
    print(chain.invoke(messages))
    #invoke = çağırmak
