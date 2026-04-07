import google.generativeai as genai
from app.config import GEMINI_API_KEY

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Use Flash model (fast + free tier friendly)
model = genai.GenerativeModel("models/gemini-2.5-flash")


def generate_response(history):
    """
    Generate response using full chat history
    """

    try:
        # Convert history into a single prompt
        conversation = ""
        for msg in history:
            role = "User" if msg["role"] == "user" else "Assistant"
            conversation += f"{role}: {msg['content']}\n"

        conversation += "Assistant:"

        response = model.generate_content(conversation)

        return response.text

    except Exception as e:
        print("ERROR:", str(e))
        return f"Error: {str(e)}"


