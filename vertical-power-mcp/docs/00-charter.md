# 00 — Charter (simple words)

## What this is

A **vertical integration** for **Energy data (IEA)** into Microsoft Power Platform, driven from **Cursor**:

1. **Pull** indicators from IEA (API key in local `.env` only).  
2. **Store** them in Dataverse on a **Developer** environment (org account).  
3. **Automate** refresh/checks with Power Automate (org account + FlowAgent MCP).  
4. **Build UI** with official **Canvas Authoring MCP** + canvas skills (`.pa.yaml` + Studio coauthoring).  
5. **Show** KPIs in Power BI **service** (browser on Mac).  
6. **Control** data path with **our** Vertical Power MCP; UI/flows with **Microsoft** MCPs.

## Who does what

| Who | Role |
| --- | --- |
| Cursor + Hub X skills + crews | Brain: plan, brief, wait for you |
| Our Vertical Power MCP | Hands: IEA + Dataverse typed data tools |
| Microsoft Canvas Authoring MCP | Hands: canvas screens/controls via coauthoring |
| Microsoft FlowAgent / Automate plugin | Hands: cloud flows |
| You (browser) | Studio coauthoring tab, approve risky steps |
| Org tenant | Required login (personal MSA cannot run Automate) |

## Success

- IEA → Dataverse → Canvas gallery → Flow → BI path works on Developer.  
- Docs portable via Obsidian `PowerVertical/` if we leave Cursor.  
- Same design can promote later (Wave 2) when Aman approves.

See [[../PLAN]].
