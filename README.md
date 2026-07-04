# 🩺 Medical Assistant — RAG-Based Medical Chatbot

A **Medical Domain Chatbot** built using **Retrieval-Augmented Generation (RAG)**. Upload your own medical documents (textbooks, reports, notes) and get accurate, context-grounded answers powered by state-of-the-art LLMs.

<p align="center">
  <img src="https://miro.medium.com/1*myvGbGdZPDQ3fJVVJsxBnA.png" alt="RAG Architecture" width="800">
</p>

---

## 🎓 What is RAG?

**Retrieval-Augmented Generation (RAG)** enhances language models by supplying relevant external context from a knowledge base before generating a response. This reduces hallucinations and significantly improves accuracy — especially critical in specialized, high-stakes domains like medicine.

---

## 🔄 Architecture

```
User Input
   ↓
Query Embedding → Pinecone Vector DB ← Embedded Chunks ← Chunking ← PDF Loader
   ↓
Retrieved Docs
   ↓
RAG Chain (Groq + LangChain)
   ↓
LLM-generated Answer
```

---

## 📚 Features

- 📄 Upload medical PDFs (notes, textbooks, reports)
- ✂️ Auto-extracts text and splits it into semantic chunks
- 🧠 Embeds content using Google Generative AI / BGE embeddings
- 🗂️ Stores and retrieves vectors via **Pinecone DB**
- ⚡ Uses **Groq's `llama-3.3-70b-versatile`**  via **LangChain** for fast, accurate generation
- 🚀 **FastAPI** backend with clean endpoints for upload and Q&A
- 💬 Streamlit-based chat interface with history download

---

## 🌐 Tech Stack

| Component     | Technology                     |
|---------------|---------------------------------|
| LLM           | Groq API(llama-3.3-70b-versatile)|
| Embeddings    | Google Generative AI / BGE      |
| Vector DB     | Pinecone                        |
| Framework     | LangChain                       |
| Backend       | FastAPI                         |
| Frontend      | Streamlit                       |

---

## 📡 API Endpoints

| Method | Endpoint         | Description                          |
|--------|------------------|---------------------------------------|
| `POST` | `/upload_pdfs/`  | Upload one or more PDF files          |
| `POST` | `/ask/`          | Ask a question — form field: `question` |

---

## 📁 Folder Structure

```
└── 📁assets
    ├── DIABETES.pdf
    ├── MedicalAssistant.pdf
    └── medicalAssistant.png
└── 📁client
    └── 📁components
        ├── chatUI.py
        ├── history_download.py
        ├── upload.py
    └── 📁utils
        ├── api.py
    ├── app.py
    ├── config.py
    └── requirements.txt
└── 📁server
    └── 📁middlewares
        ├── exception_handlers.py
    └── 📁modules
        ├── llm.py
        ├── load_vectorstore.py
        ├── pdf_handlers.py
        ├── query_handlers.py
    └── 📁routes
        ├── ask_question.py
        ├── upload_pdfs.py
    └── 📁uploaded_docs
        ├── DIABETES.pdf
        ├── Supratim Nag - LOR.pdf
    ├── .env
    ├── logger.py
    ├── main.py
    ├── requirements.txt
    └── test.py
```

---

## ⚡ Quick Setup

### 🔧 Backend (Server)

```bash
# Clone the repo
git clone https://github.com/snsupratim/medicalAssistant.git
cd medicalAssistant/server

# Create virtual env
uv venv
.venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Set environment variables (.env)
GOOGLE_API_KEY=...
GROQ_API_KEY=...
PINECONE_API_KEY=...

# Run the server
uvicorn main:app --reload --port 8000
```

### 💻 Frontend (Client)

```bash
cd medicalAssistant/client

# Create virtual env
uv venv
.venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
uv pip install -r requirements.txt

# Run the app
streamlit run app.py
```

-

## 🌟 Credits

Built with ❤️ by **Rohit Shankar**
Inspired by the **LangChain**, **Groq**, **Pinecone**, and **FastAPI** ecosystems.

---

## 🎉 License

This project is licensed under the **MIT License**.
