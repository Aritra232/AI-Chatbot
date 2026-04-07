# 🚀 AI Chatbot API (FastAPI + Gemini + Docker)

A ChatGPT-style conversational AI backend built with FastAPI, powered by Google Gemini API, and fully containerized using Docker.

---

## 📌 Features

- Multi-turn conversation with context awareness  
- Session-based memory (isolated per user)  
- Gemini LLM integration  
- RESTful API design  
- SQLite database for persistent storage  
- Basic rate limiting (2 seconds per session)  
- Docker & Docker Compose support  

---

## 🏗️ Project Structure

```bash
app/
│── main.py
│
├── routes/
│   └── chat.py
│
├── services/
│   ├── ai.py
│   ├── memory.py
│   ├── db.py
│   └── models.py
│
├── models/
│   └── schemas.py
│
└── config.py

Dockerfile
docker-compose.yml
.env.example
README.md
