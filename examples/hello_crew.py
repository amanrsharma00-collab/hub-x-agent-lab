"""CrewAI sketch: Researcher -> Writer. Needs an LLM key for a live run."""
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Researcher",
    goal="Find 3 crisp facts about the topic",
    backstory="Short bullets for a non-engineer.",
    verbose=False,
    allow_delegation=False,
)
writer = Agent(
    role="Writer",
    goal="Turn facts into 5 short bullets",
    backstory="ETRM consultant. No fluff.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Topic: {topic}. List 3 facts in plain English.",
    expected_output="Exactly 3 short bullets.",
    agent=researcher,
)
t2 = Task(
    description="Rewrite into 5 bullets a non-engineer can use.",
    expected_output="Exactly 5 short bullets.",
    agent=writer,
)
crew = Crew(
    agents=[researcher, writer],
    tasks=[t1, t2],
    process=Process.sequential,
    verbose=False,
)

if __name__ == "__main__":
    print("Crew ready: Researcher -> Writer")
    print("Live run needs a model API key. In Cursor, open this lab and ask the agent to adapt this file.")
