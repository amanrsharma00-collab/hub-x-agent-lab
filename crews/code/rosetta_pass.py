"""ROSETTA-PASS — Engineer -> Translator. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

engineer = Agent(
    role="Engineer",
    goal="One accurate definition, max two sentences",
    backstory="Precise. No essay.",
    verbose=False,
    allow_delegation=False,
)
translator = Agent(
    role="Translator",
    goal="Three bullets: plain meaning, everyday picture, when Aman hears it",
    backstory="Plain English for a non-engineer. No trading examples.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Term: {term}. One accurate definition, max two sentences.",
    expected_output="One short definition.",
    agent=engineer,
)
t2 = Task(
    description="Exactly 3 bullets: plain meaning; everyday picture; when heard. No ETRM/trading examples.",
    expected_output="Exactly 3 short bullets.",
    agent=translator,
)
crew = Crew(agents=[engineer, translator], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("ROSETTA-PASS ready. kickoff(inputs={'term': 'API'}) needs a model key.")
