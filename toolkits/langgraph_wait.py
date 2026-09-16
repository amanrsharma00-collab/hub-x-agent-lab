"""LangGraph toolkit sketch — wait-for-human pattern.

No model API key needed for this structure demo.
Live LLM nodes later = optional vendor key (not daily path).
"""
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt


class JobState(TypedDict):
    topic: str
    draft: str
    approved: bool


def draft_step(state: JobState) -> dict:
    return {"draft": f"Draft for: {state['topic']}", "approved": False}


def wait_step(state: JobState) -> dict:
    # Pauses here until a human resumes with a decision.
    decision = interrupt({"ask": "Approve this draft?", "draft": state["draft"]})
    return {"approved": bool(decision)}


def finish_step(state: JobState) -> dict:
    return state


def build_graph():
    g = StateGraph(JobState)
    g.add_node("draft", draft_step)
    g.add_node("wait", wait_step)
    g.add_node("finish", finish_step)
    g.add_edge(START, "draft")
    g.add_edge("draft", "wait")
    g.add_edge("wait", "finish")
    g.add_edge("finish", END)
    return g.compile()


if __name__ == "__main__":
    app = build_graph()
    print("LangGraph wait-for-human sketch ready.")
    print("Nodes: draft → wait (interrupt) → finish")
    print("Compile OK. Resume/interrupt needs a checkpointer for real runs.")
