from app.services.db import SessionLocal
from app.services.models import Message


def get_history(session_id: str, limit: int = 10):
    db = SessionLocal()
    messages = (
        db.query(Message)
        .filter(Message.session_id == session_id)
        .order_by(Message.id.desc())
        .limit(limit)
        .all()
    )
    db.close()

    messages.reverse()

    return [{"role": m.role, "content": m.content} for m in messages]


def add_message(session_id: str, role: str, content: str):
    db = SessionLocal()

    msg = Message(
        session_id=session_id,
        role=role,
        content=content
    )

    db.add(msg)
    db.commit()
    db.close()


def clear_history(session_id: str):
    db = SessionLocal()
    db.query(Message).filter(Message.session_id == session_id).delete()
    db.commit()
    db.close()