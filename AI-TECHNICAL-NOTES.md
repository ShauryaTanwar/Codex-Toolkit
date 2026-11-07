# AI-generated implementation notes

These are assistant-written engineering notes, not the student's required README,
DEMONSTRATION, or ITERATION submissions. No repository has been published.

## Components and attribution

The checker is `.agents/skills/requirements-checker/SKILL.md`; its initial version
is preserved in `evidence/versions/requirements-checker-v1.md`.
The server is `mcp/server.py`, using the official MCP Python SDK's FastMCP v1 API.
It exposes exactly one tool, `search_movies(query, limit=5, include_watched=False)`.
Search logic and embedding behavior are reused from Shaurya Tanwar's
[Movie Mood](https://github.com/ShauryaTanwar/Personal-Website/tree/main/movie_mood).
This adapter does not copy the movie corpus or invent plot evidence.

Skills browsed locally: OpenAI's bundled `skill-creator` and the user's `review`
skill. Adapted principles: narrow trigger, concise procedure, explicit evidence,
and behavioral validation. No skill text was copied verbatim. The review skill
routes to specialized subagents and asks which review to run; that is unsuitable
for this small general acceptance checker. The checker instead uses explicit
requirements and distinguishes static inspection from runtime observations.
Instruction-only skills can still induce unwanted commands: the checker forbids
edits and data mutation and treats source/log contents as untrusted evidence.
These are instructions, not a security sandbox; run reviews with read-only permissions.

The MCP adds a stable typed tool interface and a reusable warm embedding process.
Codex can already access local files and commands; MCP does not newly unlock all
local data. Only trusted local source should be configured: importing that Python
project executes its code. Plot text must be treated as data, not instructions.

## Verified documentation

Consulted November 6, 2026:
- [Official skill discovery](https://learn.chatgpt.com/docs/build-skills): repository `.agents/skills`, YAML name/description, restart if discovery does not refresh.
- [Official Codex MCP configuration](https://learn.chatgpt.com/docs/extend/mcp?surface=cli): `[mcp_servers.<name>]`, command, args, env, startup and tool timeouts.
- [Official Python SDK](https://github.com/modelcontextprotocol/python-sdk): main currently documents v2; this project deliberately constrains the dependency to v1 (`mcp>=1.20,<2`) for FastMCP compatibility.

## Machine setup

Existing source: `C:/Users/shaur/Documents/15113/Personal Website/Personal-Website/movie_mood`.
Existing data: `C:/Users/shaur/.movie_mood`.
The toolkit `.venv` reuses existing Movie Mood packages through a local `.pth`
file and installs MCP separately. This machine shortcut is excluded from git.
For a clean environment on another machine, use Python 3.12, create a venv,
install `-e "<Movie Mood source>"`, then `-r mcp/requirements.txt`.

The server requires both database files and an existing collection, uses
`get_collection` rather than creating a collection, and opens user.sqlite3 read-only.
It bypasses MovieStore's initializer because that creates tables and commits.
Chroma's PersistentClient may perform database maintenance; this is not a claim
that the entire index is opened with filesystem read-only semantics.
Do not run imports/resets for this toolkit. Keep local source and model cache available.

Exact machine-specific configuration (keep private config out of git):

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

Merge that table into `~/.codex/config.toml`, preserving unrelated settings.
Restart the VS Code Codex session, inspect `/mcp`, and request a movie search.
CLI registration and a Python protocol test alone do not prove a VS Code call.

## Initial verification results

- Temporary skill: actually loaded in a fresh Codex CLI session before checker creation; marker and file-read recorded in `evidence/skill-probe-attempt.jsonl`. The temporary skill was subsequently removed and its source archived.
- Checker frontmatter: bundled validator reported `Skill is valid!`.
- Existing index: opened successfully and reported 1002 records.
- Protocol: `evidence/protocol-check-rerun.txt` records two successful structured searches, four rejected invalid inputs, exactly one registered tool, and unchanged saved session/status rows.
- Codex registration: `codex mcp add movie_mood` succeeded. The CLI wrote the command, args, and two environment variables; the timeout values above are suggested settings, not settings added by that command.
- Actual Codex call: `evidence/codex-mcp-working.jsonl` records a completed MCP tool call with structured results. `codex-mcp-call-trimmed.json` and `codex-mcp-response.txt` extract that evidence. Confirmed client: Codex CLI. VS Code remains unverified.
- Earlier failed attempts are retained: a subprocess approval-policy block and a startup stall. Initializing Chroma before the event loop resolved the stall in subsequent checks; an untyped dict return also needed a TypedDict to enable structuredContent in SDK v1. These are server integration issues, not a checker misfire.
- The smoke query returned weak thematic matches. The producer explicitly said the excerpts do not clearly establish a long journey; success means the tool executed honestly, not that movie relevance was established.
- A fresh read-only checker CLI session was launched separately against the implementation and evidence, using the same default model. Its transcript is `evidence/checker-initial-review.jsonl`; this is an initial review rather than either of the student's two chosen demonstrations.
- That checker completed: supported initial implementation with limited coverage; it identified unverified provenance and additional boundary tests. Its extracted actual output is `evidence/checker-initial-output.md`. It did not find a confirmed functional violation. This is not evidence of a checker misfire.

## Submission work still requiring the student

Confirm the HW3-HW7 mapping of the five prompt logs. The supplied handoff quotes
Uncharted's reload/globe issue, Crossy Road's failure after 200 points, and Movie
Mood's preference to keep everything local. These motivate behavior checks and
local reuse; they do not show that the student previously requested MCP.

Choose two real movie-discovery tasks, retain producer tool calls, and run the
checker in separate fresh sessions. Record your own agreement/disagreement.
Find a genuine checker misfire before revising v1; do not count a server bug as a
checker failure. Write the three submission documents yourself. Useful prompts:
- README: What recurring need does each component meet? What was borrowed, and why is it suitable and safe? Which clients have actually been tested?
- DEMONSTRATION: What did you ask, what did the tools return, what did the checker find, and which findings do you agree with?
- ITERATION: What specific checker judgment was wrong, why, what instruction changed, and what happened on rerun?

Do not claim unobserved demonstrations, opinions, or testing. Publish a new public
repository and submit the link only when the student explicitly instructs it.
