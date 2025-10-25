from dotenv import load_dotenv, dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser #Çıktının nasıl işleneceğini belirtir.(String şeklinde burada)
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# temperature arttıkça yaratıcılık artar, azaldıkça kesinlik artar.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)

#messages = [
#    SystemMessage(content="Translate the following from English to Turkish"),
#    HumanMessage(content="Hi!"),
#]

system_prompt = "Translate the following into {language}" #Sistem tarafında dil dinamik
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user","{text}") #Kullanıcı tarafında text dinamik
    ]
) #template = şablon

parser = StrOutputParser()
chain = prompt_template | model | parser #LCEL

if __name__ == "__main__":
    print(chain.invoke({"language":"italian", "text":"Hello World"}))
    #invoke = çağırmak
