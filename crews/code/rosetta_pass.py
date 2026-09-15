"""ROSETTA-PASS — Engineer -> Translator. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

engineer = Agent(
    role="Engineer",
    goal="Define one term accurately in max 2 sentences",
    backstory="Precise, short.",
    verbose=False,
    allow_delegation=False,
)
translator = Agent(
    role="Translator",
    goal="Three bullets: plain, ETRM picture, when Aman hears it",
    backstory="Non-engineer ETRM consultant.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Term: {term}. Max 2 sentences.",
    expected_output="One short definition.",
    agent=engineer,
)
t2 = Task(
    description="Exactly 3 bullets: plain meaning; ETRM picture; when heard.",
    expected_output="Exactly 3 short bullets.",
    agent=translator,
)
crew = Crew(agents=[engineer, translator], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("ROSETTA-PASS ready. kickoff(inputs={'term': 'API'}) needs a model key.")
