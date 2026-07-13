def search_rag(query: str) -> str:
    """Tool exposed to the agent to search the knowledge base."""
    # This would call the rag module
    return f"RAG results for {query}"
