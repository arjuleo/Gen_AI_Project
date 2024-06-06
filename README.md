Modules Folder contains 4 python files, Project_1.py, Project_2.py, Project_3.py and Project_4.py on Gen AI.

Project_4.py: The Robust Code compared to other 3 code snippets - Faster in opening the interface, and faster in generating response.
              This file contains python code and it was the fourth attempt to create an Generative AI
              Upload PDF File Manually.
              Ask questions related to the uploaded file (prompts) to get the answer
              Streamlit Used to interact
              Framework Langchain is used
              Used Vector Stores VectorstoreIndexCreator through langchain.indexes
              Used "load_qa_chain" for question and answers
              Used "get_relevant_documents" to retrieve relevant documents
              OpenAIEmbeddings() not required as VectorstoreIndexCreator Converts text chunks into vector embeddings 
              Chunk Size : 3000

Project_3.py: Ths Code is prepared for "Intelligent Automation", where It automatically takes in PDF File and pre-defined prompt to give the response.
              This file contains python code and it was the third attempt to create an Generative AI
              This Gen AI directly takes in the PDF File and prompt Automatically.
              Provides the answer and saves in the variable "result"
              No Streamlit Used
              Framework Langchain is used
              Used Vector Stores FAISS through langchain
              Used "load_qa_chain" for question and answers
              Chunk Size : 3000

Project_2.py: Ths Code is prepared as same as Project_3.py, but here Streamlit is used to interact manually
              This file contains python code and it was the second attempt to create an Generative AI
              Upload PDF File Manually.
              Ask questions related to the uploaded file (prompts) to get the answer
              Streamlit Used to interact
              Framework Langchain is used
              Used Vector Stores FAISS through langchain
              Used "load_qa_chain" for question and answers
              Chunk Size : 3000

Project_1.py: This file contains python code and it was the first attempt to create an Generative AI
              Upload PDF File Manually.
              Ask questions related to the uploaded file (prompts) to get the answer
              Streamlit Used to interact
              Framework Langchain is used
              Used VectorstoreIndexCreator for creating vector stores from various data sources
              This is helpful in efficient Searching and Retrieval
              Used "RetrievalQA" for question and answers
              Chunk Size : 3000
              
