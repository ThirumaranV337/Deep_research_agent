from agents import Agent,WebsearchTool,ModelSettings,AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os 

load_dotenv(override=True)

model_name="openai/gpt-oss-120b"

GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROQ_API=os.getenv("GROQ_API")

instructions="""
You are a research assistant. Given a search term,your search the web for that term and 
produce a concise summary of the result.The summary must 2-3 paragraphs and less then 300 words.
capture the main points and be succinct.reply only with the sumary.
"""

"""creating the model instance by using the open Ai client library """
groq_client=AsyncOpenAI(bse_url=GROQ_BASE_URL,api_key=GROQ_API)

gpt_model=OpenAIChatCompletionsModel(model=model_name,openai_client=groq_client)

settings=ModelSettings(tool_choice="required")
tools=[WebsearchTool()]

search_agent=Agent(name="Search Agent",instructions=instructions,tools=tools,model=model_name,model_settings=settings)