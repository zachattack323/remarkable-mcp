"""Cloud Run entrypoint for SSE/HTTP transport."""

import os

# Cloud Run provides the port via PORT; FastMCP reads FASTMCP_* at import time.
os.environ["FASTMCP_PORT"] = os.environ.get("PORT", "8080")
os.environ["FASTMCP_HOST"] = "0.0.0.0"
# Avoid Cloud Run edge conflicts on /sse by using a custom SSE path.
os.environ.setdefault("FASTMCP_SSE_PATH", "/mcp/sse")
os.environ.setdefault("FASTMCP_MESSAGE_PATH", "/mcp/messages/")

from remarkable_mcp.server import mcp

# Ensure FastMCP binds to Cloud Run's host/port even if env parsing is skipped.
mcp.settings.host = "0.0.0.0"
mcp.settings.port = int(os.environ.get("PORT", "8080"))

mcp.run(transport="sse")
