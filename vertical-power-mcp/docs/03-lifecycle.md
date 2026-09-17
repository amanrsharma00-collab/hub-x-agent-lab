# 03 — Lifecycle: Plan → Validate → Execute → Test

## Status

| Stage | State |
| --- | --- |
| **Plan** | **Done** (this pack) |
| Validate | Waiting — Aman says `validate` |
| Execute | Not started — scaffold MCP in Agent Lab |
| Test | Not started — IEA + one period + browser check |

## Plan (done) — checklist

- [x] Charter: vertical Energy integrate, not POC  
- [x] Scope: Apps + Automate + BI + IEA; outs listed  
- [x] Action catalog multi-pillar  
- [x] $0 Wave 1 money rule  
- [x] IEA key handling note  

## Validate — what we check (no spend)

1. Browser: Developer environment exists (make.powerapps.com).  
2. Dataverse: can create/open **Energy Indicator** (Phase 0).  
3. Automate: can create one instant flow in same env (under free run cap).  
4. Power BI service: can open app.powerbi.com with same Microsoft account (My Workspace).  
5. Lab: `toolkits/sample_data/` readable.  
6. Secrets: place for `IEA_API_KEY` exists locally (file not committed).  
7. Cursor: can run **local** MCP process (python-sdk) — no Azure paid SKU required for Wave 1 design.

Fail any item → fix before Execute.

## Execute — build order

1. Agent Lab package `toolkits/hub_x_vertical_power_mcp/`  
2. Implement modules: `lab`, `iea`, `apps`, `flow`, `pbi`  
3. Cursor `mcp.json` → local server only  
4. Hub X skill update: `power-platform-vertical-architect` + agentic chain call MCP tools after approve  
5. Browser: one Import flow + one simple report connected to Dataverse/Excel bridge as available on free tier  

## Test — success criteria

| # | Test | Pass |
| --- | --- | --- |
| T1 | `lab.profile_csv` on sample | Profile returns |
| T2 | `iea.fetch_series` with your key | ≥1 typed row (or clear auth error) |
| T3 | Approve → upsert ≤30 indicators | Rows visible in Dataverse |
| T4 | `flow.trigger_*` + `flow.get_run` | Succeeded |
| T5 | `pbi.refresh_dataset` or report open hint | Browser shows numbers |
| T6 | No call to official `/api/mcp` | Confirmed in config |

## LangGraph rail (every write)

`draft action → show typed payload → WAIT Aman → execute → report → stop`
