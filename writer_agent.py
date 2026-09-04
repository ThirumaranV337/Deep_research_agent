from pydantic import BaseModel,Field
from agents import Agent,AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
load_dotenv(override=True)


model_name="openai/gpt-oss-120b"

GROQ_BASE_URL = "https://api.groq.com/openai/v1"
GROQ_API=os.getenv("GROQ_API")

instructions="""You are the senior researcher tasked with writing a cohesive report for a research query.
You will be provided with the original query,and some research.
Generate a comprehensive report based on the research and the query.
The final output should be in the markdown format with the professional look and it should be lengthy and detailed.Aim 
for 5-10 pages of content,at least 1000 words.
"""

groq_client=AsyncOpenAI(bse_url=GROQ_BASE_URL,api_key=GROQ_API)

gpt_model=OpenAIChatCompletionsModel(model=model_name,openai_client=groq_client)


class ReportData(BaseModel):
    short_summary:str=Field(description="A short 2-3 sentence summary of the findinngs.")
    markdown_report:str=Field(description="The final report")
    follow_up_questions: list[str]=Field(description="Suggested topic to research further")
writer_agent=Agent(name="writer Agent",instructions=instructions,model=gpt_model)
