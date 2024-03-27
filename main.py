# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
import streamlit as st
import pickle
import time
from langchain.llms import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain import PromptTemplate
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import LLMChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()

st.title("New Research Tool 📈")
st.sidebar.title("News Article URLs")

urls = []

for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)
process_url_clicked = st.sidebar.button("Process URLs")
file_path = "/Users/darshvaghasia/PycharmProjects/newsresearchtool/faiss_store_openai.pkl"

main_placeholder = st.empty()
llm= OpenAI(temperature= 0.9, max_tokens= 500,model_name="gpt-3.5-turbo-1106")

def get_conversational_chain():

    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    """
    prompt = PromptTemplate(template = prompt_template, input_variables = ["context", "question"])
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)
    # chain = LLMChain(llm = llm, prompt=prompt)

    return chain

if process_url_clicked:
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data Loading ... Started ...✅✅✅")
    data = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=['\n\n', '\n', '.', ','],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter ... Started ...✅✅✅")

    docs = text_splitter.split_documents(data)
    print(docs)
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started ... Started ...✅✅✅")
    time.sleep(2)
    with open(file_path, "wb") as f:
        pickle.dump(vectorstore_openai, f)
query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            vectorstore = pickle.load(f)
            # chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=vectorstore.as_retriever())
            # result = chain({"question": query}, return_only_outputs=True)
            docs = vectorstore.similarity_search(query)
            chain = get_conversational_chain()
            result = chain(
                {"input_documents": docs, "question": query}
                , return_only_outputs=True)
            # result = chain.run({"context": docs, "question": query})
            st.header("Answer")
            st.write(result["output_text"])
            # st.write(result)

