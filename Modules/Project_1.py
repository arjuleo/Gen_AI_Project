# ================ Code for Interacting with Gen AI ===========================

# Upload PDF File Manually.
# Ask questions related to the uploaded file (prompts) to get the answer
# Streamlit Used to interact
# Framework Langchain is used
# Used VectorstoreIndexCreator for creating vector stores from various data sources
  # This is helpful in efficient Searching and Retrieval
# # Used "RetrievalQA" for question and answers

# Chunk Size : 3000

# =============================================================================

import streamlit as st
from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.indexes import VectorstoreIndexCreator
import tempfile
import os

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

def load_pdf_and_create_index(pdf_file):
    
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(pdf_file.read())
        tmp_file_path = tmp_file.name

    loader            = PyMuPDFLoader(tmp_file_path)
    pages             = loader.load_and_split()
    
    text_splitter     = CharacterTextSplitter(
                        separator     ="\n",
                        chunk_size    = 3000,
                        chunk_overlap = 200)
    
    texts             = text_splitter.split_documents(pages)
    index_creator     = VectorstoreIndexCreator()
    vectorstore_index = index_creator.from_documents(texts).vectorstore

    return vectorstore_index

def main():
    
    st.title("Gen AI Project 1")
    pdf_file = st.file_uploader("Upload a PDF File", type="pdf")

    if pdf_file is not None:
        
        vectorstore_index = load_pdf_and_create_index(pdf_file)

        qa = RetrievalQA.from_chain_type(
            llm        = OpenAI(temperature=0.8),
            chain_type = "stuff",
            retriever  = vectorstore_index.as_retriever(search_kwargs={"fetch_score": True}),
            return_source_documents=True,)

        query = st.text_input("Ask a question about the financial report")

        if query:
            result = qa({"query": query})
            st.write(f"Answer: {result['result']}")
            
if __name__ == "__main__":
    main()

