from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults


load_dotenv()

search = TavilySearchResults(max_results=2) #max_results = en fazla kaç tane sonuç getireceğini söylüyoruz.

tools = [search] #arama sonuçlarını listeye koyuyoruz.

if __name__ == '__main__':
    search_results = search.invoke("what is the weather in istanbul?")
    print(search_results)