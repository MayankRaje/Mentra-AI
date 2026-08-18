def create_interview_prompt(
    question: str,
    level: str
) -> str:

    return f"""
You are a technical interview preparation assistant.

Candidate level:
{level}

Question:
{question}

Answer in this structure:

1. Short Answer
2. Explanation
3. Simple Example
4. Interview Tip

Keep the answer practical and easy to understand.
"""