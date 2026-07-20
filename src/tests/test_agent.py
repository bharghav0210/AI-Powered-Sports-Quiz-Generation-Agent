
from pprint import pprint

from src.agent import QuizAgent


def main() -> None:
    """Run a simple end-to-end quiz generation test."""

    print("=" * 80)
    print("SPORTS QUIZ AGENT TEST")
    print("=" * 80)

    agent = QuizAgent()

    sport = "Cricket"
    difficulty = "Easy"
    num_questions = 5

    print(f"Sport           : {sport}")
    print(f"Difficulty      : {difficulty}")
    print(f"No. of Questions: {num_questions}")
    print("-" * 80)

    result = agent.generate_quiz(
        sport=sport,
        difficulty=difficulty,
        num_questions=num_questions,
    )

    # ------------------------------------------------------------------
    # Failure
    # ------------------------------------------------------------------
    if not result.get("success", False):

        print("\n❌ Quiz generation failed\n")

        print("Error:")
        print(result.get("error", "Unknown error"))

        print("\nFull Response:")
        pprint(result)

        return

    # ------------------------------------------------------------------
    # Success
    # ------------------------------------------------------------------
    print("\n✅ Quiz generated successfully!\n")

    print(f"Sport       : {result.get('sport')}")
    print(f"Difficulty  : {result.get('difficulty')}")
    print(f"Questions   : {result.get('num_questions')}")

    print("\n" + "=" * 80)
    print("GENERATED QUIZ")
    print("=" * 80)

    print(result.get("quiz", "No quiz returned."))

    print("\n" + "=" * 80)
    print("TEST COMPLETED")
    print("=" * 80)


if __name__ == "__main__":
    main()