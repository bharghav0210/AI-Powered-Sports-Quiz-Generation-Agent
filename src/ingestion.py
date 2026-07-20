from typing import List

from src.database import ChromaDatabase
from src.search import WebSearch


class KnowledgeIngestion:
    """
    Handles ingestion of sports knowledge into ChromaDB.
    """

    def __init__(self, database: ChromaDatabase) -> None:
        """
        Parameters
        ----------
        database : ChromaDatabase
            Shared ChromaDB instance.
        """

        self.database = database
        self.search = WebSearch()

    # =========================================================
    # Public Method
    # =========================================================

    def ingest_sport(self, sport: str) -> bool:
        """
        Search and ingest knowledge for a sport.

        Parameters
        ----------
        sport : str

        Returns
        -------
        bool
            True if ingestion succeeds.
        """

        # -----------------------------------------------------
        # Skip if already exists
        # -----------------------------------------------------

        if self.database.sport_exists(sport):

            print(f"[INFO] '{sport}' already exists in ChromaDB.")

            return True

        print(f"[INFO] Searching knowledge for '{sport}'...")

        results = self.search.search(sport)

        if not results:

            print("[ERROR] No search results found.")

            return False

        documents = self._prepare_documents(results)
        metadatas = self._prepare_metadata(results, sport)
        ids = self._generate_ids(sport, len(results))

        self.database.add_documents(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
        )

        print(f"[INFO] Stored {len(documents)} documents.")

        return True

    # =========================================================
    # Private Helpers
    # =========================================================

    def _prepare_documents(
        self,
        results: List[dict],
    ) -> List[str]:
        """
        Convert search results into document strings.
        """

        documents = []

        for result in results:

            document = (
                f"Title: {result['title']}\n\n"
                f"Source: {result['url']}\n\n"
                f"Summary:\n"
                f"{result['snippet']}"
            )

            documents.append(document)

        return documents

    def _prepare_metadata(
        self,
        results: List[dict],
        sport: str,
    ):
        """
        Create metadata for every document.
        """

        metadata = []

        for result in results:

            metadata.append(
                {
                    "sport": sport,
                    "title": result["title"],
                    "url": result["url"],
                    "source": "DuckDuckGo",
                }
            )

        return metadata

    def _generate_ids(
        self,
        sport: str,
        count: int,
    ):
        """
        Generate unique IDs.
        """

        return [
            f"{sport.lower()}_{index}"
            for index in range(1, count + 1)
        ]