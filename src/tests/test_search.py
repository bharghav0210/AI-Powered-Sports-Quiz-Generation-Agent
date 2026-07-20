from src.search import WebSearch


def main():

    search = WebSearch()

    results = search.search("Cricket")

    print(f"\nFound {len(results)} results\n")

    for index, result in enumerate(results, start=1):

        print("=" * 80)
        print(f"Result {index}")
        print("=" * 80)
        print(f"Title   : {result['title']}")
        print(f"URL     : {result['url']}")
        print(f"Snippet : {result['snippet']}")
        print()


if __name__ == "__main__":
    main()