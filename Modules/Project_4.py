# ================ Code for Interacting with Gen AI ===========================

# Upload PDF File Manually.
# Ask questions related to the uploaded file (prompts) to get the answer
# Streamlit Used to interact
# Framework Langchain is used
# Used Vector Stores VectorstoreIndexCreator through langchain.indexes
# Used "load_qa_chain" for question and answers
# Used "get_relevant_documents" to retrieve relevant documents
# OpenAIEmbeddings() not required as VectorstoreIndexCreator Converts text chunks into 
  # vector embeddings 

# Chunk Size : 3000

# =============================================================================

import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.indexes import VectorstoreIndexCreator
import tempfile
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def load_pdf_and_create_index(pdf_file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf_file.read())
        tmp_file_path = tmp_file.name

    loader = PyMuPDFLoader(tmp_file_path)
    pages = loader.load_and_split()
    
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=3000,
        chunk_overlap=200
    )
    
    texts = text_splitter.split_documents(pages)
    index_creator = VectorstoreIndexCreator()
    vectorstore_index = index_creator.from_documents(texts).vectorstore

    return vectorstore_index

def main():
    st.title("Gen AI Project 4")

    pdf_file = st.file_uploader("Upload a PDF File", type="pdf")

    if pdf_file is not None:
        # Use the first method to create the index
        vectorstore_index = load_pdf_and_create_index(pdf_file)

        query = st.text_input("Ask a question")

        if query:
            
            retrieved_docs = vectorstore_index.as_retriever(search_kwargs={"fetch_score": True}).get_relevant_documents(query)

            # Convert retrieved documents to text
            #retrieved_texts = [doc.page_content for doc in retrieved_docs]

            # Initialize the custom QA chain for answering
            #embeddings = OpenAIEmbeddings()
            #knowledge_base = FAISS.from_texts(retrieved_texts, embedding=embeddings)
            llm = OpenAI(openai_api_key=OPENAI_API_KEY)
            chain = load_qa_chain(llm, chain_type="stuff")

            # Step 2: Use the custom QA chain to generate the answer
            response = chain.run(input_documents=retrieved_docs, question=query)

            st.write(f"Answer: {response}")

if __name__ == "__main__":
    main()
