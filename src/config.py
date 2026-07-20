from pathlib import Path

from dotenv import load_dotenv
import os

# ============================================================
# Load Environment Variables
# ============================================================

load_dotenv()

# ============================================================
# Project Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

CHROMA_DB_PATH = BASE_DIR / "chroma_db"

# ============================================================
# OpenAI Configuration
# ============================================================

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL = os.getenv(
    "OPENAI_MODEL",
    "gpt-4.1-mini",
)

# ============================================================
# LLM Provider
# ============================================================

LLM_PROVIDER = os.getenv(
    "LLM_PROVIDER",
    "ollama",      # openai | ollama
)

# ============================================================
# Ollama
# ============================================================

OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434",
)

OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.2:3b",
)

# ============================================================
# Gemini
# ============================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY"
)

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-2.5-flash"
)
# ============================================================
# ChromaDB Configuration
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

MAX_QUESTION_COUNT = 10

MIN_QUESTION_COUNT = 1

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