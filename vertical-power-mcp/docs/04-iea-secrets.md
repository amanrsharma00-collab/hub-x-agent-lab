# 04 — IEA API keys (safe)

You said you can provide IEA API keys. **Do not paste keys into Hub X notes or chat.**

## Where they live

| Place | OK? |
| --- | --- |
| Agent Lab `.env` (gitignored) | Yes |
| macOS Keychain / env var `IEA_API_KEY` | Yes |
| Obsidian vault / GitHub / Oscarwire | **Never** |
| Cursor chat | **Never** (say “key is in .env” only) |

## Setup (when Execute starts)

1. In `Hub-X-Agent-Lab/`, create `.env` from `.env.example`.  
2. Put `IEA_API_KEY=...` locally.  
3. MCP reads env at runtime; tools only see “key present: yes/no.”  
4. Rotate key if it ever leaks into a screenshot or commit.

## What the key is used for

Only `iea.*` actions: list/fetch series for the Energy Indicator vertical.  
Not for Microsoft login (that stays your Microsoft account / device code for Dataverse·Automate·BI).

## Related

[[02-action-catalog]] · [[03-lifecycle]]
