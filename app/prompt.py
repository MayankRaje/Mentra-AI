def create_interview_prompt(question: str, level: str) -> str:
    return f"""
You are an experienced technical interviewer.

Candidate level:{level}

Question:{question}

Return ONLY valid JSON in this exact format:

{{
  "short_answer": "...",
  "explanation": "...",
  "example": "...",
  "interview_tip": "..."
}}

Guidelines:
- Keep the answer appropriate for the candidate level.
- Keep it practical and easy to understand.
- Do not add any text outside the JSON.
"""