import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

def extract_json(content: str) -> dict:
    json_text = content[content.find("{"):content.rfind("}") + 1]
    return json.loads(json_text)

def get_model():
    return ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",  # You can also try "gemini-1.5-pro" if supported
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.0,
    )
