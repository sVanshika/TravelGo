import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AI_MODEL_URL: str = os.getenv("AI_MODEL_URL", "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1")
    AI_API_KEY: str = os.getenv("AI_API_KEY")

settings = Settings()
