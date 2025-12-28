# 📄 Resume Screening RAG Chatbot

A powerful Retrieval-Augmented Generation (RAG) chatbot built with Streamlit and LangChain for intelligent resume screening and candidate discovery. Upload multiple resume PDFs and ask natural language questions to find the perfect candidate.

## ✨ Features

- **📚 Bulk Resume Upload**: Upload multiple PDF resumes at once
- **🔍 Intelligent Search**: Ask natural language questions to find candidates based on skills, experience, or qualifications
- **🤖 RAG-Powered**: Uses Retrieval-Augmented Generation for accurate, context-aware responses
- **⚡ Fast Retrieval**: Leverages FAISS vector database for efficient similarity search
- **🎯 Context-Aware**: Only returns answers based on uploaded resume content

## 🛠️ Technologies Used

- **Streamlit**: Interactive web application framework
- **LangChain**: Framework for building LLM-powered applications
- **Ollama**: Local LLM and embeddings (nomic-embed-text, llama3.2)
- **FAISS**: Vector database for similarity search
- **PyPDF**: PDF document parsing

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running locally
- Required Ollama models:
  - `nomic-embed-text:latest` (for embeddings)
  - `llama3.2:latest` (for language model)

### Installing Ollama Models

```bash
# Install the embedding model
ollama pull nomic-embed-text

# Install the language model
ollama pull llama3.2
```

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MadhavanAR/Rag-Chatbot.git
   cd Rag-Chatbot
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On macOS/Linux
   source venv/bin/activate
   
   # On Windows
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

1. **Start the Streamlit application**
   ```bash
   streamlit run app.py
   ```

2. **Upload Resume PDFs**
   - Click on the file uploader
   - Select one or multiple PDF resume files
   - Wait for the processing to complete

3. **Ask Questions**
   - Enter your question in the text input field
   - Examples:
     - "Find a Java developer with 2 years of experience"
     - "Who has experience with machine learning?"
     - "Show me candidates with React.js skills"

4. **View Results**
   - The chatbot will search through the uploaded resumes
   - Relevant candidates and their information will be displayed

## 📁 Project Structure

```
Rag-Chatbot/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── .gitignore           # Git ignore file
```

## 🔧 How It Works

1. **Document Loading**: PDF resumes are loaded and parsed using PyPDFLoader
2. **Text Splitting**: Documents are split into smaller chunks (1000 characters with 150 overlap) for better retrieval
3. **Embedding**: Text chunks are converted to vector embeddings using Ollama's nomic-embed-text model
4. **Vector Storage**: Embeddings are stored in a FAISS vector database
5. **Retrieval**: When a question is asked, relevant chunks are retrieved using similarity search
6. **Generation**: The LLM (llama3.2) generates an answer based on the retrieved context

## 🎯 Example Queries

- "Find candidates with Python programming experience"
- "Who has a master's degree in Computer Science?"
- "Show me developers with 5+ years of experience"
- "Find candidates who know Docker and Kubernetes"
- "Who has experience in financial technology?"

## 🔒 Privacy & Security

- All processing happens locally on your machine
- Resumes are processed in-memory (temporary files are cleaned up)
- No data is sent to external services
- Your data stays private

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/MadhavanAR/Rag-Chatbot/issues).

## 👤 Author

**MadhavanAR**

- GitHub: [@MadhavanAR](https://github.com/MadhavanAR)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://www.langchain.com/)
- LLM and embeddings provided by [Ollama](https://ollama.ai/)

