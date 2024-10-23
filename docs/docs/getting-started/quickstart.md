---
sidebar_position: 1
---

# System Overview

AskDocsGPT is designed to make your documentation searchable using advanced AI technology. This guide will help you understand the system components and how they work together.

## System Components

### Server Component
- Built with FastAPI
- Integrates with LangChain for document processing
- Uses Pinecone for vector storage
- Implements GPT model for query processing

### Client Component
- Built with Streamlit
- Provides chat-like interface
- Connects to server via REST API
- Handles user authentication