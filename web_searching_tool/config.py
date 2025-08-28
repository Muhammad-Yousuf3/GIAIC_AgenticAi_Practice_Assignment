import os
from dotenv import load_dotenv
from tavily import TavilyClient
from agents import OpenAIChatCompletionsModel
from openai import AsyncOpenAI

load_dotenv(override=True)

GEMINI_API_KEY=os.getenv("GEMINI_API_KEY")
GEMINI_BASE_URL=os.getenv("GEMINI_BASE_URL")
GEMINI_MODEL_NAME=os.getenv("GEMINI_MODEL_NAME")

client=AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=GEMINI_BASE_URL)

model=OpenAIChatCompletionsModel(openai_client=client,model=GEMINI_MODEL_NAME)

#TAVILY CONFIG
TAVILY_API_KEY=os.getenv("TAVILY_API_KEY")
tavily_client=TavilyClient(api_key=TAVILY_API_KEY)