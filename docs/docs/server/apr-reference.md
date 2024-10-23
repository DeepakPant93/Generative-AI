---
sidebar_position: 1
---

# API Reference

## Authentication

All API endpoints require Basic Authentication. Make sure to include your credentials in the request headers.

## Endpoints

### Document Upload
```http
POST /upload
Content-Type: multipart/form-data

Parameters:
- file: File (required) - The document to upload
```

### Query Document
```http
POST /query
Content-Type: application/json

{
    "query": "string",
    "chat_history": []
}
```