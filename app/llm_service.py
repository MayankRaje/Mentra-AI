import json
from openai import OpenAI
from app.config import (OPENROUTER_API_KEY,OPENROUTER_MODEL)
from app.prompt import create_interview_prompt
from app.models import InterviewAnswer


# OpenAI-compatible client configured to route requests through OpenRouter.
client = OpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

#return result in form of InterviewAnswer
def generate_answer(question: str, level: str) -> InterviewAnswer:
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

    content = response.choices[0].message.content

    # Convert the LLM's JSON text into a Python dictionary.
    data = json.loads(content)

    # Validate and map the LLM output to our expected response structure.
    return InterviewAnswer(**data)