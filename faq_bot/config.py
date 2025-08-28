import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

# Load environment variables from .env file
load_dotenv(override=True)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL = os.getenv("GEMINI_BASE_URL")
GEMINI_MODEL_NAME = os.getenv("GEMINI_MODEL_NAME")

# Initialize the OpenAI model with the Gemini API key and base URL
client=AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)

model=OpenAIChatCompletionsModel(openai_client=client, model=GEMINI_MODEL_NAME)