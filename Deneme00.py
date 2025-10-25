from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

model = GoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature = 0.5,
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You ara a helpful assistant. Answer all questions to the best of your ability."),
        MessagesPlaceholder(variable_name="messages")
])

chain = prompt | model


# Hafıza olmadan da döngü içerisinde hatırlar mı diye merak ettim. Fakat hatırlamadığını gördüm.
if __name__ == "__main__":
    while True:
        user_input = input(">")
        response = chain.invoke([
            HumanMessage(content=user_input)
        ]
        )
        print(response)