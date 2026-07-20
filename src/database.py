from typing import Any, Dict, List

import chromadb
from chromadb.api.models.Collection import Collection
from chromadb.utils.embedding_functions import (
    SentenceTransformerEmbeddingFunction,
)

from src.config import (
    CHROMA_DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
)


class ChromaDatabase:
    """
    Wrapper around ChromaDB operations.

    Responsibilities
    ----------------
    - Create/Open persistent database
    - Store documents
    - Retrieve documents
    - Check whether knowledge already exists
    - Collection statistics
    """

    def __init__(self) -> None:
        """
        Initialize the persistent ChromaDB client.
        """

        self.client = chromadb.PersistentClient(
            path=str(CHROMA_DB_PATH)
        )

        self.embedding_function = (
            SentenceTransformerEmbeddingFunction(
                model_name=EMBEDDING_MODEL
            )
        )

        self.collection: Collection = (
            self.client.get_or_create_collection(
                name=COLLECTION_NAME,
                embedding_function=self.embedding_function,
            )
        )

    # =========================================================
    # Add Documents
    # =========================================================

    def add_documents(
        self,
        documents: List[str],
        metadatas: List[Dict[str, Any]],
        ids: List[str],
    ) -> None:
        """
        Store documents inside ChromaDB.
        """

        if not documents:
            return

        self.collection.add(
            documents=documents,
            metadatas=metadatas,
            ids=ids,
        )

    # =========================================================
    # Check Existing Sport
    # =========================================================

    def sport_exists(
        self,
        sport: str,
    ) -> bool:
        """
        Returns True if knowledge for a sport
        already exists.
        """

        results = self.collection.get(
            where={
                "sport": sport
            }
        )

        return len(results["ids"]) > 0

    # =========================================================
    # Retrieve Documents
    # =========================================================

    def retrieve_documents(
        self,
        sport: str,
        query: str,
        top_k: int = 5,
    ) -> List[str]:
        """
        Perform semantic search.

        Returns
        -------
        List[str]
            Relevant document texts.
        """

        results = self.collection.query(
            query_texts=[query],
            n_results=top_k,
            where={
                "sport": sport
            },
        )

        documents = results.get(
            "documents",
            []
        )

        if not documents:
            return []

        return documents[0]

    # =========================================================
    # Document Count
    # =========================================================

    def document_count(self) -> int:
        """
        Return total stored documents.
        """

        return self.collection.count()

    # =========================================================
    # Clear Database
    # =========================================================

    def clear_collection(self) -> None:
        """
        Delete every document.
        """

        data = self.collection.get()

        ids = data.get(
            "ids",
            []
        )

        if ids:
            self.collection.delete(ids=ids)

    # =========================================================
    # Collection Information
    # =========================================================

    def collection_info(self) -> Dict[str, Any]:
        """
        Return collection statistics.
        """

        return {
            "collection_name": COLLECTION_NAME,
            "embedding_model": EMBEDDING_MODEL,
            "database_path": str(CHROMA_DB_PATH),
            "documents": self.document_count(),
        }

    # =========================================================
    # Display Information
    # =========================================================

    def print_info(self) -> None:
        """
        Print database information.
        """

        info = self.collection_info()

        print("\n========== ChromaDB ==========")

        for key, value in info.items():
            print(f"{key:<20}: {value}")

        print("==============================\n")