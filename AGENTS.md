# Codex Toolkit — project handoff

## Goal and current state
I am building a small reusable agent toolkit, using Codex in VS Code on Windows. The local codex-toolkit folder has been created. This handoff records planning, not completed implementation or demonstrations.

Use a NEW public GitHub repository for this assignment, separate from Personal-Website. Suggested layout: sibling codex-toolkit and Personal-Website folders. Do not publish or push unless the user instructs you to.

## Agreed implementation
1. A narrow checker skill: review stated requirements against actual behavior, including persistence, repeated use, and relevant edge cases. Report without modifying files. Give file/line evidence for code findings; distinguish static inspection from observed runtime behavior. Mark untested claims as unverified. Use a defined output format and a description explaining when to invoke it.
2. A local stdio MCP server exposing exactly ONE tool, search_movies. Reuse the user's Movie Mood semantic search implementation and existing database. Return structured movie results with IDs, titles, and actual plot evidence. Do not invent movies, plot evidence, or successful calls. Validate inputs and keep logging off stdout.

Keep scope small. The MCP supplies structured access to the local semantic movie index; the skill supplies review procedure. Codex can already read files and run commands, so explain the MCP's benefit precisely rather than claiming it makes all local data newly accessible.

## Existing project
Repository: https://github.com/ShauryaTanwar/Personal-Website
Movie project subdirectory: movie_mood/
Relevant files inspected during planning: movie_mood/README.md and requirements-tested.txt; the project file listing was also inspected. Search implementation has NOT yet been reviewed.
Likely integration files: movie_mood/movie_mood/core.py, cli.py, embedding.py, and pyproject.toml. Read these before choosing an integration.
README reports Chroma collection movie_plots_v1, local all-MiniLM-L6-v2 embeddings, and separate SQLite user state. Default data directory: ~/.movie_mood; override via MOVIE_MOOD_HOME or --home. Actual database location and availability on the user's computer are unconfirmed. Git excludes data. Do not reimport, reset, or delete the existing database unnecessarily. Determine whether search mutates saved intent and isolate demo state if necessary.

## Prompt-log evidence already located
All five files below were accessed in the public repository. Some are representative summaries rather than complete transcripts. Do not invent additional quotes or assume homework numbers from folder names; ask the user to confirm the HW3–HW7 mapping if needed.
- Uncharted/prompt_log.md
- crossy-road/prompt_log.md
- auxcade/prompt_log.md
- movie_mood/prompt_log.md
- Bloom/prompt_log.md

Verbatim user excerpts supporting the checker:
- Uncharted: "When i reload the website the locations I visited and chats are saved but the globe resets. please fix that"
- Crossy Road: "interestingly after 200 points the player cannot collect coints anymore"
- Bloom (excerpt): "Just some small bugs so far, the UI is overlapping itself and the items that should be in the corner are slightly not."
These suggest recurring gaps between a completion claim and behavior during actual use. A general requirements checker is an agreed direction, not something the logs explicitly name.

Verbatim Movie Mood preference supporting local reuse:
"Keep everything local and avoid paid APIs"
Movie Mood performance prompt:
"it takes an incredibly long time to search compared to the CLI. investigate the problem and see if you can cut it down. Also, rework the UI to become more old styled movie theater themed"
These support local search and attention to latency; do not falsely claim the logs already requested MCP.

## Assignment requirements
- Ground both toolkit choices in actual HW3–HW7 prompt logs, quoting two or three relevant lines.
- Browse existing skills, record borrowing/adaptation, and critically assess suitability and security.
- First install a trivial temporary skill and verify Codex actually loads it, then build the real checker. Check CURRENT official Codex docs for skill discovery and MCP registration rather than trusting stale paths.
- Build one checker skill folder containing SKILL.md with YAML name and description, explicit steps, constraints, and output format.
- Build one working local stdio MCP tool with source and dependency files. Verify it starts, registers, and is actually called by Codex. Registration is not proven by calling the Python function directly.
- Use BOTH pieces on real work at least twice. The producer calls the MCP; the checker runs in a separate fresh agent session, ideally a different model. Preserve trimmed transcripts showing actual tool calls and checker output. Do not claim a fresh session happened unless it did.
- Find a genuine checker misfire, preserve version 1, diagnose and revise it, then rerun. Do not manufacture a historical failure or quietly replace it with an unrelated server bug.
- Submit a NEW public repo and its link through https://forms.gle/9n3VJxmS6R1D65ME6 . Assignment states Sunday November 8, 2026 at 8 PM; timezone is not specified in the provided assignment.
- Repository includes skill folder, MCP source/dependencies, and three SEPARATE HUMAN-WRITTEN documents: README.md, DEMONSTRATION.md, ITERATION.md.
- README: purpose/triggers, evidence motivating each component, installation and exact MCP config with machine paths identified, confirmed clients, attribution, AI-use note/citations.
- DEMONSTRATION: real task, both runs with transcript excerpts, checker findings, student's own agreement/disagreement.
- ITERATION: concrete failure, student's diagnosis, change, observed rerun result.
Do not ghostwrite those three submissions. Offer outlines or prompts and review the student's drafts. Never invent the student's opinions, testing, work hours, or independent contributions.

## Immediate next steps
1. Inspect this folder and any existing instructions. Locate the sibling Personal-Website/movie_mood project; ask for its path only if it cannot be found reasonably. Check the Python interpreter and existing database without exposing secrets.
2. Explain the small implementation plan; inspect current official Codex/MCP docs and the existing movie search API.
3. Verify trivial skill discovery, then implement checker v1 and the one-tool server with minimal meaningful checks and install instructions in an AI-labeled technical notes file, separate from the required human-written README.
4. Help the user register the server in local Codex, preserving unrelated config. The assignment gives ~/.codex/config.toml as a starting point; verify current docs and use absolute Windows paths with forward slashes.
5. Guide two real demonstrations and a fresh-context checker review; capture honest evidence and a real revision. Make clear which steps require the user's local VS Code session.

## Working style
Be direct and practical. Continue authorized implementation without repeated permission questions. Ask only for genuinely missing paths or decisions. Do not modify Personal-Website unnecessarily. Keep secrets, virtual environments, downloaded corpora, databases, and machine-specific private config out of the public toolkit repository.
