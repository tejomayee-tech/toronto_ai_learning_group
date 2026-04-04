#!/bin/bash
# Quick start script for Ollama MCP PostgreSQL integration

echo "🚀 Starting Ollama MCP PostgreSQL Integration"
echo "=============================================="

# Check if Ollama is running
if ! pgrep -x "ollama" > /dev/null; then
    echo "⚠️  Ollama is not running. Starting it..."
    ollama serve &
    sleep 3
fi

# Check if the model is available
if ! ollama list | grep -q "llama3.1"; then
    echo "📥 Pulling llama3.1 model..."
    ollama pull llama3.1
fi

# Install dependencies if needed
if [ ! -d ".venv" ]; then
    echo "📦 Setting up virtual environment..."
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
else
    source .venv/bin/activate
fi

# Check database connection
echo "🔍 Checking database connection..."
python3 -c "
import os
from dotenv import load_dotenv
load_dotenv('mcp-postgres-server/.env')
import psycopg2
try:
    conn = psycopg2.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        dbname=os.getenv('DB_NAME')
    )
    conn.close()
    print('✅ Database connection successful')
except Exception as e:
    print(f'❌ Database connection failed: {e}')
    exit(1)
"

echo ""
echo "🎯 Starting interactive AI database assistant..."
echo "Type your questions in natural language!"
echo "Examples:"
echo "  - 'How many records are in the users table?'"
echo "  - 'Show me the database schema'"
echo "  - 'Find all products with price > 100'"
echo ""
echo "Type 'quit' to exit"
echo ""

# Run the client
python3 ollama_mcp_client.py