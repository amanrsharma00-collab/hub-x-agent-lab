# Hub X Agent Lab

**Obsidian Hub X** = notes. **This folder** = named crews + CrewAI code.

## Call names (say these)

| Call | Job |
| --- | --- |
| **DESK-BRIEF** | Explain a topic (3→5 bullets) |
| **ROSETTA-PASS** | Jargon → plain + ETRM |
| **ATLAS-PICK** | Which agent shape / kit |
| **TOKEN-GATE** | Cheap research path |
| **OSCAR-WIRE** | Short GitHub brief |
| **FOUR-EYES** | Human-approval gate |

Full index: [`crews/CALL-BOOK.md`](crews/CALL-BOOK.md)

Example: `Run DESK-BRIEF on topic: what is an agent`

## Layout

```
crews/           MD specs + CALL-BOOK
crews/code/      CrewAI Python sketches
.cursor/skills/  hub-x-crews skill
.cursor/rules/   always-on call names
```

## Setup

```bash
cd ~/Documents/Hub-X-Agent-Lab
source .venv/bin/activate
python -c "import crewai; print(crewai.__version__)"
```

Live `kickoff()` needs a model API key. Markdown crews work in Cursor chat without it.

## GitHub

https://github.com/amanrsharma00-collab/hub-x-agent-lab
