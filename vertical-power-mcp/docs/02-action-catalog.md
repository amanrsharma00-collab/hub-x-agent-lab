# 02 — Action catalog (multi-action vertical)

Typed tools only. No free-form “run any API.”  
Every **write** requires LangGraph **WAIT** (`approved`).  
**Master plan:** [[../PLAN]]

## A. Shared / Lab — our MCP

| Action | In | Out |
| --- | --- | --- |
| `lab.profile_csv` | path | ≤8 profile bullets |
| `lab.kpi_pack_csv` | path + optional targets | 5 measures + 3 chart ideas |
| `lab.flag_csv_exceptions` | path + rules | ≤10 rows |

## B. IEA — our MCP

| Action | In | Out |
| --- | --- | --- |
| `iea.list_datasets` | optional filter | id, name, period coverage |
| `iea.fetch_series` | dataset/series ids, country, period range | typed rows |
| `iea.map_to_energy_indicator` | IEA rows | Dataverse-ready row objects |

Secrets: [[../secrets/04-iea-secrets]]

## C. Power Apps / Dataverse — our MCP (Wave 1A)

| Action | In | Out |
| --- | --- | --- |
| `apps.whoami` | — | env url, user, is_developer |
| `apps.list_tables` | optional prefix | table logical names |
| `apps.describe_table` | table | columns, types, choices |
| `apps.ensure_energy_indicator` | — | create-if-missing (Phase 0) |
| `apps.upsert_energy_indicators` | importrunid + rows[] | created, updated, failed, errors[] |
| `apps.list_by_period` | period, optional country | items[] |
| `apps.flag_exceptions` | importrunid + rule | count + sample ids |
| `apps.list_canvas_apps` | — | app name, id, web link |
| `apps.open_hint` | app id | browser URL |

## D. Power Automate — Wave 1B (org account + Microsoft / our trigger tools)

| Action | In | Out |
| --- | --- | --- |
| `flow.list` | optional name filter | flow name, id, state |
| `flow.describe` | flow id | trigger type, inputs |
| `flow.trigger_iea_import` | importrunid + rowsJson | run id |
| `flow.trigger_flag_exceptions` | importrunid | run id |
| `flow.get_run` | run id | status, error summary |
| `flow.list_runs` | flow id, top N | recent statuses |

Build/debug also via Microsoft **`power-automate`** plugin / FlowAgent MCP when wired.  
See [[../personal-account-blocker]].

## E. Power BI service — Wave 1D

| Action | In | Out |
| --- | --- | --- |
| `pbi.list_workspaces` | — | id, name |
| `pbi.list_datasets` | workspace id | id, name |
| `pbi.list_reports` | workspace id | id, name, webUrl |
| `pbi.refresh_dataset` | dataset id | refresh id / accepted |
| `pbi.get_refresh_history` | dataset id, top N | statuses |
| `pbi.report_open_hint` | report id | browser URL |

Mac = browser only (no Power BI Desktop).

## F. Canvas authoring — Wave 1C (Microsoft Canvas Authoring MCP)

Not implemented in our Python MCP. Use Microsoft skills + MCP:

| Skill / tool | Job |
| --- | --- |
| `configure-canvas-mcp` / `connect` | Bind Studio coauthoring session |
| `canvas-app` | Create/edit screens via `.pa.yaml` |
| `compile_canvas` / `sync_canvas` | Validate and sync to Studio |
| `describe_control` / list controls | Discover UI surface |
| `add-data-source` | Guide Dataverse/connector bind in Studio |

Source: [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) `canvas-apps`  
Needs: .NET 10 · org env · Studio tab open with **Coauthoring**  
Detail: [[../architecture/official-skills-revalidation]]

## G. Vertical orchestration (happy path)

1. IEA fetch → map → **WAIT** → `apps.upsert` (or flow trigger in 1B)  
2. `apps.list_by_period` + flag exceptions  
3. Canvas: configure MCP → `canvas-app` gallery on Energy Indicator → compile/sync  
4. Optional: Automate schedule refresh  
5. `pbi.refresh` + open hint  
6. Stop  

Schema: [[../architecture/phase0-energy-indicator]]
