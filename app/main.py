
from fastapi import FastAPI
from app.routes.chat import router as chat_router
from app.services.db import engine
from app.services.models import Base

app = FastAPI()

app.include_router(chat_router)

Base.metadata.create_all(bind=engine)