from dotenv import  load_dotenv
import os
import  google.generativeai as genai
import  tweepy as x

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

# setup x credentials
x_auth = x.OAuthHandler(X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_SECRET)
x_api = x.API(x_auth)


def ai_writter(ideas:str)->str:
    # a prompt from gbt
    prompt = f"""You're an expert X (Twitter) content creator. 
    Write a tweet (max 280 characters) that is clever, engaging, and possibly viral.
    Topic: "{idea}"
    Include emojis and hashtags when helpful, but don't overuse."""
    try:
        response = ai.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Error: {e}"

EXIT_OPTIONS=['quit', 'exit','0']

if __name__ == "__main__":
    while True:
        print(f"Exit options: {EXIT_OPTIONS} \n")
        idea = input("What would idea like to write as an expert X? ")
        if idea in EXIT_OPTIONS:
            break
        else:
            if idea.strip():
                print(ai_writter(idea))