"""DESK-BRIEF — Researcher -> Writer. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Researcher",
    goal="Find 3 crisp facts about the topic",
    backstory="Short bullets for a non-engineer. Plain English only. No trading examples.",
    verbose=False,
    allow_delegation=False,
)
writer = Agent(
    role="Writer",
    goal="Turn facts into 5 short bullets",
    backstory="Plain English writer. No fluff. No trading examples.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Topic: {topic}. Exactly 3 short bullets. Plain English.",
    expected_output="Exactly 3 short bullets.",
    agent=researcher,
)
t2 = Task(
    description="Rewrite into exactly 5 bullets for Aman.",
    expected_output="Exactly 5 short bullets.",
    agent=writer,
)
crew = Crew(agents=[researcher, writer], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("DESK-BRIEF ready. kickoff(inputs={'topic': '...'}) needs a model key.")
