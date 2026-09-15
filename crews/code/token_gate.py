"""TOKEN-GATE — Planner -> Trimmer. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

planner = Agent(
    role="Planner",
    goal="Draft at most 5 steps for the request",
    backstory="Short plans only.",
    verbose=False,
    allow_delegation=False,
)
trimmer = Agent(
    role="Trimmer",
    goal="Keep only Hub X notes → one README → one search",
    backstory="Token budget enforcer for Aman.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Request: {plan}. Max 5 short steps.",
    expected_output="At most 5 lines.",
    agent=planner,
)
t2 = Task(
    description="Reorder to cheap path. Drop browser/mega-crew/completeness.",
    expected_output="Ordered cheap path + drops.",
    agent=trimmer,
)
crew = Crew(agents=[planner, trimmer], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("TOKEN-GATE ready. kickoff(inputs={'plan': '...'}) needs a model key.")
