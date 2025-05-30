from graph.chains.json_chain import json_chain
from db.memory_store import store_result

def json_agent(state):
    print("Json Agent")
    jsoncontent = json_chain.invoke({"file_content": state.file_content,"intent":state.intent})
    extracteddata = f"Data:{jsoncontent.cleaned_data} Missing Values:{jsoncontent.missing_fields}"
    store_result(state.file_type,state.intent,"JSON",extracteddata)
    print(f"Extracted Data : {extracteddata}")
    print("DATA SAVED TO DATABASE")
    return jsoncontent