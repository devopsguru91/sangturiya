# Project Structure

This project follows an agentic system architecture. The structure is broken down into the following components:

- **`ui/`**: Frontend user interface applications and components. Handles user interactions.
- **`agent/`**: The core AI agent system logic, including reasoning, task planning, and orchestration of other components.
- **`backend/`**: General backend services, API endpoints, and business logic that supports the agent and UI.
- **`mcp/`**: Model Context Protocol implementations and server setups. Handles the interaction and providing context to AI models.
- **`db/`**: Database migrations, schemas, ORM models, and database access utilities.
- **`rag/`**: Retrieval-Augmented Generation pipeline. Contains logic for vector embeddings, document chunking, semantic search, and integration with the knowledge base.
