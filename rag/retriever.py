class DocumentRetriever:
    def __init__(self, vector_store):
        self.vector_store = vector_store

    def retrieve(self, query: str, top_k: int = 5):
        # Implementation to fetch top_k documents
        return ["Doc 1", "Doc 2"]
