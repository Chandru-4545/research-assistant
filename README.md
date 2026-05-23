# 📄 AI Research Assistant

An AI-powered tool that lets you upload any PDF and ask questions about it — powered by Google Gemini and a local vector database (ChromaDB). This is a Retrieval-Augmented Generation (RAG) system that finds the most relevant parts of your document and uses an LLM to answer your questions accurately.

---

## 🧠 What Problem Does It Solve?

Reading long PDFs to find specific answers is slow and tedious. This tool lets you:
- Upload any PDF (research paper, report, textbook, etc.)
- Ask natural language questions about it
- Get precise, grounded answers in seconds

---

## 🏗️ Architecture

```
PDF File
   ↓
[PyPDF Loader] → Extract raw text
   ↓
[Text Splitter] → Split into 500-token chunks with overlap
   ↓
[ChromaDB] → Store chunks in a local vector database
   ↓
User asks a question
   ↓
[Semantic Search] → Find top 3 most relevant chunks
   ↓
[Gemini API] → Generate answer using retrieved context
   ↓
Answer displayed in Gradio UI
```

**Key Components:**
| Component | Role |
|-----------|------|
| `PyPDF` | Loads and reads PDF files |
| `LangChain` | Splits text into overlapping chunks |
| `ChromaDB` | Stores and retrieves text by semantic similarity |
| `Google Gemini API` | Generates answers from retrieved context |
| `Gradio` | Simple browser-based UI |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/research-assistant.git
cd research-assistant
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Set Your Gemini API Key

Get your free API key from [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

**On Mac/Linux:**
```bash
export GEMINI_API_KEY=your_api_key_here
```

**On Windows:**
```cmd
set GEMINI_API_KEY=your_api_key_here
```

### 4. Run the App

```bash
python app.py
```

Then open your browser and go to: `http://localhost:7860`

---

## 🚀 How to Use

1. Click **"Upload PDF"** and select any PDF file
2. Click **"Process Document"** — wait for the ✅ confirmation
3. Type your question in the text box
4. Click **"Ask"** and get your answer!

---

## 📁 Project Structure

```
research-assistant/
├── app.py              # Gradio UI — main entry point
├── ingest.py           # PDF loading, chunking, and storing in ChromaDB
├── query.py            # Semantic search + Gemini API call
├── requirements.txt    # All dependencies
└── README.md           # This file
```

---

## 📦 Requirements

```
google-generativeai
chromadb
pypdf
langchain
langchain-community
sentence-transformers
gradio
```

---

## 🔧 Engineering Challenge

The hardest part was **tuning the chunk size**. If chunks are too large, the context sent to Gemini contains too much irrelevant text and degrades answer quality. If chunks are too small, important context gets split across chunks and the answer is incomplete.

After testing, a chunk size of **500 tokens with 50-token overlap** gave the best balance between relevance and completeness.

---

## 📹 Demo

[▶️ Watch the demo video](https://your-loom-link-here.com)

---

## 📄 License

MIT License — free to use and modify.
