from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature = 0.6)

search = TavilySearchResults(max_results=2) #max_results = en fazla kaç tane sonuç getireceğini söylüyoruz.

tools = [search] #arama sonuçlarını listeye koyuyoruz.

model_with_tools = model.bind_tools(tools) #llm ile araçları birbirine bağlamak için

if __name__ == '__main__':
    #search_results = search.invoke("what is the weather in istanbul?")
    #print(search_results)

    response = model_with_tools.invoke([HumanMessage(content="what is the weather in istanbul right now?")])
    print(response) #content boş geliyor yani llm anlamıyor bu yüzden cevap vermiyor ama metadata mevcut.
    print(response.tool_calls)