from pydantic import BaseModel


class InterviewRequest(BaseModel):
    question: str
    level: str = "SDE-2"


class InterviewResponse(BaseModel):
    question: str
    level: str
    answer: str