from config import OPENAI_API_KEY, PINECONE_API_KEY

from models.schemas import ChatRequest
from langchain_openai import OpenAIEmbeddings
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_pinecone import PineconeVectorStore
from langchain.schema.output_parser import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from pinecone import Pinecone
from .utils.combine_docs import combine

def get_message(question, history):
    # Embedding model
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=OPENAI_API_KEY)
    # LLM
    llm = init_chat_model("gpt-4o-mini", model_provider="openai")

    # Standalone question 
    standaloneQuestionTemplate = 'Given a question, convert it to a standalone question to make it the most efficient for when it is converted to embedding to query vector database. Make sure you get rid of any un-needed input. question: {question} standalone question:'
    standaloneQuestionPrompt = ChatPromptTemplate.from_template(standaloneQuestionTemplate)
    standalone_chain = standaloneQuestionPrompt | llm | StrOutputParser()

    # Retrieval
    pc = Pinecone(api_key=PINECONE_API_KEY)
    index = pc.Index("langchain-rag")
    vector_store = PineconeVectorStore(embedding=embeddings, index=index)
    retriever = vector_store.as_retriever()

    # Answer
    answerTemplate = """
        You are a helpful and professional assistant specialized in nutrition.

        Your task is to answer user questions using the provided context and history. If the answer is not found in the context, say "I'm not sure based on the provided information." or continue the conversation in a direction headed with nutrition

        ---
        History:
        {history}

        ---
        Context:
        {context}

        ---
        Question:
        {question}

        Answer:
        """
    answerPrompt = ChatPromptTemplate.from_template(answerTemplate)
    answerChain = answerPrompt | llm | StrOutputParser()

    # Current Chain 
    chain = (
        {"question": RunnablePassthrough(), "history": RunnablePassthrough(), "context": standalone_chain | retriever | combine}
        | answerChain
    )

    result = chain.invoke({"question": question,
                           "history": history})

    return {"role": "system",
            "content": result}