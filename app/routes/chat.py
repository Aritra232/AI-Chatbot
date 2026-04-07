from fastapi import APIRouter, HTTPException
from app.models.schemas import (
    ChatRequest,
    ChatResponse,
    HistoryResponse,
    HealthResponse,
)
from app.services.memory import get_history, add_message, clear_history
from app.services.ai import generate_response
import logging
from time import time

request_log = {}

logging.basicConfig(level=logging.INFO)



router = APIRouter()


# 🔹 Health Check
@router.get("/health", response_model=HealthResponse)
def health_check():
    return {"status": "ok"}

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        session_id = request.session_id
        user_message = request.message

        current_time = time()

        if session_id in request_log:
            if current_time - request_log[session_id] < 2:
                raise HTTPException(
                    status_code=429,
                    detail="Too many requests. Please wait a moment."
                )

        request_log[session_id] = current_time

        # Save user message
        add_message(session_id, "user", user_message)

        # Get history
        history = get_history(session_id)

        # Generate AI response
        ai_reply = generate_response(history)

        # Save AI reply
        add_message(session_id, "assistant", ai_reply)

        # Logging
        logging.info(f"Session: {session_id} | Message: {user_message} | Reply: {ai_reply}")

        return {"reply": ai_reply}

    except HTTPException as e:
        # keep original HTTP errors (like 429)
        raise e

    except Exception as e:
        logging.error(f"Error in /chat: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
    

# 🔹 Get History
@router.get("/history/{session_id}", response_model=HistoryResponse)
def get_chat_history(session_id: str):
    history = get_history(session_id)

    if not history:
        raise HTTPException(status_code=404, detail="Session not found")

    return {
        "session_id": session_id,
        "history": history
    }


# 🔹 Clear History
@router.delete("/history/{session_id}")
def delete_chat_history(session_id: str):
    clear_history(session_id)

    return {"message": "History cleared successfully"}