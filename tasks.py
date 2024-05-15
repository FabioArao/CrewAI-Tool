from crewai import Task
from textwrap import dedent

"""
Creating Tasks Cheat Sheet:
- Begin with the end in mind. Identify the specific outcome your tasks are aiming to achieve.
- Break down the outcome into actionable tasks, assigning each task to the appropriate agent.
- Ensure tasks are descriptive, providing clear instructions and expected deliverables.

Goal:
- Develop a detailed itinerary, including city selection, attractions, and practical travel advice.

Key Steps for Task Creation:
1. Identify the Desired Outcome: Define what success looks like for your project.
    - A detailed 7 day travel itenerary.

2. Task Breakdown: Divide the goal into smaller, manageable tasks that agents can execute.
    - Itenerary Planning: develop a detailed plan for each day of the trip.
    - City Selection: Analayze and pick the best cities to visit.
    - Local Tour Guide: Find a local expert to provide insights and recommendations.

3. Assign Tasks to Agents: Match tasks with agents based on their roles and expertise.

4. Task Description Template:
  - Use this template as a guide to define each task in your CrewAI application. 
  - This template helps ensure that each task is clearly defined, actionable, and aligned with the specific goals of your project.

  Template:
  ---------
  def [task_name](self, agent, [parameters]):
      return Task(description=dedent(f'''
      **Task**: [Provide a concise name or summary of the task.]
      **Description**: [Detailed description of what the agent is expected to do, including actionable steps and expected outcomes. This should be clear and direct, outlining the specific actions required to complete the task.]

      **Parameters**: 
      - [Parameter 1]: [Description]
      - [Parameter 2]: [Description]
      ... [Add more parameters as needed.]

      **Note**: [Optional section for incentives or encouragement for high-quality work. This can include tips, additional context, or motivations to encourage agents to deliver their best work.]

      '''), agent=agent)

"""


class ResearcherTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def planning_task(self, agent, query):
        return Task(
            description=dedent(
                f"""
            **Task**: Plan
            **Description**: As the Planner, your primary task is to deconstruct the user's complex, multi-hop question into a network of simpler, interconnected questions.\n
            This involves identifying the key components and relationships within the question.\n
            You must determine if the question involves linear, branching, or converging paths and plan accordingly.\n
            For each identified sub-question, you should outline a logical sequence or network that progressively builds towards answering the overarching query.\n
            This structured approach facilitates a comprehensive investigation by guiding subsequent agents through a clear, methodical process.\n
            Be prepared to receive feedback from the Integration Agent on missing information or clarity needed and adjust the investigation accordingly.\n
            Here's an example of how you might break down a question: Who succeeded the first President of Namibia?\n
            1. Who was the first President of Namibia?\n
            2. Who succeeded Sam Nujoma?\n
            here's the query: {query}

            **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""A detailed view of the sub-questions and their relationships to the main question and how to proceed with the investigation to answer the main question """
            ),
            agent=agent,
        )

    def research_task(self, agent, query):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Research task
                    **Description**: As the researcher, your responsibility is to conduct targeted searches for information based on the structured path provided by the Planner Agent.\n
                    You should tackle each sub-question individually, using available resources to gather relevant, specific information.\n
                    Adapt your search strategy based on the type of sub-question be it factual, conceptual, or contextual and incorporate knowledge from previous searches to inform subsequent ones.\n
                    Your goal is to systematically assemble the pieces of information required to construct the context needed for addressing the original, complex multi-hop question.\n
                    If you encounter challenges in finding the required information, note down what is missing or unclear for feedback to the Planner Agent.\n
                    here's the query: {query}

                    **Note**: {self.__tip_section()}
        """
            ),
            expected_output=dedent(
                f"""Specific information and sources relevant to the sub-questions identified by the Planner Agent"""),
            agent=agent,
        )

    def integration_task(self, agent, query):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Integration task
                    **Description**: As the Integration Agent, synthesize the answers obtained for each sub-question into a coherent, comprehensive response that addresses the user's original, multi-hop question.\n
                    If you identify information gaps or need further clarification, provide specific feedback to the Planner Agent.\n
                    This feedback is crucial for refining the investigation and ensuring the final response is as comprehensive and accurate as possible.\n
                    Ensure you include the sources of information in your integrated response to maintain transparency and credibility.\n
                    here's the query: {query}

                    **Note**: {self.__tip_section()}
        """
            ),
             expected_output=dedent(
                f"""All the information gathered from the researcher agent organised and integrated with website links and references."""),
            agent=agent,
        )

    def reporter_task(self, agent, query):
        return Task(
            description=dedent(
                f"""
                    **Task**:  Reporter task
                    **Description**: As the Reporter Agent, your role is to deliver the final, integrated response to the user, ensuring it accurately and comprehensively addresses the multi-hop question.\n
                    Review the synthesized answer for clarity, accuracy, and completeness, incorporating citations for all referenced information.\n
                    Present the findings in a clear, concise, and informative manner, providing citations and links to sources.\n
                    Your presentation should reflect the structured investigation and synthesis process, offering a complete answer and facilitating further exploration by the user if desired.\n
                    If the Integration Agent has identified that the question cannot be fully answered with the available information, communicate this transparently to the user along with any potential next steps or recommendations for further inquiry.\n
                    here's the query: {query}
                    **Note**: {self.__tip_section()}
        """
            ),
             expected_output=dedent(
                f"""AA clear, accurate, and concise response to the user, with references and website links to sources of information"""),
            agent=agent,
        )  
