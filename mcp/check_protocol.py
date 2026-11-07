"""Exercise actual stdio transport, validation, repeat calls, and user-state preservation."""
import asyncio
import json
import os
from pathlib import Path
import sqlite3
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


def state():
    path = Path(os.environ["MOVIE_MOOD_HOME"]) / "user.sqlite3"
    with sqlite3.connect(path.as_uri() + "?mode=ro", uri=True) as db:
        return {table: db.execute(f"SELECT * FROM {table} ORDER BY 1").fetchall()
                for table in ("status", "session")}


async def main():
    before = state()
    params = StdioServerParameters(command=sys.executable, args=[str(Path(__file__).with_name("server.py"))], env=dict(os.environ))
    async with stdio_client(params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()
            names = [t.name for t in (await session.list_tools()).tools]
            assert names == ["search_movies"], names
            for args in ({"query": " "}, {"query": "friendship", "limit": 0},
                         {"query": "friendship", "limit": True}, {"query": 3}):
                result = await session.call_tool("search_movies", args)
                assert result.isError, args
            for _ in range(2):
                result = await session.call_tool("search_movies", {"query": "an unlikely friendship on a long journey", "limit": 2})
                assert not result.isError, result
                data = result.structuredContent
                assert data and data["results"], result
                assert all(r["id"] and r["title"] and r["plot_evidence"] for r in data["results"])
                print(json.dumps(data, ensure_ascii=True))
    assert state() == before, "Saved user state changed"
    print("PASS: one tool; invalid inputs rejected; two real searches; user state unchanged")


if __name__ == "__main__":
    asyncio.run(main())
