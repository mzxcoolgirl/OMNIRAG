# 📚 OmniRAG – Chat with Your PDF using AI

OmniRAG is a **Retrieval-Augmented Generation (RAG)** based application that allows users to upload a PDF and ask questions about its content.
It combines **semantic search + hybrid retrieval + LLM (Groq API)** to generate accurate, context-aware answers.

---

## 🚀 Features

* 📄 Upload any PDF document
* 🔍 Extract and split text into meaningful chunks
* 🧠 Generate embeddings using Sentence Transformers
* ⚡ Fast similarity search using FAISS
* 🔀 Hybrid retrieval (BM25 + vector search)
* 🤖 LLM-based answer generation (Groq API)
* 💬 Interactive chat interface (Streamlit)
* 📜 Displays relevant context for transparency

---

## 🧠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **LLM API:** Groq
* **Embeddings:** Sentence Transformers
* **Vector DB:** FAISS
* **Keyword Search:** BM25

---

## 📂 Project Structure

```
OMNIRAG/
│
├── rag/
│   ├── ingestion.py        # PDF text extraction
│   ├── chunking.py         # Text splitting
│   ├── embeddings.py       # Embedding generation
│   ├── retriever.py        # FAISS index & search
│   ├── hybrid_retriever.py # Hybrid (BM25 + vector)
│   ├── reranker.py         # Result reranking
│   └── llm.py              # LLM API integration
│
├── ui/
│   └── app.py              # Streamlit UI
│
├── data/
│   └── documents/          # Uploaded PDFs
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/OMNIRAG.git
cd OMNIRAG
```

---

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Add API Key (Groq)

Create a file:

```
.streamlit/secrets.toml
```

Add:

```toml
API_KEY = "your_groq_api_key"
```

---

### 5. Run the app

```bash
streamlit run ui/app.py
```

---

## 🌐 Deployment (Streamlit Cloud)

1. Push project to GitHub
2. Go to Streamlit Cloud
3. Select repository
4. Set entry file:

```
ui/app.py
```

5. Add secrets in dashboard:

```toml
API_KEY = "your_groq_api_key"
```

6. Deploy 🚀

---

## 🧠 How It Works (RAG Pipeline)

1. **PDF Upload**
2. **Text Extraction**
3. **Chunking**
4. **Embedding Generation**
5. **Vector Search (FAISS)**
6. **Hybrid Retrieval (BM25 + Embeddings)**
7. **Context Creation**
8. **LLM Answer Generation**

---

## 🎯 Example Use Cases

* 📖 Study notes from PDFs
* 📑 Research paper Q&A
* 📘 Book summarization
* 🧾 Document analysis

---
## 🌐 Live Demo

🚀 Try the deployed application here:  
👉 https://omnirag-jlgpymdt5xyjsuqtrmunpt.streamlit.app/

---

### 📌 What you can do:
- Upload a PDF
- Ask questions
- Get AI-powered answers

## ⚠️ Limitations

* Depends on quality of PDF text extraction
* Large PDFs may take time to process
* Accuracy depends on retrieval quality

---

## 🔮 Future Improvements

* Multi-PDF support
* Highlight answers in document
* Chat history persistence
* Better UI/UX
* Streaming responses

---

## 👩‍💻 Author

**Muskan**
B.Tech CSE (AI/ML)
GNA University

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
