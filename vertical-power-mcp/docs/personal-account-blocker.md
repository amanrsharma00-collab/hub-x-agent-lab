# Personal account blocker — how we proceed

**Fact:** Power Automate cloud and Developer Plan signup need a **work/school (Entra)** account. Personal MSA (outlook/hotmail/many personal logins) is blocked.

## Path A — LOCKED

Aman will provide **org / M365 Developer tenant** credentials soon.  
Then: sign into Apps · Automate · BI · Admin with that account → **`validate`**.

That unlocks:

- Dataverse Developer env  
- Power Automate + FlowAgent / `power-automate` skills  
- Canvas Studio coauthoring + **Canvas Authoring MCP** ([power-platform-skills](https://github.com/microsoft/power-platform-skills))

## Path B — only if org tenant delayed

Wave 1A data logic on CSV / local MCP only — no Automate, no Studio until Path A.  
Prefer not to stay here long.

## Still true after GitHub revalidation

Official Canvas skills **exist** — they do **not** remove the org-account requirement.  
See [[architecture/official-skills-revalidation]] · [[PLAN]]
