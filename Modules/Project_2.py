# ================ Code for Interacting with Gen AI ===========================

# Upload PDF File Manually.
# Ask questions related to the uploaded file (prompts) to get the answer
# Streamlit Used to interact
# Framework Langchain is used
# Used Vector Stores FAISS through langchain
# Used "load_qa_chain" for question and answers

# Chunk Size : 3000

# =============================================================================

from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
import os

OPENAI_API_KEY       = os.getenv('OPENAI_API_KEY')

load_dotenv()

def main():
    
    st.header(body   = "Gen AI Project 2 💬")
    pdf              = st.file_uploader(label="Upload your pdf file", type="pdf")
    
    if pdf is not None:
        
        pdf_reader   = PdfReader(pdf)
        pdf_text     = ""
        for page in pdf_reader.pages:
            pdf_text = pdf_text + page.extract_text()
        
        text_splitter = CharacterTextSplitter(
            separator       ="\n",
            chunk_size      = 3000,
            chunk_overlap   = 200,
            length_function = len,)

        chunks         = text_splitter.split_text(pdf_text)

        embeddings     = OpenAIEmbeddings()
        knowledge_base = FAISS.from_texts(chunks, embedding = embeddings)

        user_question  = st.text_input(label="Ask your question")

        if user_question:
            docs       = knowledge_base.similarity_search(user_question)
            llm        = OpenAI(openai_api_key = OPENAI_API_KEY)
            chain      = load_qa_chain(llm, chain_type="stuff")
            response   = chain.run(input_documents = docs, question = user_question)
            st.write(response)

if __name__ == '__main__':
    main()