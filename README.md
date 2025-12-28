# Resume Screening RAG Chatbot

A Retrieval-Augmented Generation (RAG) application for intelligent resume screening and candidate discovery. Built with Streamlit and LangChain, enabling natural language queries over uploaded resume PDFs.

## Features

- Bulk PDF resume upload
- Natural language query interface
- RAG-based semantic search
- FAISS vector database for efficient retrieval
- Context-aware responses limited to uploaded content

## Tech Stack

- **Streamlit**: Web UI framework
- **LangChain**: LLM orchestration
- **Ollama**: Local LLM and embeddings (nomic-embed-text, llama3.2)
- **FAISS**: Vector similarity search
- **PyPDF**: PDF parsing

## Prerequisites

- Python 3.8+
- Ollama installed and running locally
- Required Ollama models:
  ```bash
  ollama pull nomic-embed-text
  ollama pull llama3.2
  ```

## Installation

```bash
git clone https://github.com/MadhavanAR/Rag-Chatbot.git
cd Rag-Chatbot

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Usage

Start the application:
```bash
streamlit run app.py
```

1. Upload one or multiple resume PDFs via the file uploader
2. Wait for processing and indexing to complete
3. Enter natural language queries (e.g., "Find Java developer with 2 years experience")
4. View candidate matches and relevant information

## Architecture

1. **Document Loading**: PDFs parsed with PyPDFLoader
2. **Chunking**: Text split into 1000-character chunks (150 overlap) using RecursiveCharacterTextSplitter
3. **Embedding**: Chunks embedded using Ollama nomic-embed-text model
4. **Indexing**: Vectors stored in FAISS database
5. **Retrieval**: Top-k (k=5) similar chunks retrieved for each query
6. **Generation**: llama3.2 LLM generates answers from retrieved context

## Example Queries

- "Find candidates with Python programming experience"
- "Who has a master's degree in Computer Science?"
- "Show developers with 5+ years of experience"
- "Find candidates with Docker and Kubernetes experience"

## Privacy

All processing occurs locally. No data is transmitted to external services.

## License

MIT License

## Author

MadhavanAR - [GitHub](https://github.com/MadhavanAR)
