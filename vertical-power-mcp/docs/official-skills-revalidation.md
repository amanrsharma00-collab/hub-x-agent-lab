# Revalidation — official Canvas & Automate skills (GitHub)

**Date:** 2026-09-17  
**Trigger:** Aman flagged Canvas skills on GitHub; prior Hub X note understated them.

## Correction

We previously parked “canvas control authoring” as out-of-scope / no stable API.  
**That was incomplete.** Microsoft ships official **skills + Canvas Authoring MCP**.

## Core repos (validated)

| Repo | Stars (approx) | What it is |
| --- | --- | --- |
| [microsoft/power-platform-skills](https://github.com/microsoft/power-platform-skills) | ~879 | Official plugin marketplace: **canvas-apps**, **power-automate**, model-apps, code-apps, … |
| [microsoft/power-cat-skills](https://github.com/microsoft/power-cat-skills) | ~48 | Power CAT extras (e.g. `powercat-canvas-apps`) on top of the foundation plugin |
| [microsoft/Dataverse-skills](https://github.com/microsoft/Dataverse-skills) | — | Dataverse-focused skills (tables/query/admin) — not full canvas authoring |
| [microsoft/Dataverse-MCP](https://github.com/microsoft/Dataverse-MCP) | — | Labs for **hosted** Dataverse MCP |

Docs: [Create/edit canvas apps with AI code tools](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-canvas-external-tools)

## Canvas Apps plugin (what Aman saw)

From `plugins/canvas-apps/skills/`:

| Skill | Job |
| --- | --- |
| `canvas-app` | Create/edit canvas via `.pa.yaml` + coauthoring |
| `configure-canvas-mcp` | Connect **Canvas Authoring MCP** to Studio session |
| `add-data-source` | Guide adding connectors/sources in Studio |

**MCP tools (examples):** `connect`, `sync_canvas`, `compile_canvas`, `describe_control`, list controls, …

**Stack:** `.pa.yaml` + `CanvasAuthoringMcpServer` (NuGet) · needs **.NET 10 SDK**

**Session model:** Blank/existing app in Power Apps Studio → enable **Coauthoring** → keep Studio tab open → agent edits YAML → MCP validates/syncs.

## Power Automate plugin (same marketplace)

`plugins/power-automate` — skills: `create-flow`, `build-flow`, `debug-flow`, `manage-flows`, …  
Uses **FlowAgent MCP** (Node 18+ · `az login`).  
Still requires an **organizational** Power Platform account — does **not** revive personal MSA Automate access.

## What this changes for PowerVertical

| Old plan | Updated |
| --- | --- |
| Canvas authoring = out | **In** once org env works — prefer Microsoft Canvas Authoring MCP + skills |
| Only “our thin MCP” for UI | Thin/vertical MCP for **IEA + Dataverse data path**; Canvas MCP for **UI authoring** |
| “No stable API” | Official coauthoring MCP is the supported path |

## What does **not** change

1. **Personal Microsoft account** still cannot use Power Automate cloud / Developer Plan signup — need org / M365 Dev tenant (**Path A**).  
2. Canvas skills need a **Power Platform environment** + Studio coauthoring — same account gate.  
3. Hosted Dataverse MCP from Cursor can still risk Copilot credits — keep local data MCP for $0 Wave 1 data path unless Aman accepts risk.  
4. Docs target Copilot CLI / Claude / VS Code plugins; Cursor can use MCP if we wire the same Canvas Authoring server — **validate in Execute**, not assumed day-one.

## Recommended stack (revised)

```text
Org account (Path A)
  ├─ Data path: our Vertical Power MCP (IEA → Dataverse) — $0 local
  ├─ UI path: Microsoft Canvas Authoring MCP + canvas-app skill
  └─ Flow path: Microsoft power-automate plugin / FlowAgent MCP (Wave 1B)
```

## Next

1. Aman completes **Path A** (org/dev tenant).  
2. On validate: check Studio + .NET 10 + whether Canvas MCP runs from Cursor.  
3. Mirror skill pointers into `PowerVertical/` + Lab `docs/`.  
4. Do **not** clone 200+ community tools — use **microsoft/power-platform-skills** as the UI/flow foundation.
