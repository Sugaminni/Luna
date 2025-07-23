from dotenv import load_dotenv
import os
from openai import OpenAI
from pathlib import Path

# Gets the gpt API key from .env file locally
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")

# Confirms that Luna is online and ready
client = OpenAI(api_key=api_key)
print("Luna here, reporting for duty!")
