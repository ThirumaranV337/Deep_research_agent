from pydantic import BaseModel,Field
from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel
import os
from dotenv import load_dotenv
load_dotenv(override=True)

model_name="openai/gpt-oss-120b"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROQ_API=os.getenv("GROQ_API")

how_many_search=5

instructions=f"""
you are the reserch assistant.Give a user qury,come up with a set of web searches
to perform to best answer the query.Output{how_many_search} terms to query for.
"""

"""creating the model instance by using the open Ai client library """
groq_client=AsyncOpenAI(bse_url=GROQ_BASE_URL,api_key=GROQ_API)

gpt_model=OpenAIChatCompletionsModel(model=model_name,openai_client=groq_client)





class WebsearchItem(BaseModel):
    reason:str=Field(description="You reasoning for why this search is important to the query.")
    query:str=Field(description="The search term is used for the web search .")
class WebSearchPlan(BaseModel):
    searches:list[WebsearchItem]=Field(description="A list of web searches to perform to best answer the query.")
planner_agent=Agent(name="Planner Agent",instructions=instructions,model=gpt_model,output_type=WebSearchPlan)

