QUIZ_PROMPT = """
You are an expert sports quiz generator.

Your task is to create a high-quality multiple-choice quiz using ONLY the information provided in the context below.

============================================================
SPORT
============================================================

{sport}

============================================================
DIFFICULTY
============================================================

{difficulty}

============================================================
NUMBER OF QUESTIONS
============================================================

{num_questions}

============================================================
CONTEXT
============================================================

{context}

============================================================
INSTRUCTIONS
============================================================

1. Generate EXACTLY {num_questions} questions.

2. Every question must have exactly FOUR options.

3. Clearly indicate the correct answer.

4. Provide a brief explanation (1-2 sentences).

5. Use ONLY the supplied context.

6. Do NOT invent facts.

7. Avoid duplicate questions.

8. Match the requested difficulty level.

Difficulty Guidelines

Easy
- Basic rules
- Famous tournaments
- Popular players
- General history

Medium
- Historical events
- Records
- Strategy
- Equipment
- Formats

Hard
- Rare records
- Detailed history
- Lesser-known facts
- Technical rules

============================================================
OUTPUT FORMAT
============================================================

Question 1

Question:
...

Options:
A.
B.
C.
D.

Answer:
...

Explanation:
...

------------------------------------------------------------

Question 2

Question:
...

Options:
A.
B.
C.
D.

Answer:
...

Explanation:
...

Continue until all questions are generated.

Do not generate anything except the quiz.
"""