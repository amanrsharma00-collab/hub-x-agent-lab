---
name: power-platform-agentic
description: Mac browser-only agentic workflow that chains Power Platform analytics skills with LangGraph wait-for-human pauses and numbered web click handoffs (make.powerapps.com, Automate, Power BI service). Use when Aman wants seamless Power Platform integration, browser-only Mac work, or Run Power Platform agentic.
---

# Power Platform agentic (Mac · web)

Audience: Aman. Plain English.

## Constraint

**Mac + web browser only.** Never require Power BI Desktop or Windows apps.  
Sites: make.powerapps.com · make.powerautomate.com · app.powerbi.com · admin.powerplatform.microsoft.com  
Free lane: Power Apps Developer Plan (dev/test).

## When to use

User wants **agentic integration** of skills into a seamless Power Platform workflow, or says:

> Run Power Platform agentic on sample: …

Also read Hub X `Connect/power-platform-agentic-web.md` + `Connect/langgraph-start.md`.

## Orchestration order

Run **one** stage, then pause:

1. PROFILE → wait  
2. KPI-PACK → wait  
3. EXCEPTION → wait  
4. APP-SCHEMA → wait  
5. BROWSER-HANDOFF (≤8 click steps) → wait for `done step N` / `approved`  
6. Stop  

Use skill **power-platform-analytics** for stages 1–4.  
If sample file missing, default `toolkits/sample_data/orders_sample.csv` in Agent Lab.

## Who clicks

- **Cursor:** packs, schemas, click checklists, FOUR-EYES wording if asked.  
- **Aman in browser:** import, build, publish.  
- **No MCP** to Microsoft unless Aman explicitly approves later.

## Seamless helpers (optional, same chat)

- TOKEN-GATE — before wide research  
- FOUR-EYES — before publish  
- DESK-BRIEF — definitions only (no ETRM examples)

## Must not

- Desktop BI / Windows steps  
- Production writes  
- Skip interrupt  
- Auto-browse Microsoft to “finish” the app  
- Book trades / move money / change live systems
