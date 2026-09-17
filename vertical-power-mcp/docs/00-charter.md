# 00 — Charter (simple words)

## What this is

A **vertical integration** for **Energy data (IEA)** into Microsoft Power Platform, driven from **Cursor**:

1. **Pull** indicators from IEA (you can supply API keys).  
2. **Store** them in Dataverse (Power Apps’ database) on Developer Plan.  
3. **Automate** refresh / checks with Power Automate.  
4. **Show** KPIs in Power BI **service** (browser on Mac).  
5. **Control** it with a **local Vertical Power MCP** — many typed actions, still not “every button in the world.”

## Why not “Thin MCP” alone?

Thin MCP was a **short menu for Dataverse only**.  
You need **Power Apps + Power Automate + Power BI** together so the vertical can run as a real workflow, not a one-table demo.

## Who does what

| Who | Role |
| --- | --- |
| Cursor + Hub X skills | Brain: plan, brief, wait for you |
| Vertical Power MCP (local) | Hands: typed tools for Apps / Automate / BI / IEA |
| You (browser) | See apps, flows, reports; approve risky steps |
| IEA | Source of energy datasets (keys in local secret file only) |

## Success looks like

- Multiple actions work across the three products.  
- IEA → Dataverse → Flow → BI path runs on **Developer** without new Microsoft bills.  
- Same design can later promote to a paid/production tenant **when you choose** (Wave 2) — Wave 1 does not require production.
