# 01 — Scope (in / out / waves)

## In scope (Wave 1)

### Wave 1A (can start without Power Automate)

| Pillar | What MCP + skills may do |
| --- | --- |
| **Power Apps / Dataverse** | Tables, rows, Energy Indicator — **needs org/Developer account** |
| **IEA + Lab CSV** | Fetch/map/profile; upsert via MCP direct API (not Flow) |
| **Cursor skills** | PROFILE, KPI-PACK, EXCEPTION, APP-SCHEMA, FOUR-EYES, LangGraph waits |
| **Power BI (service)** | Only after same org account works; else defer |

### Wave 1B (after work/school or M365 Dev tenant)

| Pillar | What |
| --- | --- |
| **Power Automate** | List / trigger / monitor import + exception flows |

**Blocker note:** Personal Microsoft accounts **cannot** use Power Automate cloud. See [[../personal-account-blocker]].

## Explicitly out (until Aman opens Wave 2+)

| Out | Why |
| --- | --- |
| **200+** random community mega-MCP dumps | Prefer **microsoft/power-platform-skills** instead |
| **Premium** connectors as default | Can force paid licenses |
| **Production** environments | Mandate + Governor |
| Copilot Studio / hosted Dataverse MCP from Cursor (Wave 1 default) | Credit / license risk — optional later |
| Live trading / cash | Hub X anti-goals |

## Explicitly **in** after org account (revised 2026-09-17)

| In | Source |
| --- | --- |
| **Canvas authoring** via skills + Canvas Authoring MCP | [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) `canvas-apps` |
| **Power Automate** build/debug via FlowAgent MCP | Same repo `power-automate` plugin |
| CAT extras (optional) | [microsoft/power-cat-skills](https://github.com/microsoft/power-cat-skills) |

Full write-up: [[official-skills-revalidation]]

## Wave 2 (later, only if you approve spend/risk)

- Solution packaging + ALM between Dev and a non-prod sandbox.  
- Optional premium connectors.  
- Production cutover checklist + FOUR-EYES.  
- Still **not** cloning 200+ community tools; grow **our** catalog by vertical need.
