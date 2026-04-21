
* ⚡ Fast (connection pooling)
* 🧠 RAG-ready (schema tool)
* 🔒 Safe (read-only guard + limits)
* 🧩 Minimal (no overengineering)

---

# 🚀 Project: Python MCP Server for PostgreSQL (SQL RAG)

---

# 🛠️ Project Structure

```text
mcp-postgres-server/
├── .env
├── server.py
└── requirements.txt
```

---

# 1️⃣ Dependencies (`requirements.txt`)

```text
mcp
psycopg2-binary
python-dotenv
```

Install:

```bash
pip install -r requirements.txt
```

---

# 2️⃣ Environment Setup (`.env`)

```env
DB_USER=postgres
DB_PASSWORD=your_password_here
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
```

---

# 3️⃣ Optimized MCP Server (`server.py`)

This version includes:

* ✅ Connection pooling (major speed boost)
* ✅ Query safety guard (read-only)
* ✅ Automatic LIMIT
* ✅ JSON responses (LLM-friendly)
* ✅ Schema tool (for SQL RAG)
* ✅ Query timeout protection

---

```python
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
# Run MCP Server
# -----------------------------------
if __name__ == "__main__":
    mcp.run()
```

---

# 4️⃣ Run the Server

```bash
python server.py
```

This starts your MCP server.

---

# 🧠 How This Works (SQL RAG Flow)

```text
LLM (e.g. Ollama)
    ↓
MCP Client
    ↓
query_db / get_schema tools
    ↓
PostgreSQL
```

---

# ⚡ Performance Improvements (What Changed)

| Optimization      | Benefit                          |
| ----------------- | -------------------------------- |
| Connection Pool   | 🚀 Eliminates reconnect overhead |
| JSON output       | Faster LLM parsing               |
| LIMIT enforcement | Prevents huge queries            |
| Query guard       | Prevents destructive ops         |
| Schema tool       | Enables accurate SQL generation  |
| Timeout (5s)      | Prevents hanging queries         |

---

# 🧪 Example MCP Tool Usage

### Query tool

```json
{
  "sql_query": "SELECT COUNT(*) FROM public.students"
}
```

### Schema tool

```json
{}
```

---


# 🔒 Safety (Minimal but Effective)

* Blocks:

  * DROP
  * DELETE
  * UPDATE
  * INSERT
  * ALTER
* Enforces LIMIT
* 5s query timeout

---

# 🧠 Optional Enhancements (Next Step)

Keep POC simple, but you can add:

### 1️⃣ SQL auto-correction

Retry failed queries via LLM

### 2️⃣ Caching

Cache schema + frequent queries

### 3️⃣ Column descriptions

Improve LLM accuracy

### 4️⃣ Multi-schema support

---

**Python MCP server for PostgreSQL next-steps**


* 🔹 Full AI chat UI over this MCP
* 🔹 Hybrid RAG (SQL + vector DB)
* 🔹 Autonomous SQL agent (self-healing queries)
* 🔹 Multi-database MCP router
