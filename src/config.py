import os

from dotenv import load_dotenv

load_dotenv()

class LLMConfig: 
    openrouter_api_ley = os.getenv("OPENROUTER_API_KEY")