from crewai import Crew
from textwrap import dedent
from agents import ResearcherAgents
from tasks import ResearcherTasks

from dotenv import load_dotenv
load_dotenv()


class ResearchCrew:
    def __init__(self, query):
        self.query = query

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = ResearcherAgents()
        tasks = ResearcherTasks()

        # Define your custom agents and tasks here
        expert_planner_agent = agents.expert_planner_agent()
        integration_agent = agents.integration_agent()
        researcher_expert = agents.researcher_expert()
        reporting_agent = agents.reporting_agent()

        # Custom tasks include agent name and variables as input
        planning_task = tasks.planning_task(
            expert_planner_agent,
            self.query,
        )

        research_task = tasks.research_task(
            researcher_expert,
            self.query,
        )

        integration_task = tasks.integration_task(
            integration_agent,
            self.query,
        )

        reporter_task = tasks.reporter_task(
            reporting_agent,
            self.query,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[expert_planner_agent,
                    integration_agent,
                    researcher_expert,
                    reporting_agent
                    ],
            tasks=[
                planning_task,
                research_task,
                integration_task,
                reporter_task
            ],
            verbose=True,
            max_rpm=1
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Planner Crew")
    print('-------------------------------')
    query = input(
        dedent("""
      What is the subject we will talk about today?
    """))

    Research_Crew = ResearchCrew(query)
    result = Research_Crew.run()
    print("\n\n########################")
    print("## Here is you Trip Plan")
    print("########################\n")
    f=open("./exportTxt.txt", "a")
    f.write(result)
    f.close
    print(result)