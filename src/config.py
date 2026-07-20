from pathlib import Path
import os

from dotenv import load_dotenv

# ============================================================
# Load Local Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Streamlit Secrets (Optional)
# ============================================================

try:
    import streamlit as st

    def get_config(key: str, default=None):
        return st.secrets.get(key, os.getenv(key, default))

except Exception:

    def get_config(key: str, default=None):
        return os.getenv(key, default)


# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_DB_PATH = BASE_DIR / "chroma_db"

# ============================================================
# LLM Provider
# ============================================================

LLM_PROVIDER = get_config(
    "LLM_PROVIDER",
    "gemini",
)

# ============================================================
# OpenAI
# ============================================================

OPENAI_API_KEY = get_config(
    "OPENAI_API_KEY"
)

OPENAI_MODEL = get_config(
    "OPENAI_MODEL",
    "gpt-4.1-mini",
)

# ============================================================
# Gemini
# ============================================================

GEMINI_API_KEY = get_config(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = get_config(
    "GEMINI_MODEL",
    "gemini-flash-latest",
)

# ============================================================
# Ollama
# ============================================================

OLLAMA_BASE_URL = get_config(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)

OLLAMA_MODEL = get_config(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)

# ============================================================
# ChromaDB
# ============================================================

COLLECTION_NAME = "sports_knowledge"

EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# ============================================================
# Search Configuration
# ============================================================

SEARCH_RESULTS = 5

TOP_K = 5

# ============================================================
# Quiz Configuration
# ============================================================

DEFAULT_QUESTION_COUNT = 5

MIN_QUESTION_COUNT = 1

MAX_QUESTION_COUNT = 10

# ============================================================
# Supported Sports
# ============================================================

SPORTS = [
    "Cricket",
    "Football",
    "Basketball",
    "Tennis",
    "Hockey",
    "Baseball",
    "Badminton",
    "Volleyball",
    "Olympics",
]

# ============================================================
# Difficulty Levels
# ============================================================

DIFFICULTIES = [
    "Easy",
    "Medium",
    "Hard",
]