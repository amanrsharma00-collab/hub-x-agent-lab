# 02 — Action catalog (multi-action vertical)

Typed tools only. No free-form “run any API.”  
Prefix = module. Every **write** tool requires prior Cursor **approve** (LangGraph wait).

## A. Shared / Lab

| Action | In | Out |
| --- | --- | --- |
| `lab.profile_csv` | path | ≤8 profile bullets |
| `lab.kpi_pack_csv` | path + optional targets | 5 measures + 3 chart ideas |
| `lab.flag_csv_exceptions` | path + rules | ≤10 rows |

## B. IEA

| Action | In | Out |
| --- | --- | --- |
| `iea.list_datasets` | optional filter | id, name, period coverage |
| `iea.fetch_series` | dataset/series ids, country, period range | typed rows (name, code, country, period, value, unit, sourceref) |
| `iea.map_to_energy_indicator` | IEA rows | Dataverse-ready row objects |

**Secrets:** API key from local env only — see [[04-iea-secrets]].

## C. Power Apps / Dataverse

| Action | In | Out |
| --- | --- | --- |
| `apps.whoami` | — | env url, user, is_developer |
| `apps.list_tables` | optional prefix | table logical names |
| `apps.describe_table` | table | columns, types, choices |
| `apps.ensure_energy_indicator` | — | create-if-missing schema from Phase 0 |
| `apps.upsert_energy_indicators` | importrunid + rows[] | created, updated, failed, errors[] |
| `apps.list_by_period` | period, optional country | items[] |
| `apps.flag_exceptions` | importrunid + rule | count + sample ids |
| `apps.list_canvas_apps` | — | app name, id, web link |
| `apps.open_hint` | app id | browser URL for maker/player |

**Not in catalog:** pixel-level canvas control create/edit.

## D. Power Automate

| Action | In | Out |
| --- | --- | --- |
| `flow.list` | optional name filter | flow name, id, state |
| `flow.describe` | flow id | trigger type, expected inputs |
| `flow.trigger_iea_import` | importrunid + rowsJson | run id |
| `flow.trigger_flag_exceptions` | importrunid | run id |
| `flow.get_run` | run id | status, error summary |
| `flow.list_runs` | flow id, top N | recent statuses |

Flows themselves are built once in browser (or generated as definition packs in Execute phase); MCP **triggers and monitors** them.

## E. Power BI (service · browser)

| Action | In | Out |
| --- | --- | --- |
| `pbi.list_workspaces` | — | id, name (My Workspace OK) |
| `pbi.list_datasets` | workspace id | id, name |
| `pbi.list_reports` | workspace id | id, name, webUrl |
| `pbi.refresh_dataset` | dataset id | refresh id / accepted |
| `pbi.get_refresh_history` | dataset id, top N | statuses |
| `pbi.report_open_hint` | report id | browser URL |

**Not in catalog:** Power BI Desktop (.pbix authoring on Windows). Mac = service + browser.

## F. Vertical orchestration (skills call these in order)

1. `iea.fetch_series` → `iea.map_to_energy_indicator`  
2. **WAIT approve**  
3. `apps.upsert_energy_indicators` **or** `flow.trigger_iea_import`  
4. `flow.get_run` until Succeeded/Failed  
5. `apps.list_by_period` + `apps.flag_exceptions`  
6. `pbi.refresh_dataset` → `pbi.report_open_hint`  
7. Stop

## Related schema

[[../phase0-energy-indicator]]
