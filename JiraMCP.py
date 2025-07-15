import os

from fastmcp import FastMCP

mcp = FastMCP("MyMCPServer", host="localhost", port=8000)

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the MCP server."

if __name__ == "__main__":
    mcp.run(transport="sse")