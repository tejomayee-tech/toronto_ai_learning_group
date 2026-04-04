import asyncio
from mcp.client.stdio import stdio_client
from mcp.client.session import ClientSession
from mcp.types import CallToolRequest

async def main():
    # Launch the server
    server_params = {
        "command": "python",
        "args": ["server.py"],
        "env": None
    }

    async with stdio_client(server_params) as (read_stream, write_stream):
        async with ClientSession(read_stream, write_stream) as session:
            # Initialize
            await session.initialize()

            # List tools
            tools = await session.list_tools()
            print("Available tools:", [tool.name for tool in tools.tools])

            # Call get_schema
            result = await session.call_tool(CallToolRequest(
                method="tools/call",
                params={
                    "name": "get_schema",
                    "arguments": {}
                }
            ))
            print("Schema:", result)

            # Call query_db
            result = await session.call_tool(CallToolRequest(
                method="tools/call",
                params={
                    "name": "query_db",
                    "arguments": {
                        "sql_query": "SELECT COUNT(*) FROM public.student"
                    }
                }
            ))
            print("Query result:", result)

if __name__ == "__main__":
    asyncio.run(main())