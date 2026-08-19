from pydantic import BaseModel


class InterviewRequest(BaseModel):
    question: str
    level: str = "SDE-2"


# Structured output expected from the LLM.
class InterviewAnswer(BaseModel):
    short_answer: str
    explanation: str
    example: str
    interview_tip: str


class InterviewResponse(BaseModel):
    question: str
    level: str
    answer: InterviewAnswer