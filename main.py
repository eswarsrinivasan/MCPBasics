from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Basic_demo")


@mcp.tool()
def add(a:float, b:float)-> float:
    """returns sum of the numbers"""
    return a+b

@mcp.tool()
def subtract(a:float, b:float)-> float:
    """returns remaining of the numbers"""
    return a-b
