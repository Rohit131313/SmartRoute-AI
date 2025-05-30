from graph.chains.email_chain import email_chain
from db.memory_store import store_result

def email_agent(state):
    print("Email Agent")
    emailcontent = email_chain.invoke({"file_content": state.file_content})
    extracteddata = f"Sender: {emailcontent.sender} Intent:{emailcontent.intent} Summary:{emailcontent.summary}"
    store_result(state.file_type,state.intent,"JSON",extracteddata)
    print(f"Extracted Data : {extracteddata}")
    print("DATA SAVED TO DATABASE")
    return emailcontent
