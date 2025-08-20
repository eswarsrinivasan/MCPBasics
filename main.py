import asyncio
from mcp.server.fastmcp import FastMCP
from browser_manager import BrowserManager
import atexit

mcp = FastMCP("Basic_demo")

class SeleniumAgentTools:
    def __init__(self):
        self.browser = BrowserManager()

    async def open_url(self, url: str) -> str:
        return await self.browser.open_url(url)

    async def get_title(self) -> str:
        return await self.browser.get_title()
    
    async def click(self, ID : str) -> str:
        return await self.browser.click(ID)
    
    async def send_keys(self, ID: str, value: str):
        return await self.browser.send_keys(ID,value)

    def shutdown(self):
        self.browser.stop_browser()

agent = SeleniumAgentTools()

@mcp.tool()
async def open_url(url: str) -> str:
    """Opens the browser and navigates to given webpage"""
    return await agent.open_url(url)

@mcp.tool()
async def get_title() -> str:
    """gets the title of the current page"""
    return await agent.get_title()

@mcp.tool()
async def click(ID: str):
    """Clicks on the element identified using ID"""
    return await agent.click(ID)

@mcp.tool()
async def send_keys(ID: str, value: str):
    """Inserts value to the element identified using ID"""
    return await agent.send_keys(ID, value)

@mcp.tool()
def quit_browser():
    """Closes the browser"""
    return agent.shutdown()

atexit.register(agent.shutdown)

if __name__ == "__main__":
    asyncio.run(mcp.run(transport="stdio"))
