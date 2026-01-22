"""Cloud Run entrypoint for SSE/HTTP transport."""

import os

from remarkable_mcp.server import mcp


# Cloud Run provides the port via PORT; FastMCP reads FASTMCP_PORT
if "PORT" in os.environ and "FASTMCP_PORT" not in os.environ:
    os.environ["FASTMCP_PORT"] = os.environ["PORT"]

mcp.run(transport="sse")
