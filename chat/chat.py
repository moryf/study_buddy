from langchain_google_genai import ChatGoogleGenerativeAI
from settings import settings
from langchain_core.prompts import ChatPromptTemplate

template = "Explain this topic: '{topic}' in one simple paragraph."
prompt = ChatPromptTemplate.from_template(template)

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash-lite",
    temperature = 1,
    google_api_key= settings.settings.GOOGLE_API_KEY,
)

chain = prompt | llm

def explain(topic):
    response = chain.invoke({"topic": topic})
    return response.content
