"""Cloud Run entrypoint for SSE/HTTP transport."""

import os

# Cloud Run provides the port via PORT; FastMCP reads FASTMCP_* at import time.
if "PORT" in os.environ and "FASTMCP_PORT" not in os.environ:
    os.environ["FASTMCP_PORT"] = os.environ["PORT"]
if "FASTMCP_HOST" not in os.environ:
    os.environ["FASTMCP_HOST"] = "0.0.0.0"

from remarkable_mcp.server import mcp

mcp.run(transport="sse")
