from langgraph.graph import StateGraph
from graph.state import GraphState
from graph.nodes.classifier_agent import classifier_agent
from graph.nodes.json_agent import json_agent
from graph.nodes.email_agent import email_agent


def route_agent(state: GraphState) -> str:
        if state.file_type == "JSON":
            return "JSONAgent"
        elif state.file_type == "Email":
            return "EmailAgent"

def build_flow():
    builder = StateGraph(GraphState)

    builder.add_node("Classifier", classifier_agent)

    builder.add_node("JSONAgent", json_agent)
    builder.add_node("EmailAgent", email_agent)


    # Graph structure
    builder.set_entry_point("Classifier")
    builder.add_conditional_edges("Classifier", route_agent)

    return builder.compile()
