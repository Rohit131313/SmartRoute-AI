from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.environ["GOOGLE_API_KEY"]

class JSONAnalysis(BaseModel):
    cleaned_data: str
    missing_fields: str

json_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the relevant fields according to the {intent} and also specify the missing fields"),
    ("human", "JSON data:\n{file_content}")
])
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0)
json = llm.with_structured_output(JSONAnalysis)
json_chain: RunnableSequence = json_prompt | json
