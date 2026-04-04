import os
import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

# -----------------------------------
# Load environment variables
# -----------------------------------
load_dotenv()

# -----------------------------------
# Initialize MCP Server
# -----------------------------------
mcp = FastMCP("Postgres-Local")

# -----------------------------------
# Connection Pool (performance boost)
# -----------------------------------
pool = SimpleConnectionPool(
    1, 10,
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    dbname=os.getenv("DB_NAME"),
    options="-c statement_timeout=5000"  # 5 sec timeout
)

# -----------------------------------
# Helper: enforce LIMIT
# -----------------------------------
def enforce_limit(sql: str) -> str:
    if "limit" not in sql.lower():
        return sql.rstrip(";") + " LIMIT 50;"
    return sql

# -----------------------------------
# Helper: block unsafe queries
# -----------------------------------
def is_safe_query(sql: str) -> bool:
    blocked = ["drop", "delete", "truncate", "update", "insert", "alter"]
    return not any(word in sql.lower() for word in blocked)

# -----------------------------------
# Tool 1: Execute SQL
# -----------------------------------
@mcp.tool()
def query_db(sql_query: str) -> dict:
    """
    Executes a safe, read-only SQL query.
    Returns structured JSON.
    """

    if not is_safe_query(sql_query):
        return {"error": "Only SELECT queries are allowed"}

    sql_query = enforce_limit(sql_query)

    conn = None

    try:
        conn = pool.getconn()

        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(sql_query)

            if cur.description:
                rows = cur.fetchall()
                return {
                    "rows": rows,
                    "count": len(rows)
                }
            else:
                return {"message": "Query executed successfully"}

    except Exception as e:
        return {"error": str(e)}

    finally:
        if conn:
            pool.putconn(conn)

# -----------------------------------
# Tool 2: Get Schema (SQL RAG)
# -----------------------------------
@mcp.tool()
def get_schema() -> dict:
    """
    Returns database schema for LLM grounding.
    """

    conn = None

    try:
        conn = pool.getconn()

        with conn.cursor() as cur:
            cur.execute("""
                SELECT table_name, column_name, data_type
                FROM information_schema.columns
                WHERE table_schema = 'public'
                ORDER BY table_name;
            """)

            rows = cur.fetchall()

            schema = {}
            for table, column, dtype in rows:
                schema.setdefault(table, []).append({
                    "column": column,
                    "type": dtype
                })

            return schema

    except Exception as e:
        return {"error": str(e)}

    finally:
        if conn:
            pool.putconn(conn)

# -----------------------------------
# Run MCP Server with Streamable HTTP Transport
# -----------------------------------
if __name__ == "__main__":
    # Run with streamable HTTP transport for web API access
    mcp.run(transport="streamable-http")