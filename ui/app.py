import streamlit as st
import numpy as np
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

from rag.ingestion import extract_text
from rag.chunking import split_text
from rag.embeddings import create_embeddings, model
from rag.retriever import build_index, search
from rag.llm import generate_answer
from rag.reranker import rerank
from rag.hybrid_retriever import HybridRetriever

st.title("OmniRAG")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, message in st.session_state.chat_history:
    if role == "User":
        st.sidebar.markdown(f"**🧑 {message}**")
    else:
        st.sidebar.markdown(f"🤖 {message}")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    save_path = os.path.join("data/documents", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded successfully!")

    text = extract_text(save_path)

    chunks = split_text(text)

    st.write("Chunks created:", len(chunks))

    embeddings = create_embeddings(chunks)

    index = build_index(embeddings)
    
    retriever = HybridRetriever(chunks, embeddings, index)

    st.success("Embeddings created and stored in FAISS!")

    query = st.text_input("Ask a question about the document")

    if query:

        query_embedding = model.encode([query])

        retrieved_chunks = retriever.search(query_embedding, query)
        
        reranked_chunks = rerank(query, retrieved_chunks)
        
        context = " ".join(reranked_chunks)

        history = "\n".join(st.session_state.chat_history)

        answer = generate_answer(context, query, history)
        st.session_state.chat_history.append(f"User: {query}")
        st.session_state.chat_history.append(f"Assistant: {answer}")

        st.subheader("Answer")
        st.write(answer)
        