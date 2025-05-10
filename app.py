from dotenv import  load_dotenv
import os
import  google.generativeai as genai

load_dotenv()

# set up gemini AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
ai = genai.GenerativeModel("gemini-2.0-flash")


def test():
    try:
        response = ai.generate_content("What is your name?")
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"


if __name__ == "__main__":
    print(test())