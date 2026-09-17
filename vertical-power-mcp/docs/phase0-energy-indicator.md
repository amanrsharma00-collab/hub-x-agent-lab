# Phase 0 — Energy Indicator MVP (IEA)

**Still the data-layer schema for PowerVertical.**  
**Stack now:** see Hub X `PowerVertical/PLAN.md`.

**Env:** Power Apps Developer (org account) · Cursor + our MCP + Microsoft Canvas/Automate MCPs  
**External:** IEA (key in Lab `.env` only)

## 1. Architectural Data Schema

### Table: Energy Indicator
**Schema name (suggested):** `cr_energyindicator`  
**Primary name column:** `cr_name` (Indicator label)

| Column | Type | Notes |
| --- | --- | --- |
| `cr_name` | Text (100) | e.g. Electricity generation |
| `cr_indicatorcode` | Text (50) | IEA / internal code |
| `cr_country` | Text (100) | Country or region name |
| `cr_countrycode` | Text (10) | ISO-ish code if present |
| `cr_period` | Text (20) | e.g. 2023, 2023-Q1 |
| `cr_periodstart` | Date only | Optional parse of period |
| `cr_value` | Decimal | Numeric value |
| `cr_unit` | Choice | see below |
| `cr_source` | Choice | IEA (default) |
| `cr_sourceref` | Text (200) | Dataset / series id or URL slug |
| `cr_importrunid` | Text (36) | Groups one Automate import |
| `cr_asof` | Date and time | When row was loaded |

**Choices — Unit:** `GWh` · `TWh` · `MW` · `kt` · `PJ` · `percent` · `other`  
**Choices — Source:** `IEA` · `Manual`  

**Relationships (MVP):** none required. Later: link to Country reference table if needed.

**Security (MVP):** one security role *Energy Indicator Read-Write* for you in developer env; no sharing outside env.

## 2. Agent Action & Plugin Definitions (Cursor → Automate)

No Copilot Studio. Cursor proposes; Automate executes typed inputs only.

### Action A — `ImportIeaIndicators`
| | |
| --- | --- |
| Trigger | Aman says approve import / Cursor handoff after pack |
| Inputs (required) | `importrunid` (string), `rows` (array of typed objects) |
| Row object | `name`, `indicatorcode`, `country`, `countrycode`, `period`, `value` (number), `unit` (enum), `sourceref` |
| Outputs | `createdcount`, `failedcount`, `importrunid`, `errors[]` |
| Forbidden | Extra JSON keys; free-text SQL; untyped “payload” blobs |

### Action B — `ListIndicatorsByPeriod`
| | |
| --- | --- |
| Trigger | Brief / gallery refresh |
| Inputs | `period` (string), optional `countrycode` |
| Outputs | `items[]` with name, country, value, unit |

### Action C — `FlagExceptions`
| | |
| --- | --- |
| Trigger | After import |
| Inputs | `importrunid`, `rule` enum: `missing_value` \| `unknown_unit` |
| Outputs | `exceptioncount`, `sampleids[]` (≤10) |

## 3. Power Automate Workflow Logic

### Flow 1 — `IEA Indicator Import` (manual / instant cloud flow)

1. **Trigger:** Instant — inputs: `importrunid` (text), `rowsJson` (text).  
2. **Parse JSON** — schema = row object above (reject unknown fields).  
3. **Apply to each** row:  
   - **Create new row** in Dataverse → Energy Indicator.  
   - Map columns; set `cr_source` = IEA; set `cr_asof` = `utcNow()`.  
4. **Scope** with **Configure run after** failure → append to `errors` string variable.  
5. **Response** (or Compose for maker): `{ createdcount, failedcount, importrunid, errors }`.  

**Error handling:** do not stop whole run on one bad row; count failures; return errors ≤20 lines.

### Flow 2 — `List by Period` (instant)

1. Trigger inputs: `period`, optional `countrycode`.  
2. **List rows** Dataverse — filter: `cr_period eq '{period}'` (+ country if provided).  
3. **Select** → slim fields.  
4. Return JSON array.

### Flow 3 — `Flag Exceptions` (instant)

1. List rows where `cr_importrunid eq '{id}'` and (`cr_value` empty OR unit = other unexpectedly).  
2. Return count + first 10 ids.

## 4. Power Fx snippets (canvas app — browser)

**Gallery items** (Energy Indicators):
```powerfx
SortByColumns(
  Filter('Energy Indicators', period = PeriodDropdown.Selected.Value),
  "cr_country",
  SortOrder.Ascending
)
```

**Patch one manual row** (test without Flow):
```powerfx
Patch(
  'Energy Indicators',
  Defaults('Energy Indicators'),
  {
    cr_name: TitleInput.Text,
    cr_indicatorcode: CodeInput.Text,
    cr_country: CountryInput.Text,
    cr_countrycode: CountryCodeInput.Text,
    cr_period: PeriodInput.Text,
    cr_value: Value(ValueInput.Text),
    cr_unit: 'Unit (Energy Indicators)'.GWh,
    cr_source: 'Source (Energy Indicators)'.IEA,
    cr_sourceref: SourceRefInput.Text,
    cr_importrunid: ImportRunInput.Text,
    cr_asof: Now()
  }
)
```
*(Choice path names follow whatever the maker portal shows after you create choices.)*

**KPI label — row count in view:**
```powerfx
"Rows: " & CountRows(Gallery1.AllItems)
```

## Browser try order (Mac)

1. make.powerapps.com → Developer environment → create table **Energy Indicator** + columns above.  
2. Create instant Flow **IEA Indicator Import** (even if you first Patch 2–3 rows by hand).  
3. Canvas app: gallery + period dropdown + KPI label.  
4. Reply `approved` or `revise` with what broke.

## Sample seed (optional)

Reuse Lab idea: small CSV shaped like IEA rows → later map into `rowsJson`. Keep under developer capacity.
