---
name: power-platform-analytics
description: Analytical packs for free Power Apps Developer Plan / Power BI Desktop using Hub X sample CSVs and LangGraph wait-for-human rails. Use when Aman asks for Power Platform analytics, KPI packs, PROFILE/EXCEPTION/APP-SCHEMA modes, or testing skills on sample_data.
---

# Power Platform analytics (free test lane)

Audience: Aman. Plain English. No trading examples.

## When to use

Power Apps / Power BI / Dataverse **analytics packs** on free or developer tools.  
Not for live production publish. Not a seventh Markdown crew call.

## Free lane only

1. Power Apps **Developer Plan** (dev/test Dataverse).  
2. **Power BI Desktop** (author reports free).  
3. CSV / Excel from Agent Lab `toolkits/sample_data/`.  
4. Prefer Hub X `Connect/power-platform-free-analytics.md` + `Connect/langgraph-start.md` before any web hunt.

## Modes (pick one)

| Mode | Input | Output (hard caps) |
| --- | --- | --- |
| **PROFILE** | one CSV | ≤8 bullets: rows, columns, nulls, junk risks |
| **KPI-PACK** | CSV + optional `kpi_targets.csv` | exactly **5** measures + **3** chart ideas + **1** app tile idea |
| **EXCEPTION** | CSV + rules/targets | ≤10 exception rows (id + why) + **3** fix ideas |
| **APP-SCHEMA** | after KPI or PROFILE | table columns (≤12) + **3** screen outline + **1** Flow trigger idea |

If mode missing → ask one question: `PROFILE, KPI-PACK, EXCEPTION, or APP-SCHEMA?`

## LangGraph rails (always)

1. **Load** sample file (do not invent rows).  
2. **Compute** in chat or Lab sketch.  
3. **Interrupt** — show pack; wait for Aman approve before any “create table / publish app / write Dataverse” steps.  
4. **Resume** only after explicit approve.  
5. Stop. No second research loop.

Sketch: `toolkits/langgraph_analytics.py`

## How Aman calls it

> Follow Connect/langgraph-start and power-platform-analytics. Mode: KPI-PACK on toolkits/sample_data/orders_sample.csv

## Must not

- Paid-premium connectors as the default path  
- Production environment writes  
- Browser scrape of Microsoft docs “for completeness”  
- Book trades / move money / change live systems  
- Replace DESK-BRIEF for simple definitions (use Markdown crews)
