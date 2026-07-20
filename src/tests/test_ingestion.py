from src.database import ChromaDatabase
from src.ingestion import KnowledgeIngestion


def main():

    database = ChromaDatabase()

    ingestion = KnowledgeIngestion(database)

    success = ingestion.ingest_sport("Football")

    print()

    print("Success :", success)
    print("Documents :", database.document_count())


if __name__ == "__main__":
    main()