import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from rag.ingestion import extract_text
from rag.chunking import split_text
from rag.embeddings import create_embeddings, model
from rag.retriever import build_index
from rag.hybrid_retriever import HybridRetriever
from rag.reranker import rerank
from rag.llm import generate_answer

st.title("OmniRAG - Chat with PDF")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:

    save_path = os.path.join("data/documents", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF uploaded!")

    text = extract_text(save_path)
    chunks = split_text(text)

    st.write("Chunks created:", len(chunks))

    embeddings = create_embeddings(chunks)
    index = build_index(embeddings)

    retriever = HybridRetriever(chunks, embeddings, index)

    st.success("Embeddings ready!")

    query = st.text_input("Ask a question")

    if query:

        query_embedding = model.encode(query)

        # 🔥 HYBRID SEARCH
        retrieved_chunks = retriever.search(query_embedding, query, k=10)

        # 🔥 RERANK
        reranked_chunks = rerank(query, retrieved_chunks)

        context = " ".join(reranked_chunks[:3])

        if "history" not in st.session_state:
            st.session_state.history = ""

        history = st.session_state.history

        answer = generate_answer(context, query, history)

        st.session_state.history += f"\nUser: {query}\nAssistant: {answer}"

        st.subheader("Answer")
        st.write(answer)