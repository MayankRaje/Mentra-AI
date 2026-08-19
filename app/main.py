from fastapi import FastAPI

from app.models import InterviewRequest
from app.models import InterviewResponse
from app.llm_service import generate_answer

app = FastAPI(
    title="Mentra",
    description="AI-powered technical interview preparation assistant"
)

@app.get("/")
def home():
    return {
        "message": "Mentra backend is running"
    }


@app.post(
    "/interview-answer",
    response_model=InterviewResponse
)
def interview_answer(request: InterviewRequest):
    answer = generate_answer(
        request.question,
        request.level
    )

    return InterviewResponse(
        question=request.question,
        level=request.level,
        answer=answer
    )