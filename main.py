from graph.graph import build_flow
from graph.state import GraphState
from db.memory_store import init_db

init_db()
flow = build_flow()

state = GraphState(file_content="""
Dear Vendor,

We would like to request a quotation for the supply of 500 units of industrial-grade copper wire. Please include the delivery schedule, payment terms, and any applicable discounts in your response. The products should meet ISO quality standards and be delivered by the end of next month.

Looking forward to your prompt response.

Best regards,  
Procurement Team  
ABC Industries Pvt. Ltd.

""",file_type="",intent="")
final_state = flow.invoke(state)


