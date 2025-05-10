from dotenv import  load_dotenv
import os
import  google.generativeai as genai

load_dotenv()

# environment variables

# X API KEYS
X_API_KEY= os.getenv("X_API_KEY")
X_API_SECRET = os.getenv("X_API_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_SECRET = os.getenv("X_ACCESS_SECRET")

# Gemini AI KEYS
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# setup gemini AI
genai.configure(api_key=GEMINI_API_KEY)
ai = genai.GenerativeModel("gemini-2.0-flash")


def test():
    try:
        response = ai.generate_content("What is your name?")
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(test())