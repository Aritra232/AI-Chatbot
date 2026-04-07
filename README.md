

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



## ⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/ai-chatbot-fastapi.git

cd ai-chatbot-fastapi
2. Create .env File
GEMINI_API_KEY=your_api_key_here
3. Run with Docker (Recommended)
docker-compose up --build

API will be available at: https://aistudio.google.com

4. Run Without Docker
pip install -r requirements.txt
uvicorn app.main:app --reload

## 📡 API Endpoints
🔹 Health Check

GET /health

Response:

{
  "status": "ok"
}


🔹Chat

POST /chat

Request:

{
  "session_id": "user123",
  "message": "Hello!"
}

Response:

{
  "reply": "Hi! How can I help you?"
}

🔹 Get Chat History

GET /history/{session_id}

Response:

{
  "session_id": "user123",
  "history": [
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there!"}
  ]
}

🔹 Clear Chat History

DELETE /history/{session_id}

Response:

{
  "message": "History cleared successfully"
}

##  🧠 How It Works
1. User sends a message with a session_id
2. Message is stored in SQLite database
3. Full conversation history is retrieved
4. History is sent to Gemini API
5. AI generates response
6. Response is stored and returned

##  Additional Features
1. Rate limiting to prevent spam (2 seconds per session)
2. Proper error handling with HTTP status codes
3. Modular and clean architecture

##  🐳 Docker Commands

Build image:

docker build -t ai-chatbot .

Run container:

docker run -p 8000:8000 ai-chatbot

Using Docker Compose:

docker-compose up

##  🎯 Design Decisions
1. FastAPI for high performance APIs
2. Gemini API for fast and free LLM usage
3. SQLite for lightweight persistence
4. Pydantic for validation
5. Docker for reproducibility

##  🔐 Environment Variables
GEMINI_API_KEY=your_api_key_here


## 👨‍💻 Author
Aritra Das

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
