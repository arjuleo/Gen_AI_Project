# ================ Code for Intelligent Automation ============================

# This Gen AI directly takes in the PDF File and prompt Automatically.
# Provides the answer and saves in the variable "result"
# No Streamlit Used
# Framework Langchain is used
# Used Vector Stores FAISS through langchain
# Used "load_qa_chain" for question and answers

# Chunk Size : 3000

# =============================================================================

from PyPDF2 import PdfReader
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import OpenAI
import os

OPENAI_API_KEY       = os.getenv('OPENAI_API_KEY')

File_Path                    = "C:\\GEN_AI_Project"
PDFFile                      = "2022_Annual_Report_Sample" + ".pdf"
pdfreader                    = PdfReader(File_Path + "\\" + PDFFile)

query                        = "Provide Summary of Financial Performance of the Company"

raw_text = ''
for i, page in enumerate(pdfreader.pages):
    content = page.extract_text()
    if content:
        raw_text += content

text_splitter = CharacterTextSplitter(
    separator = "\n",
    chunk_size = 3000,
    chunk_overlap  = 200,
    length_function = len,
)

texts = text_splitter.split_text(raw_text)

embeddings      = OpenAIEmbeddings()
document_search = FAISS.from_texts(texts, embeddings)
chain           = load_qa_chain(OpenAI(), chain_type="stuff")

docs   = document_search.similarity_search(query)
result = chain.run(input_documents=docs, question=query)
print(result)

















