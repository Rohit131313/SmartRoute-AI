from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.environ["GOOGLE_API_KEY"]

class EmailFields(BaseModel):
    sender: str
    intent: str
    summary: str

email_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract relevant fields from email."),
    ("human", "Email content:\n{file_content}")
])

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0)

email = llm.with_structured_output(EmailFields)
email_chain: RunnableSequence = email_prompt | email
