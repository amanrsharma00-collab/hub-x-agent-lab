# Power Apps / Power Platform MCP — core finding

**Updated:** 2026-09-17  
**Question:** Can we MCP “all Power Apps tools”? Is there a GitHub core? Build our own?

## Short answer

| Question | Answer |
| --- | --- |
| Can we do it? | **Yes** — but “all tools” is **not one open repo**. Microsoft hosts **Dataverse MCP**; apps/flows tooling is separate / community. |
| Rebuild Microsoft? | **No.** Use official Dataverse MCP first. |
| Build our own? | **Yes, thin** — only typed tools we need (IEA Energy Indicator MVP) if official gaps or free-lane blocks. |

## Core (official Microsoft)

| Repo / doc | What it is |
| --- | --- |
| [microsoft/Dataverse-MCP](https://github.com/microsoft/Dataverse-MCP) | Labs for **Dataverse remote MCP** (setup + Claude + VS Code) |
| [microsoft/pp-mcp](https://github.com/microsoft/pp-mcp) | Power Platform MCP labs & samples ([aka.ms/pp-mcp](https://aka.ms/pp-mcp)) |
| [microsoft/Dataverse-skills](https://github.com/microsoft/Dataverse-skills) | Agent **skills** wrapping Dataverse MCP + PAC / SDK |
| [Learn: Dataverse MCP](https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp) | Hosted server: `https://{org}.crm.dynamics.com/api/mcp` |

**Dataverse MCP tools (hosted):** `search_data`, `search`, `create_record`, `update_record`, `delete_record`, `create_table`, `update_table`, `delete_table`, `read_query`, `describe`, skill upsert/delete, file upload helpers.

**Separate:** Power Apps MCP server (agent feed / `invoke_data_entry` with **human review**) — docs under Power Apps maker; not “clone all maker studio.”

**Cursor note:** Docs stress VS Code GitHub Copilot + Claude. Cursor can speak MCP, but admin must **allow the client** in Power Platform admin center. Non–Copilot Studio agent use may incur **Copilot credit billing** (Microsoft policy from Dec 2025) — check before heavy use.

## Community (broader “Power Platform tools”)

| Repo | Notes |
| --- | --- |
| [rcb0727/powerplatform-mcp-server](https://github.com/rcb0727/powerplatform-mcp-server) | Large tool surface (~280+), Azure CLI auth — community, not Microsoft |
| [viswmish/powerapps-custom-mcp](https://github.com/viswmish/powerapps-custom-mcp) | Claims apps/flows/canvas authoring tools — low stars; vet before trust |
| [mwhesse/dataverse-mcp](https://github.com/mwhesse/dataverse-mcp) | Local schema ops via Web API |
| [Cliveo/Power-Platform-MCP](https://github.com/Cliveo/Power-Platform-MCP) | .NET Dataverse + Automate |

Treat community as **reference**, not production blind trust.

## What does *not* exist as one official OSS

A single Microsoft open-source MCP that exposes **every** Power Apps maker action (all canvas controls, all connectors, full solution ALM) as clone-and-run.  
Official path = **hosted Dataverse MCP** (+ optional Power Apps MCP features in product).

## Recommended Hub X path (free try · Mac · Cursor)

1. **Try official** Dataverse MCP against Developer env (enable MCP clients in admin; get Instance URL from make.powerapps.com session details).  
2. If blocked (client not allowed / billing / missing tools) → **build thin Hub MCP** in Agent Lab:  
   - Governor kit: [mcp python-sdk](https://github.com/modelcontextprotocol/python-sdk)  
   - Tools only from Phase 0: `ImportIeaIndicators`, `ListIndicatorsByPeriod`, `FlagExceptions` (typed JSON → Dataverse Web API)  
   - LangGraph wait before create/update/delete  
3. Do **not** chase “283 tools” for MVP.

## Status

| Step | State |
| --- | --- |
| Radar | Done (this note) |
| Wire Cursor → Dataverse MCP | **Waiting Aman approve** |
| Scaffold thin `hub-x-power-mcp` | Ready when you say go |

## Related

- [[vertical-mvp-lock]] · [[phase0-energy-indicator]] · [[Governor/connect-stack]] (#2 MCP sdk)
