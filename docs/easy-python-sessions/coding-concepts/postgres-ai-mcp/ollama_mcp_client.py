#!/usr/bin/env python3
"""
MCP Client for Ollama - Connects PostgreSQL MCP Server to Ollama LLM

This script creates an MCP client that connects to your PostgreSQL MCP server
and provides the tools to Ollama through LangChain for database queries.
"""

import asyncio
import json
import os
import subprocess
import sys
from typing import Any, Dict, List, Optional

import requests
from langchain_core.tools import BaseTool
from langchain_ollama import ChatOllama
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel, Field


class MCPTool(BaseTool):
    """LangChain tool wrapper for MCP server tools"""

    name: str = Field(description="Tool name")
    description: str = Field(description="Tool description")
    api_endpoint: str = Field(description="API endpoint URL")
    method: str = Field(description="HTTP method")

    def __init__(self, name: str, description: str, api_endpoint: str, method: str = "POST"):
        super().__init__(name=name, description=description)
        self.api_endpoint = api_endpoint
        self.method = method

    def _run(self, **kwargs) -> str:
        """Execute the tool via REST API"""
        try:
            if self.method == "GET":
                response = requests.get(self.api_endpoint)
            elif self.method == "POST":
                response = requests.post(self.api_endpoint, json=kwargs)
            else:
                return f"Unsupported HTTP method: {self.method}"

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    return json.dumps(result.get("data", {}), indent=2)
                else:
                    return f"API Error: {result.get('error', 'Unknown error')}"
            else:
                return f"HTTP Error: {response.status_code} - {response.text}"

        except Exception as e:
            return f"Error executing tool {self.name}: {str(e)}"


class OllamaMCPClient:
    """MCP Client that integrates with Ollama"""

    def __init__(self, api_base_url: str = "http://localhost:8001", ollama_model: str = "llama3.1"):
        self.api_base_url = api_base_url
        self.ollama_model = ollama_model
        self.tools = []
        self.llm = ChatOllama(model=ollama_model, temperature=0.1)

    def start_api_server(self):
        """Start the API wrapper server"""
        try:
            # Import here to avoid circular imports
            import subprocess
            import sys

            # Start the API wrapper server
            self.api_process = subprocess.Popen(
                [sys.executable, "mcp-postgres-server/api_wrapper.py"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )

            # Wait a moment for server to start
            import time
            time.sleep(2)

            print("API wrapper server started successfully")

        except Exception as e:
            print(f"Failed to start API server: {e}")
            raise

    def discover_tools(self) -> List[MCPTool]:
        """Discover available tools from API server"""
        try:
            # Get tools from API
            response = requests.get(f"{self.api_base_url}/tools")

            if response.status_code == 200:
                tools_data = response.json()
                tools = []

                for tool_info in tools_data.get("tools", []):
                    tool = MCPTool(
                        name=tool_info["name"],
                        description=tool_info["description"],
                        api_endpoint=f"{self.api_base_url}{tool_info['endpoint']}",
                        method=tool_info["method"]
                    )
                    tools.append(tool)

                print(f"Discovered {len(tools)} tools: {[t.name for t in tools]}")
                return tools
            else:
                print(f"Failed to list tools: {response.status_code}")
                return []

        except Exception as e:
            print(f"Error discovering tools: {e}")
            return []

    def create_agent(self):
        """Create LangChain agent with MCP tools"""
        self.tools = self.discover_tools()

        if not self.tools:
            print("No tools discovered, creating agent without tools")
            return None

        # Create prompt template
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are a helpful AI assistant with access to a PostgreSQL database through MCP tools.

You have access to the following tools:
{tools}

Use the tools to help answer questions about the database. Always use the query_db tool for SQL queries, and get_schema to understand the database structure.

When writing SQL queries:
- Use SELECT statements only (read-only access)
- Limit results to avoid large outputs
- Use proper table and column names
- Be specific in your queries

Format your responses clearly and explain what you're doing."""),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ])

        # Create agent
        agent = create_tool_calling_agent(self.llm, self.tools, prompt)
        agent_executor = AgentExecutor(
            agent=agent,
            tools=self.tools,
            verbose=True,
            handle_parsing_errors=True
        )

        return agent_executor

    def chat(self, query: str) -> str:
        """Process a user query"""
        if not hasattr(self, 'agent') or self.agent is None:
            self.agent = self.create_agent()
            if self.agent is None:
                return "Failed to create agent - no tools available"

        try:
            result = self.agent.invoke({"input": query})
            return result["output"]
        except Exception as e:
            return f"Error processing query: {str(e)}"

    def close(self):
        """Clean up resources"""
        if hasattr(self, 'api_process') and self.api_process:
            self.api_process.terminate()
            self.api_process.wait()
            print("API server stopped")


def main():
    """Main interactive loop"""
    print("🚀 Starting Ollama MCP Client for PostgreSQL")
    print("=" * 50)

    # Initialize client
    client = OllamaMCPClient(
        api_base_url="http://localhost:8001",
        ollama_model="llama3.1"
    )

    try:
        # Start API server
        print("Starting API wrapper server...")
        client.start_api_server()

        # Create agent
        print("Creating AI agent with database tools...")
        agent = client.create_agent()

        if agent is None:
            print("❌ Failed to create agent")
            return

        print("✅ Setup complete! You can now query your database.")
        print("Type 'quit' to exit, 'schema' to see database structure.")
        print("-" * 50)

        while True:
            try:
                user_input = input("\n💬 You: ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    break
                elif user_input.lower() == 'schema':
                    result = client.chat("Show me the database schema")
                    print(f"\n🤖 AI: {result}")
                elif user_input:
                    result = client.chat(user_input)
                    print(f"\n🤖 AI: {result}")

            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"❌ Error: {e}")

    except Exception as e:
        print(f"❌ Setup failed: {e}")
    finally:
        client.close()
        print("\n👋 Goodbye!")


if __name__ == "__main__":
    main()