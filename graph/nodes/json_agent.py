from graph.chains.json_chain import json_chain
from db.memory_store import store_result

def json_agent(state):
    jsoncontent = json_chain.invoke({"file_content": state.file_content,"intent":state.intent})
    extracteddata = f"Data:{jsoncontent.cleaned_data} Missing Values:{jsoncontent.missing_fields}"
    store_result(state.file_type,state.intent,"JSON",extracteddata)
    print(f"\nExtracted Data : {extracteddata}")
    print("\nDATA SAVED TO DATABASE")
    return jsoncontent