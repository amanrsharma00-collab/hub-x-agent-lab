# Operating rules (PowerVertical)

These bind **every** agent working this project — Cursor, Copilot, or later tools.

## Crews (Markdown · Cursor model · no Python key required)

| Call | Use here |
| --- | --- |
| **DESK-BRIEF** | Explain one idea (plain English, **no ETRM examples**) |
| **ROSETTA-PASS** | One jargon term → plain (no ETRM) |
| **ATLAS-PICK** | Pick agent/kit shape |
| **TOKEN-GATE** | Cheap research path |
| **OSCAR-WIRE** | Short GitHub brief |
| **FOUR-EYES** | Allow / Block / Ask before publish or delete |

Project brief phrase: **Oscar, brief me** → [[../oscar-brief]]  
Do not invent a seventh crew call name.

## LangGraph rails

Every **write** path:

1. Draft typed action + payload  
2. **WAIT** for Aman (`approved` / `revise`)  
3. Execute  
4. Report  
5. Stop — no encore loop  

Applies to: Dataverse upsert, flow create/trigger, canvas sync/compile, dataset refresh, delete.

## Money & platform (Wave 1)

- Developer Plan on **org / M365 Dev tenant** (Path A)  
- Lab CSVs + Cursor skills + **our** local Vertical Power MCP (IEA/data)  
- **Microsoft** Canvas Authoring MCP + `canvas-apps` skills for UI  
- **Microsoft** `power-automate` / FlowAgent MCP for flows  
- Prefer **not** hosted Dataverse MCP from Cursor (credit risk)  
- No premium connectors as default · no production without FOUR-EYES  
- No random 200+ community mega-MCPs  

## Security

- IEA / Microsoft secrets only in Agent Lab `.env` or OS keychain  
- Never commit secrets; never paste keys into Obsidian or chat  
- No live trading / cash / production systems  

## Portability

If you leave Cursor: read [[../handoff/portability]] first. Same rules apply.
