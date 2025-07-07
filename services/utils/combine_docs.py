def combine(documents):
    content = ""

    for doc in documents:
        content += doc.page_content
    
    return content