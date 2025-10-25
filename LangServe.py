from dotenv import load_dotenv, dotenv_values
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser #Çıktının nasıl işleneceğini belirtir.(String şeklinde burada)
from langchain_core.prompts import ChatPromptTemplate
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

# temperature arttıkça yaratıcılık artar, azaldıkça kesinlik artar.
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.1)

system_prompt = "Translate the following into {language}" #Sistem tarafında dil dinamik
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt), ("user","{text}") #Kullanıcı tarafında text dinamik
    ]
) #template = şablon

parser = StrOutputParser() #Çıktı işleyici

#User Input → PromptTemplate → Model → Parser → Çıktı
chain = prompt_template | model | parser #LCEL

app = FastAPI(
    title="Translator App!",
    version="1.0",
    description="Translation Chat Bot",
) # çok hızlı bir şekilde web uygulamaları oluşturmaya yarar.

add_routes(
    app,
    chain,
    path="/chain"
) #LangServe, LangChain zincirlerini otomatik olarak API rotalarına dönüştürür.


if __name__ == "__main__":
    import uvicorn #FastAPI’yi çalıştıran asenkron sunucu.
    uvicorn.run(app, host="localhost", port=8000)


#Asenkron Sunucu (FastAPI):
#Tek bir garson (sunucu) kullanarak, bekleme sürelerinde
#modelden cevap gelmesini beklemek, veritabanından veri beklemek gibi) boşa durmaz.
#Bu sayede aynı anda binlerce müşteriye (isteğe) çok verimli bir şekilde hizmet verebilir.
