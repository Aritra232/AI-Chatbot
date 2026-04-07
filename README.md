🚀 AI Chatbot API (FastAPI + Gemini + Docker)

A ChatGPT-style conversational AI backend built with FastAPI, powered by Google Gemini API, and fully containerized using Docker.

📌 Features
Multi-turn conversation with context awareness
Session-based memory (isolated per user)
Gemini LLM integration
RESTful API design
SQLite database for persistent storage
Basic rate limiting (2 seconds per session)
Docker & Docker Compose support

🏗️ Project Structure
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
README.



⚙️ Setup Instructions
1. Clone Repository
git clone https://github.com/your-username/ai-chatbot-fastapi.git
cd ai-chatbot-fastapi
2. Create .env File
GEMINI_API_KEY=your_api_key_here
3. Run with Docker (Recommended)
docker-compose up --build

API will be available at: https://aistudio.google.com


http://localhost:8000
4. Run Without Docker
pip install -r requirements.txt
uvicorn app.main:app --reload
📡 API Endpoints
🔹 Health Check

GET /health

Response:

{
  "status": "ok"
}
🔹 Chat

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


🧠 How It Works
User sends a message with a session_id
Message is stored in SQLite database
Full conversation history is retrieved
History is sent to Gemini API
AI generates response
Response is stored and returned

🛡️ Additional Features
Rate limiting to prevent spam (2 seconds per session)
Proper error handling with HTTP status codes
Modular and clean architecture

🐳 Docker Commands

Build image:

docker build -t ai-chatbot .

Run container:

docker run -p 8000:8000 ai-chatbot

Using Docker Compose:

docker-compose up
🎯 Design Decisions

FastAPI for high performance APIs
Gemini API for fast and free LLM usage
SQLite for lightweight persistence
SQLAlchemy ORM for scalability
Pydantic for validation
Docker for reproducibility


🔐 Environment Variables
GEMINI_API_KEY=your_api_key_here

🚀 Future Improvements
Streaming responses (SSE/WebSockets)
Redis for faster memory
Authentication (JWT)
Unit testing (pytest)
Frontend UI


👨‍💻 Author
Aritra Das