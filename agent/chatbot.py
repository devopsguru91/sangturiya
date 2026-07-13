class AgenticChatbot:
    def __init__(self, mcp_client):
        self.mcp_client = mcp_client

    def generate_response(self, user_input: str) -> str:
        # Example logic: Get context from MCP, then generate response
        context = self.mcp_client.get_context(user_input)
        return f"Response based on context: {context}"
