# pip install sqlalchemy psycopg2-binary langchain langchain-community langchain-ollama

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_ollama import ChatOllama
import urllib.parse

# 1. Database Credentials
USER = "postgres"
PASSWORD = "<password>"  # The '@' here needs encoding, save password in system environment variables and read.
HOST = "localhost"
PORT = "5432"
DB_NAME = "postgres"

# This line is CRITICAL: it converts 'Admin@123' to 'Admin%40123'
safe_password = urllib.parse.quote_plus(PASSWORD)

# 2. Build the URI using the safe_password
db_uri = f"postgresql+psycopg2://{USER}:{safe_password}@{HOST}:{PORT}/{DB_NAME}"
db_obj = SQLDatabase.from_uri(db_uri)

# 3. Setup AI
llm = ChatOllama(model="llama3.1", temperature=0)

# 4. Initialize Agent
sql_agent_executor = create_sql_agent(llm, db=db_obj, verbose=True)

# 5. Run Query
response = sql_agent_executor.invoke({
    "input": "How many students are present in table public.student"
})

print(response["output"])