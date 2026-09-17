---
name: hub-x-crews
description: Named Hub X Markdown crews (DESK-BRIEF, ROSETTA-PASS, ATLAS-PICK, TOKEN-GATE, OSCAR-WIRE, FOUR-EYES). Default path uses Cursor's model in chat — no Python API key. Use when the user says Run + a call name.
---

# Hub X crews (Markdown go-to)

**Default:** run the crew **in this chat** with Cursor’s model.  
**Not default:** Python CrewAI `kickoff()` / extra vendor keys.

Audience: Aman. Non-engineer.

**Toolkits in Lab:** Markdown crews (go-to) · CrewAI (optional) · **LangGraph** (lifecycle / wait-for-human).  
LangGraph notes: Hub X `Connect/langgraph-start.md`. Not a seventh call name.

## Call names

DESK-BRIEF · ROSETTA-PASS · ATLAS-PICK · TOKEN-GATE · OSCAR-WIRE · FOUR-EYES

Specs (first match wins):

1. `Documents/Hub-X-Agent-Lab/crews/<NAME>.md` if Lab is on disk  
2. Else Hub X `Connect/crew-call-book.md` + Connect notes  

## How to run (seamless)

1. Parse call name (case-insensitive; allow `run desk-brief`).  
2. If **topic/term/goal/scope/action** missing → ask **one** short question, then wait.  
3. Load the matching MD. Obey role order and **exact** bullet counts.  
4. Label sections by role name (e.g. `### Researcher`).  
5. Stop when the last role finishes. No encore.  
6. Engineering word → plain meaning on the same line.  
7. **DESK-BRIEF** and **ROSETTA-PASS:** plain English only — **no ETRM / trading examples**.  
8. Never book trades, move cash, change production, or invent a new company strategy.

## Edge cases

| Case | Do this |
| --- | --- |
| Unknown call name | List the six names from the call-book. Do not invent a seventh. |
| User asks to “install / kickoff / API key” | Remind: Markdown path is go-to. Python is optional later. |
| User wants 5+ roles or a long essay | Refuse extras. Offer TOKEN-GATE or stick to the named crew. |
| User asks for browser / scrape everything | Block unless they explicitly insist; prefer Hub X notes first. |
| Overlap with Oscar Insights / Oscar Rewrite | Those phrases stay Oscar skills. Crews use **Run \<NAME\>**. |
| Live Python requested anyway | Point to `crews/code/` + `.env` key — do not paste secrets into chat. |

## Token rules (built in)

- Max **2** roles per named crew.  
- Hard output caps in each MD (3/5, 3 bullets, ≤8, etc.).  
- Hub X / call-book before any new GitHub hunt.  
- No “for completeness” second loop.
