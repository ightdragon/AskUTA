# Academic Advisor RAG Chatbot

An intelligent Retrieval-Augmented Generation (RAG) conversational agent designed to act as a digital academic advisor. The system crawls and scrapes university web pages, chunks and indexes the unstructured text locally into a vector database, and leverages a Large Language Model (LLM) to deliver context-aware, highly specific answers regarding registration, financial aid, and campus inquiries.

---

## 🛠️ Components Breakdown

### 1. Data Gathering & Scraping
* **`scrape_main.py`**: Discovers internal website links starting from a base URL (configured for `https://uta.edu` by default) up to a designated threshold. It then strips out UI boilerplate (headers, footers, scripts) and saves the raw body text.
* **`scrape_utils.py`**: Provides utility logic for determining valid internal links and sanitizing text strings into safe filenames.

### 2. Knowledge Ingestion & Vector Storage
* **`ingest_docs.py`**: Reads the text assets out of the `scraped_pages` folder. It splits the data using a `RecursiveCharacterTextSplitter` into manageable chunks (500 characters with a 50-character overlap), embeds them using HuggingFace's `all-MiniLM-L6-v2` model, and stores them in a local `FAISS` database index.

### 3. RAG Orchestration
* **`rag_pipeline.py`**: Initializes the underlying LangChain workflow. It reloads the local FAISS index, sets up a semantic retriever, and builds a structured prompt for Google's `gemini-1.5-pro-001` LLM, directing it to act as an academic advisor and extract critical contact information accurately.

### 4. Application Interfaces
* **`test_chat.py`**: A convenient command-line interface loop allowing developers to query the agent interactively inside a terminal.
* **`main.py`**: A production-ready asynchronous `FastAPI` instance exposing a POST endpoint (`/chat`). Includes unrestricted Cross-Origin Resource Sharing (CORS) configurations to seamlessly interface with frontend client setups.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* A valid Google Gemini API Key

### Installation

1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   ```bash
   pip install fastapi uvicorn langchain langchain-community langchain-google-genai beautifulsoup4 requests faiss-cpu sentence-transformers python-dotenv
