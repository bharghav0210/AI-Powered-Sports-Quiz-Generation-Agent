# 🏆 Sports Quiz Generation Agent

An AI-powered **Sports Quiz Generation Agent** built using **Retrieval-Augmented Generation (RAG)**. The application retrieves sports knowledge from trusted web sources, stores it in a vector database, and generates contextual multiple-choice quizzes using a Large Language Model (LLM).

The project demonstrates a complete RAG pipeline, semantic search, vector databases, prompt engineering, and modern AI application architecture.

---

## 🚀 Features

* AI-generated sports quizzes
* Retrieval-Augmented Generation (RAG)
* Semantic search using vector embeddings
* Automatic knowledge ingestion from the web
* ChromaDB vector database
* DuckDuckGo search integration
* OpenAI and Ollama support
* Streamlit web interface
* Download generated quizzes
* Modular, production-style architecture

---

# 🏗️ Architecture

```text
                      User
                        │
                        ▼
                Streamlit Application
                        │
                        ▼
                  QuizAgent
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
 Knowledge Retrieval                LLM Service
        │                       (OpenAI / Ollama)
        ▼
     ChromaDB
        ▲
        │
Knowledge Ingestion
        │
DuckDuckGo Search
```

---

# 📂 Project Structure

```text
sports-quiz-agent/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
│
├── chroma_db/
│
└── src/
    ├── __init__.py
    ├── agent.py
    ├── config.py
    ├── database.py
    ├── ingestion.py
    ├── llm.py
    ├── prompts.py
    ├── search.py
    ├── utils.py
    │
    └── tests/
        ├── test_agent.py
        ├── test_database.py
        ├── test_env.py
        ├── test_ingestion.py
        └── test_search.py
```

---

# ⚙️ Tech Stack

| Category        | Technology               |
| --------------- | ------------------------ |
| Language        | Python 3.11+             |
| UI              | Streamlit                |
| Vector Database | ChromaDB                 |
| Embedding Model | Sentence Transformers    |
| Search Engine   | DuckDuckGo Search (DDGS) |
| LLM Providers   | OpenAI / Ollama          |
| Environment     | python-dotenv            |

---

# 🔄 Workflow

```text
User Request
      │
      ▼
Select Sport
      │
      ▼
Check ChromaDB
      │
      ▼
Knowledge Exists?
      │
 ┌────┴────┐
 │         │
No         Yes
 │         │
 ▼         │
Search Web │
 │         │
 ▼         │
Create Embeddings
 │
 ▼
Store in ChromaDB
 │
 ▼
Retrieve Relevant Documents
 │
 ▼
Build Prompt
 │
 ▼
LLM (OpenAI / Ollama)
 │
 ▼
Generate Quiz
```

---

# 📦 Installation

## 1. Clone the repository

```bash
git clone https://github.com/<your-username>/sports-quiz-agent.git

cd sports-quiz-agent
```

---

## 2. Create a virtual environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure environment variables

Create a `.env` file.

Example:

```env
LLM_PROVIDER=ollama

OPENAI_API_KEY=
OPENAI_MODEL=gpt-4.1-mini

OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2:3b
```

---

# 🦙 Running with Ollama

Install Ollama.

Pull a model.

```bash
ollama pull llama3.2:3b
```

or

```bash
ollama pull qwen2.5:7b
```

Start the Ollama server.

```bash
ollama serve
```

---

# 🤖 Running with OpenAI

Update the `.env` file.

```env
LLM_PROVIDER=openai

OPENAI_API_KEY=YOUR_OPENAI_API_KEY

OPENAI_MODEL=gpt-4.1-mini
```

---

# ▶️ Running the Application

```bash
streamlit run app.py
```

---

# 🧪 Running Tests

Run the complete integration test.

```bash
python -m src.tests.test_agent
```

Other tests

```bash
python -m src.tests.test_database

python -m src.tests.test_search

python -m src.tests.test_ingestion

python -m src.tests.test_env
```

---

# 📸 Sample Output

```text
Question 1

What is the estimated origin of Cricket?

A. 15th century
B. 16th century
C. 17th century
D. 18th century

Answer:
B. 16th century

Explanation:
Cricket originated in England during the 16th century.
```

---

# 📈 Future Improvements

* PDF export
* Quiz scoring
* User authentication
* Leaderboard
* Timed quizzes
* Source citations
* Multi-language support
* Additional vector database support
* Support for more LLM providers
* Docker deployment
* CI/CD pipeline
* Cloud deployment

---

# 🎯 Learning Outcomes

This project demonstrates practical experience with:

* Retrieval-Augmented Generation (RAG)
* Semantic Search
* Vector Databases
* Prompt Engineering
* LLM Integration
* Streamlit Development
* Production-style Python Architecture
* Dependency Injection
* Object-Oriented Design
* AI Application Development

---

# 📄 License

This project is intended for educational and portfolio purposes.

---

# 👨‍💻 Author

**Madhiraju Bharghav**

AI • Data Science • Machine Learning • Generative AI

If you found this project useful, consider giving it a ⭐ on GitHub.
