from fastmcp import FastMCP

# Give your MCP server a name
mcp = FastMCP("MyMCPServer")


@mcp.tool()
def greet(name: str) -> str:
    return f"Hello, {name}! Welcome to the MCP server."

if __name__ == "__main__":
    mcp.run()
