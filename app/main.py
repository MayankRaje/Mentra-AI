from fastapi import FastAPI

from app.models import InterviewRequest
from app.models import InterviewResponse


app = FastAPI(
    title="Mentra",
    description="AI-powered technical interview preparation assistant"
)


@app.get("/")
def home():
    return {
        "message": "Mentra backend is running"
    }


@app.post("/interview-answer",response_model=InterviewResponse)

def interview_answer(request: InterviewRequest):
    temporary_answer = (
        "This is a temporary answer. "
        "LLM integration will be added next."
    )

    return InterviewResponse(
        question=request.question,
        level=request.level,
        answer=temporary_answer
    )
