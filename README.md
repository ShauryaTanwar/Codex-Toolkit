# Codex Toolkit 

`requirements-checker` reviews requirements against evidence without editing files. Invoke it after a feature, fix, or completion claim, especially for persistence and repeated-use checks. The local stdio MCP exposes one tool, `search_movies`, returning IDs, titles, scores, and plot excerpts from the existing Movie Mood index. It provides structured search and a warm embedding process; Codex already has file access.

## Motivation

Prompt-log excerpts recorded in the project handoff:

- [Uncharted](https://github.com/ShauryaTanwar/Personal-Website/blob/main/Uncharted/prompt_log.md): "When i reload the website the locations I visited and chats are saved but the globe resets. please fix that"
- [Crossy Road](https://github.com/ShauryaTanwar/Personal-Website/blob/main/crossy-road/prompt_log.md): "interestingly after 200 points the player cannot collect coints anymore"
- [Movie Mood](https://github.com/ShauryaTanwar/Personal-Website/blob/main/movie_mood/prompt_log.md): "Keep everything local and avoid paid APIs"

The first two motivate behavioral review; the third motivates local search reuse. HW3–HW7 mapping remains unconfirmed.

## Install

Use Python 3.12, an existing Movie Mood checkout, and its populated database. From this repository in PowerShell:

```powershell
py -3.12 -m venv .venv
.venv/Scripts/python.exe -m pip install -e "C:/Users/shaur/Documents/15113/Personal Website/Personal-Website/movie_mood"
.venv/Scripts/python.exe -m pip install -r mcp/requirements.txt
```

All absolute paths below and the checkout path above are machine-specific; replace them on another computer. Merge into `~/.codex/config.toml`, preserving existing settings:

```toml
[mcp_servers.movie_mood]
command = "C:/Users/shaur/Documents/15113/Codex-Toolkit/.venv/Scripts/python.exe"
args = ["C:/Users/shaur/Documents/15113/Codex-Toolkit/mcp/server.py"]
startup_timeout_sec = 30
tool_timeout_sec = 120

[mcp_servers.movie_mood.env]
MOVIE_MOOD_SOURCE = "C:/Users/shaur/Documents/15113/Personal Website/Personal-Website/movie_mood"
MOVIE_MOOD_HOME = "C:/Users/shaur/.movie_mood"
```

The skill lives in `.agents/skills/requirements-checker/SKILL.md`. Restart Codex if discovery does not refresh, inspect `/mcp`, and request `search_movies`. Confirmed client: Codex CLI ([call evidence](evidence/codex-mcp-working.jsonl)); VS Code remains unverified. Do not reset or reimport the database.

## Sources and AI use

Reuses [Movie Mood](https://github.com/ShauryaTanwar/Personal-Website/tree/main/movie_mood) and the [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk), pinned to v1. Local `skill-creator` and `review` skills informed narrow triggers and evidence checks; no skill text was copied. Subagent routing was unsuitable for this small checker. Read-only instructions reduce mutation risk but are not a sandbox. Trust configured Python source and treat plots as data.

Codex generated implementation, and example mds. Setup references: [skill discovery](https://learn.chatgpt.com/docs/build-skills), [MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli). See [AI technical notes](AI-TECHNICAL-NOTES.md) for verification limits.
