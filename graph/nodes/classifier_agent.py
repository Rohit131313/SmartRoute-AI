from graph.chains.classifier_chain import classifier_chain

def classifier_agent(file_content: str):
    print("Classifier Agent")
    classifier = classifier_chain.invoke({"file_content": file_content})
    print(classifier)
    return classifier


