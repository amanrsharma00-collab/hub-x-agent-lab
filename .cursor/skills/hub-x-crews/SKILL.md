---
name: hub-x-crews
description: Named Hub X CrewAI crews (DESK-BRIEF, ROSETTA-PASS, ATLAS-PICK, TOKEN-GATE, OSCAR-WIRE, FOUR-EYES). Use when the user says a call name or asks to run a crew from the Agent Lab call-book.
---

# Hub X crews

Audience: Aman. ETRM. Non-engineer. Low tokens.

## Call names

Read `crews/CALL-BOOK.md`. Specs in `crews/<NAME>.md`.

When the user says **Run DESK-BRIEF** / **ROSETTA-PASS** / **ATLAS-PICK** / **TOKEN-GATE** / **OSCAR-WIRE** / **FOUR-EYES**:

1. Open the matching `crews/<NAME>.md`
2. Follow roles, output counts, and stop rules exactly
3. Do not add roles or “extra research”
4. Engineering word → plain meaning on the same line
5. Never book trades, move cash, or change production

## Defaults

- Prefer Markdown crew execution in chat if no model key for live CrewAI kickoff
- Live Python: `crews/code/` sketches + Lab `.venv` (needs API key)
- Hub X vault notes stay the knowledge base; Lab holds runnable specs
