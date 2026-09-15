"""OSCAR-WIRE — Finder -> Briefer. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

finder = Agent(
    role="Finder",
    goal="Up to 4 repo hits with one-line why",
    backstory="Prefer Governor starred kits. Learning-friendly only.",
    verbose=False,
    allow_delegation=False,
)
briefer = Agent(
    role="Briefer",
    goal="Max 8 bullets for Aman; translate jargon once",
    backstory="Oscar Insights style. No fluff.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Scope: {scope}. Up to 4 hits, one line each.",
    expected_output="Up to 4 short lines.",
    agent=finder,
)
t2 = Task(
    description="Max 8 bullets. Who it helps. No AGI demos.",
    expected_output="At most 8 short bullets.",
    agent=briefer,
)
crew = Crew(agents=[finder, briefer], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("OSCAR-WIRE ready. kickoff(inputs={'scope': '...'}) needs a model key.")
