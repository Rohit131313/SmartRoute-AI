from graph.graph import build_flow
from graph.state import GraphState
from db.memory_store import init_db

init_db()
flow = build_flow()

state = GraphState(file_content="""
{
  "file_type": "JSON",
  "intent": "User Data",
  "user": {
    "id": 12345,
    "name": "John Doe",
    "email": "john.doe@example.com",
    "roles": ["admin", "user"],
    "profile": {
      "age": 30,
      "country": "USA"
    }
  }
}

Additional notes:
- This JSON contains basic user information.
- The intent is to classify user data for processing.
""",file_type="",intent="")
final_state = flow.invoke(state)


