from openai import OpenAI

from app.config import (
    OPENROUTER_API_KEY,
    OPENROUTER_MODEL
)

from app.prompt import create_interview_prompt


client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)


def generate_answer(
    question: str,
    level: str
) -> str:

    prompt = create_interview_prompt(
        question,
        level
    )

    response = client.chat.completions.create(
        model=OPENROUTER_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content