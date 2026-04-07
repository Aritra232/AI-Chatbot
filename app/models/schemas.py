from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    session_id: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)


class ChatResponse(BaseModel):
    reply: str


class Message(BaseModel):
    role: str   # "user" or "assistant"
    content: str


class HistoryResponse(BaseModel):
    session_id: str
    history: list[Message]


class HealthResponse(BaseModel):
    status: str