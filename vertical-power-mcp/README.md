# Vertical Power MCP — Agent Lab

**Obsidian notes:** `Hub X/PowerVertical/`  
**This folder:** code, local MCP, secrets, samples.

## Layout

```
vertical-power-mcp/
  docs/           Mirrored essentials from PowerVertical
  src/            MCP server (Execute phase)
  config/         mcp.json.example
  scripts/        helper scripts
  sample_data/    CSVs for free tests
  .env.example    Secret names only
```

## Rules

Follow Hub X `PowerVertical/rules/operating-rules.md`:  
Markdown crews · LangGraph wait · Wave 1 $0 · no hosted Dataverse MCP.

## Status

| Stage | State |
| --- | --- |
| Plan | Done (docs) |
| Validate | Waiting Aman answers + `validate` |
| Execute | MCP scaffold not started |
| Test | Not started |

## Secrets

Copy `.env.example` → `.env` (gitignored). Never commit keys.
