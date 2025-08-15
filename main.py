from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Basic_demo")


@mcp.tool()
def add(a:float, b:float)-> float:
    return a+b

@mcp.tool()
def subtract(a:float, b:float)-> float:
    return a-b
