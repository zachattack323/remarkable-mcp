"""Cloud Run entrypoint for SSE/HTTP transport."""

import os

# Cloud Run provides the port via PORT; FastMCP reads FASTMCP_* at import time.
os.environ["FASTMCP_PORT"] = os.environ.get("PORT", "8080")
os.environ["FASTMCP_HOST"] = "0.0.0.0"

from remarkable_mcp.server import mcp

mcp.run(transport="sse")
