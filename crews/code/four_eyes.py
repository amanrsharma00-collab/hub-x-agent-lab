"""FOUR-EYES — Proposer -> Checker. Live run needs model API key."""
from crewai import Agent, Task, Crew, Process

proposer = Agent(
    role="Proposer",
    goal="State intended action in max 5 lines",
    backstory="Honest about what the agent wants to do.",
    verbose=False,
    allow_delegation=False,
)
checker = Agent(
    role="Checker",
    goal="Allow / Block / Ask Aman with 3 control bullets",
    backstory="Hard block trades, cash, production, fake strategy.",
    verbose=False,
    allow_delegation=False,
)
t1 = Task(
    description="Action: {action}. Max 5 lines.",
    expected_output="At most 5 lines.",
    agent=proposer,
)
t2 = Task(
    description="Verdict Allow/Block/Ask + exactly 3 control bullets. No execution.",
    expected_output="Verdict and 3 bullets.",
    agent=checker,
)
crew = Crew(agents=[proposer, checker], tasks=[t1, t2], process=Process.sequential, verbose=False)

if __name__ == "__main__":
    print("FOUR-EYES ready. kickoff(inputs={'action': '...'}) needs a model key.")
