# Project Structure

This project follows an agentic system architecture for the Sangturiya AI assistant. The structure is broken down into the following components:

- **`backend/`**: General backend services, API endpoints, and business logic.
  - `main.py`: Entry point for FastAPI application.
  - `api/`: API route definitions.
  - `core/`: Core configurations and utilities.
- **`agent/`**: The core AI agent system logic, including reasoning and orchestration.
  - `chatbot.py`: Core logic for processing interactions.
  - `mcp_client.py`: Client to connect to Model Context Protocol servers to fetch context.
  - `prompts.py`: System prompts and LLM instruction templates.
- **`mcp/`**: Model Context Protocol implementations and server setups.
  - `server.py`: MCP server implementation exposing tools and resources.
  - `tools.py`: Tool definitions exposed via MCP.
- **`rag/`**: Retrieval-Augmented Generation pipeline.
  - `retriever.py`: Logic to retrieve relevant documents.
  - `ingest.py`: Logic to ingest and chunk documents.
  - `embeddings.py`: Utilities for generating embeddings.
- **`db/`**: Database migrations, schemas, and connection utilities.
  - `models.py`: Database schema definitions (e.g., SQLAlchemy models).
  - `session.py`: Database connection and session management.
- **`ui/`**: Frontend user interface applications and components.
  - `app.py`: Streamlit application serving as the primary UI.
