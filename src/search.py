from typing import Dict, List

from ddgs import DDGS

from src.config import SEARCH_RESULTS


class WebSearch:
    """
    DuckDuckGo search wrapper.
    """

    def __init__(self) -> None:
        """
        Initialize the DDGS client.
        """
        self.ddgs = DDGS()

    def search(self, sport: str) -> List[Dict[str, str]]:
        """
        Search DuckDuckGo for sports knowledge.

        Parameters
        ----------
        sport : str
            Name of the sport.

        Returns
        -------
        List[Dict[str, str]]
            Example:
            [
                {
                    "title": "...",
                    "snippet": "...",
                    "url": "..."
                }
            ]
        """

        query = (
            f"{sport} rules "
            f"{sport} history "
            f"{sport} major tournaments "
            f"{sport} facts"
        )

        try:
            results = list(
                self.ddgs.text(
                    query,
                    max_results=SEARCH_RESULTS,
                )
            )

            formatted_results: List[Dict[str, str]] = []

            for item in results:

                formatted_results.append(
                    {
                        "title": item.get("title", "").strip(),
                        "snippet": item.get("body", "").strip(),
                        "url": item.get("href", "").strip(),
                    }
                )

            return formatted_results

        except Exception as error:

            print(f"[Search Error] {error}")

            return []