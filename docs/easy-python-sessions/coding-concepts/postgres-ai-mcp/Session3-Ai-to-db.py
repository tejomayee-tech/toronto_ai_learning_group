# pip install sqlalchemy psycopg2-binary langchain langchain-ollama python-dotenv

import os
from psycopg2.extras import RealDictCursor
from psycopg2.pool import SimpleConnectionPool
import psycopg2
from langchain_ollama import ChatOllama

# 1. Database Credentials (use env vars or defaults)
USER = os.getenv("DB_USER", "postgres")
PASSWORD = os.getenv("DB_PASSWORD", "<>")
HOST = os.getenv("DB_HOST", "localhost")
PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "postgres")

# 2. Connection Pool
pool = SimpleConnectionPool(
    1, 10,
    user=USER,
    password=PASSWORD,
    host=HOST,
    port=PORT,
    dbname=DB_NAME,
    options="-c statement_timeout=5000"
)

# Helper: enforce LIMIT
def enforce_limit(sql: str) -> str:
    if "limit" not in sql.lower():
        return sql.rstrip(";") + " LIMIT 50;"
    return sql

# Helper: block unsafe queries
def is_safe_query(sql: str) -> bool:
    blocked = ["drop", "delete", "truncate", "update", "insert", "alter"]
    return not any(word in sql.lower() for word in blocked)

# 3. Database helpers
def query_db(sql_query: str) -> dict:
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
                return {"rows": rows, "count": len(rows)}
            return {"message": "Query executed successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if conn:
            pool.putconn(conn)


def get_schema() -> str:
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
            return str(schema)
    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        if conn:
            pool.putconn(conn)


# 4. Setup AI
llm = ChatOllama(model="phi3", temperature=0)


def extract_text(response) -> str:
    content = getattr(response, "content", response)
    if isinstance(content, list):
        return "".join(str(item) for item in content)
    return str(content)


def generate_sql(question: str, schema: str) -> str:
    prompt = (
        "You are an expert SQL assistant. Use the schema below to write a safe SELECT query for PostgreSQL. "
        "Do not use INSERT/UPDATE/DELETE/ALTER/TRUNCATE/DROP. "
        "how many students are there with firstname vijay in student table, ignore case.\n\n"
        f"Schema:\n{schema}\n\n"
        f"User question: {question}\nSQL:"
    )
    response = llm.invoke(prompt)
    sql = extract_text(response).strip()
    # Remove markdown code blocks if present
    if sql.startswith("```"):
        sql = sql.split("```")[1]
        if sql.startswith("sql"):
            sql = sql[3:].strip()
    # Keep only the first SQL statement if the model returns extra text.
    if ";" in sql:
        sql = sql.split(";")[0] + ";"
    return sql


def run_question(question: str) -> None:
    schema = get_schema()
    print("Schema summary:\n", schema)
    sql = generate_sql(question, schema)
    print("Generated SQL:\n", sql)
    result = query_db(sql)
    print("Query result:\n", result)


if __name__ == "__main__":
    run_question("How many students are present in table public.student")