# Example placeholder for MCP SDK
# from mcp.server.fastmcp import FastMCP

# mcp = FastMCP("Sangturiya")

class MockMCPServer:
    def __init__(self, name: str):
        self.name = name
        self.tools = []

    def register_tool(self, tool_func):
        self.tools.append(tool_func)

mcp = MockMCPServer("Sangturiya")

# In real usage:
# @mcp.tool()
# def search_rag(query: str) -> str:
#     pass
