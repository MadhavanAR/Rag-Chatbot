import streamlit as st
import tempfile
import os

# ---- LangChain imports (FINAL correct ones) ----
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaEmbeddings, OllamaLLM

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# -----------------------------------------------
# Streamlit UI
# -----------------------------------------------
st.set_page_config(page_title="Resume RAG Bot (Ollama)", layout="wide")
st.title("📄 Resume Screening RAG Chatbot")
st.write("Upload bulk resume PDFs and ask for a specific candidate")

# -----------------------------------------------
# Upload PDFs
# -----------------------------------------------
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success("Processing resumes...")

    all_docs = []

    # -----------------------------------------------
    # Load PDFs
    # -----------------------------------------------
    for pdf in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(pdf.read())
            tmp_path = tmp.name

        loader = PyPDFLoader(tmp_path)
        docs = loader.load()

        # Add filename metadata
        for d in docs:
            d.metadata["source"] = pdf.name

        all_docs.extend(docs)
        os.remove(tmp_path)

    # -----------------------------------------------
    # Split text
    # -----------------------------------------------
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(all_docs)

    # -----------------------------------------------
    # Embeddings + Vector DB (Ollama)
    # -----------------------------------------------
    embeddings = OllamaEmbeddings(model="nomic-embed-text:latest")
    vector_db = FAISS.from_documents(chunks, embeddings)

    retriever = vector_db.as_retriever(search_kwargs={"k": 5})

    # -----------------------------------------------
    # LLM (Ollama)
    # -----------------------------------------------
    llm = OllamaLLM(
        model="llama3.2:latest",
        temperature=0
    )

    # -----------------------------------------------
    # Prompt (RAG)
    # -----------------------------------------------
    prompt = ChatPromptTemplate.from_template("""
You are an HR assistant.
Answer ONLY using the resume context provided.
If the candidate is not found, say:
"Candidate not found in uploaded resumes."

Context:
{context}

Question:
{question}
""")

    # -----------------------------------------------
    # RAG Chain (LCEL – LangChain 1.x)
    # -----------------------------------------------
    rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    st.success("✅ Resumes indexed successfully!")

    # -----------------------------------------------
    # Query Input
    # -----------------------------------------------
    query = st.text_input(
        "Ask your question",
        placeholder="e.g. Find Java developer with 2 years experience"
    )

    if query:
        with st.spinner("Searching resumes..."):
            result = rag_chain.invoke(query)

        st.subheader("📌 Answer")
        st.write(result)
