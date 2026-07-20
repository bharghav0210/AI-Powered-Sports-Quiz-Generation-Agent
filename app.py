import streamlit as st

from src.agent import QuizAgent
from src.config import (
    DIFFICULTIES,
    SPORTS,
    MAX_QUESTION_COUNT,
    MIN_QUESTION_COUNT,
)

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Sports Quiz Generator",
    page_icon="🏆",
    layout="wide",
)

# ============================================================
# SESSION STATE
# ============================================================

if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = None

# ============================================================
# AGENT
# ============================================================

agent = QuizAgent()

# ============================================================
# HEADER
# ============================================================

st.title("🏆 Sports Quiz Generation Agent")
st.markdown(
    """
Generate AI-powered sports quizzes using **RAG (Retrieval-Augmented Generation)**.

The application retrieves sports knowledge from a vector database,
builds contextual prompts, and generates quizzes using an LLM.
"""
)

st.divider()

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.header("⚙ Quiz Settings")

    sport = st.selectbox(
        "Select Sport",
        SPORTS,
    )

    difficulty = st.selectbox(
        "Difficulty",
        DIFFICULTIES,
    )

    num_questions = st.slider(
        "Number of Questions",
        min_value=MIN_QUESTION_COUNT,
        max_value=MAX_QUESTION_COUNT,
        value=5,
    )

    st.divider()

    st.subheader("📊 Knowledge Base")

    try:
        info = agent.collection_info()

        st.metric(
            "Stored Documents",
            info.get("document_count", 0),
        )

    except Exception:
        st.info("Database statistics unavailable.")

# ============================================================
# GENERATE BUTTON
# ============================================================

col1, col2 = st.columns([2, 1])

with col1:

    generate = st.button(
        "🚀 Generate Quiz",
        use_container_width=True,
    )

with col2:

    clear = st.button(
        "🗑 Clear",
        use_container_width=True,
    )

if clear:
    st.session_state.quiz_result = None
    st.rerun()

# ============================================================
# GENERATE QUIZ
# ============================================================

if generate:

    with st.spinner("Generating your quiz..."):

        result = agent.generate_quiz(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions,
        )

        st.session_state.quiz_result = result

# ============================================================
# DISPLAY RESULTS
# ============================================================

if st.session_state.quiz_result:

    result = st.session_state.quiz_result

    if not result["success"]:

        st.error(result["error"])

    else:

        st.success("Quiz generated successfully!")

        st.subheader("Quiz Details")

        col1, col2, col3 = st.columns(3)

        col1.metric("Sport", result["sport"])
        col2.metric("Difficulty", result["difficulty"])
        col3.metric("Questions", result["num_questions"])

        st.divider()

        st.subheader("Generated Quiz")

        st.text_area(
            label="",
            value=result["quiz"],
            height=600,
        )

        st.download_button(
            label="📥 Download Quiz",
            data=result["quiz"],
            file_name=f"{result['sport'].lower()}_quiz.txt",
            mime="text/plain",
        )

# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "Sports Quiz Generation Agent • Powered by ChromaDB, "
    "Sentence Transformers, DuckDuckGo Search, and LLMs "
    "(OpenAI / Ollama)"
)