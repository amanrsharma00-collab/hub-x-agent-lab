"""LangGraph analytics sketch — load CSV → metrics → wait for human.

No model API key required. Uses Agent Lab sample_data.
"""
from __future__ import annotations

import csv
from pathlib import Path
from typing import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import interrupt

SAMPLE = Path(__file__).resolve().parent / "sample_data" / "orders_sample.csv"


class AnalyticsState(TypedDict):
    csv_path: str
    row_count: int
    revenue: float
    late_count: int
    open_count: int
    pack: str
    approved: bool


def load_step(state: AnalyticsState) -> dict:
    path = Path(state.get("csv_path") or SAMPLE)
    rows = list(csv.DictReader(path.open(newline="", encoding="utf-8")))
    revenue = 0.0
    late = 0
    open_n = 0
    for r in rows:
        revenue += float(r["qty"]) * float(r["unit_price"])
        if r["status"] == "Late":
            late += 1
        if r["status"] == "Open":
            open_n += 1
    return {
        "csv_path": str(path),
        "row_count": len(rows),
        "revenue": round(revenue, 2),
        "late_count": late,
        "open_count": open_n,
        "approved": False,
    }


def pack_step(state: AnalyticsState) -> dict:
    pack = (
        f"rows={state['row_count']}; revenue={state['revenue']}; "
        f"late={state['late_count']}; open={state['open_count']}"
    )
    return {"pack": pack}


def wait_step(state: AnalyticsState) -> dict:
    decision = interrupt(
        {
            "ask": "Approve this KPI pack for Power Apps / Power BI service (browser)?",
            "pack": state["pack"],
            "next_if_yes": "In browser: make.powerapps.com import CSV → gallery; app.powerbi.com one chart",
        }
    )
    return {"approved": bool(decision)}


def build_graph():
    g = StateGraph(AnalyticsState)
    g.add_node("load", load_step)
    g.add_node("pack", pack_step)
    g.add_node("wait", wait_step)
    g.add_edge(START, "load")
    g.add_edge("load", "pack")
    g.add_edge("pack", "wait")
    g.add_edge("wait", END)
    return g.compile()


if __name__ == "__main__":
    app = build_graph()
    pre = load_step({"csv_path": str(SAMPLE), "row_count": 0, "revenue": 0.0, "late_count": 0, "open_count": 0, "pack": "", "approved": False})
    pre.update(pack_step({**pre, "pack": "", "approved": False}))
    print("LangGraph analytics sketch ready.")
    print("Pack:", pre["pack"])
    print("Nodes: load → pack → wait(interrupt). Approve in chat before any Power Platform write.")
