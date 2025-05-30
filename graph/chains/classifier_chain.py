from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableSequence
from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.environ["GOOGLE_API_KEY"]

class ClassificationResult(BaseModel):
    file_type: str = Field(description="One of:RAW,JSON, Email")
    intent: str = Field(description="e.g., Invoice, Complaint, RFQ, etc.")

classifier_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a classifier. Identify the format and intent."),
    ("human", "Content:\n{file_content}\n\nReturn file_type and intent.")
])
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001", temperature=0)


structured_classifier = llm.with_structured_output(ClassificationResult)

classifier_chain: RunnableSequence = classifier_prompt | structured_classifier
