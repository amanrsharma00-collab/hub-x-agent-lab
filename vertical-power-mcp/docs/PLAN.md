# PowerVertical — master plan (current)

**Updated:** 2026-09-17  
**Status:** Plan revised after GitHub revalidation. **Re-validate after org tenant.**  
**Account path:** **A locked** — Aman will provide org / M365 Dev tenant credentials soon. Personal MSA is not the build account.

## One-sentence goal

Energy (IEA) vertical on Power Platform: **data in Dataverse**, **UI via Canvas Authoring MCP**, **flows via Automate MCP**, **BI in browser**, **Cursor + Hub X skills + LangGraph waits**, Wave 1 without new Microsoft bill where possible.

## Architecture (three hands)

```text
Cursor (brain) + Markdown crews + LangGraph WAIT
        │
        ├─ Vertical Power MCP (ours, local)     → IEA + Dataverse data path ($0 lane)
        ├─ Canvas Authoring MCP (Microsoft)     → .pa.yaml UI coauthoring
        └─ FlowAgent MCP (Microsoft)            → cloud flows (needs org account)
```

Foundation skills repo: [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills)  
Extras (optional): [microsoft/power-cat-skills](https://github.com/microsoft/power-cat-skills)  
Our code: Agent Lab `vertical-power-mcp/`

## Waves

| Wave | When | What |
| --- | --- | --- |
| **1A** | After org tenant validate | Dataverse Energy Indicator + our MCP (IEA/CSV upsert) + blank canvas + coauthoring |
| **1B** | Same tenant | Automate flows + FlowAgent / `power-automate` plugin |
| **1C** | Same tenant | Canvas Authoring MCP + `canvas-app` skill from Cursor (or Copilot CLI if Cursor blocked) |
| **1D** | Same tenant | Power BI service report + refresh hints |
| **2** | Aman approve | ALM / non-prod promote / optional premium / production checklist |

## Explicitly out (still)

- Random 200+ community mega-MCPs (use Microsoft skills instead)  
- Premium connectors as default  
- Production without FOUR-EYES  
- Hosted Dataverse MCP from Cursor as Wave 1 default (credit risk)  
- Live trading / cash  

## Lifecycle status

| Stage | State |
| --- | --- |
| Plan | **Revised — current** |
| Validate | **Paused** until org tenant + Aman says `validate` |
| Execute | Not started (MCP scaffold after validate) |
| Test | Not started |

## Oscar brief

Phrase: **Oscar, brief me** (or **Oscar brief me**) → follow [[oscar-brief]] — plan + every covering document with updated insights.
