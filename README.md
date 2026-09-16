# Hub X Agent Lab

**Obsidian Hub X** = notes. **This folder** = named crews + toolkits.

## Go-to: Markdown crews (Cursor’s model)

| Call | Job |
| --- | --- |
| **DESK-BRIEF** | Explain a topic (3→5 bullets; no ETRM examples) |
| **ROSETTA-PASS** | Jargon → plain + ETRM |
| **ATLAS-PICK** | Which agent shape / kit |
| **TOKEN-GATE** | Cheap research path |
| **OSCAR-WIRE** | Short GitHub brief |
| **FOUR-EYES** | Human-approval gate |

Say: `Run DESK-BRIEF on topic: what is an agent`  
Index: [`crews/CALL-BOOK.md`](crews/CALL-BOOK.md)

## Toolkits installed

| Kit | Use when |
| --- | --- |
| Markdown crews | Daily explain / pick / gate work |
| CrewAI | Optional Python role crews |
| **LangGraph** | Step → wait for human → continue |

Sketches: [`toolkits/langgraph_wait.py`](toolkits/langgraph_wait.py) · [`toolkits/langgraph_analytics.py`](toolkits/langgraph_analytics.py)
Sample data: [`toolkits/sample_data/`](toolkits/sample_data/) (free Power Platform tests)
Skill: `power-platform-analytics`  
Hub X note: `Connect/langgraph-start.md`

## Layout

```
crews/           MD specs + CALL-BOOK
crews/code/      Optional CrewAI Python
toolkits/        LangGraph (+ future kits)
.cursor/skills/  hub-x-crews
```

## Optional Python

`.venv` has CrewAI + LangGraph. LLM live runs need a vendor key — not required for daily Markdown crews or the LangGraph structure sketch.

## GitHub

https://github.com/amanrsharma00-collab/hub-x-agent-lab
