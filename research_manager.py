from agents import Runner
from search_agent import search_agent
from planner_agent import planner_agent,WebsearchItem,WebSearchPlan
from writer_agent import writer_agent,ReportData

class ResearchManager:

    async def run(self,query:str):

        yield "Your deep search is started your input query is given to the planning agent"
        yield "Now the agent accepted the input query and started the planning >>>"
        search_plan=await self.plan_searches(query)
        yield f"The planning agent completed the task .It was planned to do {len(search_plan.searches)} searches..."
        search_results=await self.perform_searches(search_plan)
        yield "Searches completed,Now writing the report..."
        report=await self.write_report(query,search_results)
        yield "Report written successfully"
        yield "This is your report"
        yield report.markdown_report

    async def plan_searches(self,query:str)->WebSearchPlan:
        """Plan the searches to perform the query"""
        result=await Runner.run(planner_agent,f"Query:{query}")
        return result.final_output
    async def perform_searches(self,search_plan:WebSearchPlan)->list[str]:
        """Perform the searches to perform for the query"""
        tasks=[self.search(item) for item in search_plan.searches]
        return await asyncio.gather(*tasks)
    async def search(self,item:WebsearchItem)->str | None:
        """Perform a search for the query"""
        input_message=f"search term:{item.query}\n reason for searching :{item.reason}"
        result=await Runner.run(search_agent,input_message)
        return result.final_output
    async def write_report(self,query:str,search_results:list[str])->ReportData:
        """Write the report for the query """
        input_message=f"Original query:{query}\n Summarized search results:{search_results}"
        result=await Runner.run(writer_agent,input_message)
        return result.final_output
    