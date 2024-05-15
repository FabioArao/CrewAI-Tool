import os
from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
#from crewai_tools import ScrapeWebsiteTool

from tools.search_tools import SearchTools
from tools.calculator_tools import CalculatorTools

#WebsiteTool = ScrapeWebsiteTool()

"""
Creating Agents Cheat Sheet:
- Think like a boss. Work backwards from the goal and think which employee 
    you need to hire to get the job done.
- Define the Captain of the crew who orient the other agents towards the goal. 
- Define which experts the captain needs to communicate with and delegate tasks to.
    Build a top down structure of the crew.

Goal:
- Create a 7-day travel itinerary with detailed per-day plans,
    including budget, packing suggestions, and safety tips.

Captain/Manager/Boss:
- Expert Travel Agent

Employees/Experts to hire:
- City Selection Expert 
- Local Tour Guide


Notes:
- Agents should be results driven and have a clear goal in mind
- Role is their job title
- Goals should actionable
- Backstory should be their resume
"""


#class ResearcherAgents:
#    def __init__(self):
#        self.llm = ChatGroq(
#            api_key=os.getenv("yourAPIKey"),
#            model="llama3-70b-8192"
#        )

class ResearcherAgents:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="llama3:8b-instruct-q8_0",
            base_url="http://localhost:11434/v1",
            api_key="NA"
        )

    def expert_planner_agent(self):
        return Agent(
            role="Expert Planner Agent",
            backstory=dedent(
                f"""Expert in deconstructing complex, multi-hop questions into a network of simpler, interconnected queries."""),
            goal=dedent(f"""
                        Streamline complex inquiries into organized, manageable components.
                        """),
            tools=[
                #SearchTools.search_internet,
                
            ],
            verbose=True,
            llm=self.internalllm,
            cache=True,
            allow_delegation=True,
        )


    def integration_agent(self):
        return Agent(
            role="Integration",
            backstory=dedent(
                f"""Skilled in synthesizing answers obtained for each sub-question into a coherent, comprehensive response that addresses the"""),
            goal=dedent(f"""
                        Communicate insights clearly, ensuring depth and accuracy for further exploration.
                        """),
            tools=[
                #SearchTools.search_internet,
            ],
            verbose=True,
            llm=self.llm,
            cache=True,
            allow_delegation=True,
        )

    def researcher_expert(self):
        return Agent(
            role="Researcher Expert",
            backstory=dedent(
                f"""Specialist in conducting targeted searches for information based on structured paths provided by the Planner Agent."""),
            goal=dedent(
                f"""Identify and retrieve essential data for sophisticated inquiries"""),
            tools=[SearchTools.search_internet,],
            verbose=True,
            llm=self.llm,
        )

    def reporting_agent(self):
        return Agent(
            role="Reporter",
            backstory=dedent(f"""Knowledgeable local guide with extensive information
        about the city, it's attractions and customs"""),
            goal=dedent(
                f"""Skilled in delivering final, integrated responses to users, ensuring accuracy, clarity, and completeness."""),
#            tools=[SearchTools.search_internet,],
            verbose=True,
            llm=self.internalllm,
        )
