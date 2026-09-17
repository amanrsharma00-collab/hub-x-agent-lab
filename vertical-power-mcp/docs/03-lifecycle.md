# 03 — Lifecycle: Plan → Validate → Execute → Test

**Master:** [[../PLAN]]

## Status

| Stage | State |
| --- | --- |
| **Plan** | **Revised** (Canvas + Automate official skills; Path A) |
| **Validate** | **Paused** — waiting org tenant + Aman says `validate` |
| Execute | Not started |
| Test | Not started |

## Plan checklist

- [x] Charter / scope / action catalog  
- [x] GitHub revalidation (Canvas + Automate skills)  
- [x] Path A account gate documented  
- [x] Oscar brief phrase wired  
- [x] DOC-MAP complete  

## Validate (when Aman is ready)

1. Org / M365 Dev account signs into make.powerapps.com  
2. Developer environment exists; Instance URL captured (no passwords in vault)  
3. Can create blank canvas + enable **Coauthoring**  
4. make.powerautomate.com works on **same** org account  
5. app.powerbi.com reachable  
6. `.NET 10` SDK present (for Canvas Authoring MCP) — `dotnet --list-sdks`  
7. Lab `sample_data/` + `.env.example` ready; IEA key optional for first pass  
8. Cursor can register **local** Vertical Power MCP (placeholder OK)  
9. Attempt Canvas Authoring MCP connect from Cursor (or note Copilot CLI fallback)

## Execute (after validate passes)

1. Implement our MCP modules in Lab `vertical-power-mcp/src/`  
2. Wire Cursor MCP: our server + Microsoft Canvas (+ Automate when ready)  
3. Phase 0 Energy Indicator table  
4. First canvas gallery via official skills  
5. First import flow (1B)

## Test criteria

| # | Pass |
| --- | --- |
| T1 | CSV profile works |
| T2 | IEA fetch or CSV fallback → typed rows |
| T3 | Upsert ≤30 indicators visible in Dataverse |
| T4 | Canvas sync shows gallery (Authoring MCP) |
| T5 | Flow run Succeeded (1B) |
| T6 | BI open hint or refresh (1D) |
| T7 | No secrets in git/Obsidian |

## LangGraph rail

`draft → WAIT Aman → execute → report → stop`
