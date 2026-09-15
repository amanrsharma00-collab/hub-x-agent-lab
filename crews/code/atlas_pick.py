"""ATLAS-PICK — Scout -> Chooser. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

scout = Agent(
    role="Scout",
    goal="List 3 agent shapes that could fit the goal",
    backstory="Knows Crew, Lifecycle, Library-first, Coding helper, Click-ops.",
    verbose=False,
    allow_delegation=False,
)
chooser = Agent(
    role="Chooser",
    goal="Pick one shape with why and one do-not",
    backstory="Advise Aman (ETRM). No install.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Goal: {goal}. Exactly 3 options, one line each.",
    expected_output="Exactly 3 short option lines.",
    agent=scout,
)
t2 = Task(
    description="One pick + 3 why-bullets + 1 do-not. No install steps.",
    expected_output="Pick, 3 bullets, 1 do-not.",
    agent=chooser,
)
crew = Crew(agents=[scout, chooser], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("ATLAS-PICK ready. kickoff(inputs={'goal': '...'}) needs a model key.")
