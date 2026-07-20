from typing import Dict, List

from src.config import TOP_K
from src.database import ChromaDatabase
from src.ingestion import KnowledgeIngestion
from src.llm import get_llm
from src.prompts import QUIZ_PROMPT


class QuizAgent:
    """
    Main AI Agent responsible for generating sports quizzes.
    """

    def __init__(self) -> None:
        """
        Initialize all required services.
        """

        # Shared database
        self.database = ChromaDatabase()

        # Knowledge ingestion pipeline
        self.ingestion = KnowledgeIngestion(
            database=self.database
        )

        # LLM Provider
        self.llm = get_llm()

    # ==========================================================
    # PUBLIC API
    # ==========================================================

    def generate_quiz(
        self,
        sport: str,
        difficulty: str,
        num_questions: int,
    ) -> Dict:
        """
        Generate a sports quiz.

        Parameters
        ----------
        sport : str

        difficulty : str

        num_questions : int

        Returns
        -------
        dict
        """

        try:

            # ---------------------------------------------
            # Step 1 : Ensure Knowledge Exists
            # ---------------------------------------------

            if not self.database.sport_exists(sport):

                success = self.ingestion.ingest_sport(
                    sport
                )

                if not success:

                    return {
                        "success": False,
                        "error": (
                            f"Unable to collect knowledge "
                            f"for '{sport}'."
                        ),
                    }

            # ---------------------------------------------
            # Step 2 : Retrieve Context
            # ---------------------------------------------

            documents = self.database.retrieve_documents(
                sport=sport,
                query=f"{sport} rules history tournaments facts",
                top_k=TOP_K,
            )

            context = self._build_context(documents)

            if not context:

                return {
                    "success": False,
                    "error": (
                        "No knowledge available for quiz generation."
                    ),
                }

            # ---------------------------------------------
            # Step 3 : Build Prompt
            # ---------------------------------------------

            prompt = self._build_prompt(
                sport=sport,
                difficulty=difficulty,
                num_questions=num_questions,
                context=context,
            )

            # ---------------------------------------------
            # Step 4 : Generate Quiz
            # ---------------------------------------------

            quiz = self.llm.generate(prompt)

            # ---------------------------------------------
            # Step 5 : Return Response
            # ---------------------------------------------

            return {
                "success": True,
                "sport": sport,
                "difficulty": difficulty,
                "num_questions": num_questions,
                "quiz": quiz,
            }

        except Exception as error:

            return {
                "success": False,
                "error": str(error),
            }

    # ==========================================================
    # PRIVATE HELPERS
    # ==========================================================

    def _build_context(
        self,
        documents: List[str],
    ) -> str:
        """
        Convert retrieved documents into a single
        context string.
        """

        if not documents:
            return ""

        context = []

        for index, document in enumerate(
            documents,
            start=1,
        ):

            context.append(
                "\n".join(
                    [
                        "=" * 70,
                        f"DOCUMENT {index}",
                        "=" * 70,
                        document,
                    ]
                )
            )

        return "\n\n".join(context)

    def _build_prompt(
        self,
        sport: str,
        difficulty: str,
        num_questions: int,
        context: str,
    ) -> str:
        """
        Populate the quiz prompt template.
        """

        return QUIZ_PROMPT.format(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions,
            context=context,
        )

    # ==========================================================
    # UTILITY METHODS
    # ==========================================================

    def collection_info(self) -> Dict:
        """
        Return ChromaDB statistics.
        """

        return self.database.collection_info()

    def clear_database(self) -> None:
        """
        Remove all stored documents.
        Useful during development/testing.
        """

        self.database.clear_collection()