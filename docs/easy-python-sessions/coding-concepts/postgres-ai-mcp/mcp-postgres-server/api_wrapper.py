#!/usr/bin/env python3
"""
Simple REST API wrapper for PostgreSQL MCP Server

This provides a simple HTTP API that wraps the MCP tools for easy integration.
"""

import os
import json
from typing import Dict, Any
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

# Import the MCP server functions directly
from server import query_db, get_schema

app = FastAPI(title="PostgreSQL MCP API", description="REST API wrapper for PostgreSQL MCP tools")

class QueryRequest(BaseModel):
    sql_query: str

class ToolResponse(BaseModel):
    success: bool
    data: Any = None
    error: str = None

@app.get("/")
async def root():
    """API root endpoint"""
    return {"message": "PostgreSQL MCP API", "tools": ["query_db", "get_schema"]}

@app.post("/query")
async def execute_query(request: QueryRequest) -> ToolResponse:
    """Execute a SQL query"""
    try:
        result = query_db(request.sql_query)
        return ToolResponse(success=True, data=result)
    except Exception as e:
        return ToolResponse(success=False, error=str(e))

@app.get("/schema")
async def get_database_schema() -> ToolResponse:
    """Get database schema"""
    try:
        result = get_schema()
        return ToolResponse(success=True, data=result)
    except Exception as e:
        return ToolResponse(success=False, error=str(e))

@app.get("/tools")
async def list_tools():
    """List available tools"""
    return {
        "tools": [
            {
                "name": "query_db",
                "description": "Execute a safe, read-only SQL query",
                "endpoint": "/query",
                "method": "POST",
                "parameters": {
                    "sql_query": "string - The SQL query to execute"
                }
            },
            {
                "name": "get_schema",
                "description": "Get database schema information",
                "endpoint": "/schema",
                "method": "GET",
                "parameters": {}
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)