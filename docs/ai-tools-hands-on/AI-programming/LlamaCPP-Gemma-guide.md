# Llama CPP - Gemma - Setup

## 🛠️ Project Setup: Local RAG with Gemma (GGUF)

### Prerequisites

1.  **Python 3.8+**
2.  **A GGUF Model:** Download a light instruction-tuned Gemma model (e.g., `gemma-2b-it-q4_k_m.gguf`). You can find these on the Hugging Face model hub, often in repositories like **TheBloke** or **Gemma GGUF official repos**.
      * **Action:** Place the downloaded `.gguf` file in your project directory and rename it to `gemma-2b.gguf` for simplicity.

### Step 1: Install Required Libraries

We need `llama-cpp-python` for the LLM, `LangChain` for the RAG chain, `Chroma` for the vector store, and `Sentence Transformers` for the embedding model.

```bash
pip install llama-cpp-python langchain langchain-community chromadb sentence-transformers
```

### Step 📄 Step 2: Create a Sample Knowledge Base

For this tutorial, let's create a single text file that represents our custom knowledge.

Create a file named **`data/corporate_policy.txt`** and fill it with the following text:

```text
The current remote work policy (as of January 1, 2025) states that all employees are required to be in the office on Tuesdays and Thursdays. All other days (Monday, Wednesday, and Friday) are flexible and can be worked remotely.

For vacation requests, employees must submit a request through the internal HR portal at least 14 days in advance. Last-minute requests (less than 7 days) require explicit approval from the departmental Vice President.

The company's official lunch stipend is $15 per day, which can be used for any food or beverage purchase made between 11:30 AM and 2:00 PM local time. Unused stipends do not roll over to the next day.
```

### Step 🔄 Step 3: Build the RAG Pipeline (Code)

Create a Python file named **`gemma_rag.py`** and follow the steps in the code comments.

#### `gemma_rag.py`

```python
import os
from llama_cpp import Llama
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# --- Configuration ---
MODEL_PATH = "gemma-2b.gguf" # Make sure this matches your downloaded file name
KNOWLEDGE_FILE = "data/corporate_policy.txt"
VECTOR_DB_DIR = "./chroma_db"

# 1. Load the Model (llama-cpp-python)
print("--- 1. Loading Gemma 2B (GGUF) via llama-cpp-python ---")
try:
    # Instantiate the Llama object. n_gpu_layers=0 forces CPU inference.
    # Set model_kwargs to use Gemma's specific chat format.
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=4096,           # Context window
        n_threads=8,          # CPU threads to use
        n_gpu_layers=0,       # Set to -1 to use GPU if available and installed correctly
        chat_format="gemma",  # Important for correct instruction formatting
        verbose=False
    )
    print("Model loaded successfully.")
except FileNotFoundError:
    print(f"ERROR: Model file not found at {MODEL_PATH}. Please download it first.")
    exit()

# 2. Ingest Data (Load, Split, Embed)
print("--- 2. Ingesting Corporate Policy Data ---")
os.makedirs(os.path.dirname(KNOWLEDGE_FILE), exist_ok=True)
if not os.path.exists(KNOWLEDGE_FILE):
    print(f"Creating sample data file: {KNOWLEDGE_FILE}")
    # (The sample data creation is skipped here, assume the file exists from Step 2)

# Load the document
loader = TextLoader(KNOWLEDGE_FILE)
documents = loader.load()

# Split the document into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
texts = text_splitter.split_documents(documents)

# Create an embedding model (This will be used to generate vector representations)
print("Loading Embedding Model...")
# Using a small, efficient model for local embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Create and persist the vector store (ChromaDB)
# This step embeds the text chunks and stores them locally
print(f"Creating Vector Store in {VECTOR_DB_DIR}...")
vectorstore = Chroma.from_documents(
    documents=texts,
    embedding=embeddings,
    persist_directory=VECTOR_DB_DIR
)
vectorstore.persist() # Save the database to disk
print("Vector Store created and persisted.")

# 3. Create the Retrieval Chain
# We wrap the llama-cpp-python LLM using LangChain's wrapper
from langchain_community.llms import LlamaCpp

langchain_llm = LlamaCpp(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_gpu_layers=0,
    temperature=0.1,
    verbose=False,
    model_kwargs={"chat_format": "gemma"}
)

# Create the RetrievalQA chain
# This chain automatically: 
# 1. Takes the user question
# 2. Uses the retriever to find relevant chunks
# 3. Puts the chunks and question into a final prompt
# 4. Sends the prompt to the LLM
rag_chain = RetrievalQA.from_chain_type(
    llm=langchain_llm,
    chain_type="stuff", # 'stuff' puts all context into one large prompt
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}), # retrieve top 2 chunks
    return_source_documents=False # set to True to see the source text
)

# 4. Run the End-to-End Query
print("\n--- 3. Running Retrieval-Augmented Query ---")

question_1 = "When am I required to be in the office and what is the maximum food budget?"
question_2 = "What is the policy for submitting an urgent vacation request?"

print(f"\nQUERY 1: {question_1}")
result_1 = rag_chain.invoke({"query": question_1})
print("RESPONSE 1:")
print(result_1['result'].strip())

print(f"\nQUERY 2: {question_2}")
result_2 = rag_chain.invoke({"query": question_2})
print("RESPONSE 2:")
print(result_2['result'].strip())
```

### Step ▶️ Step 4: Execute the Code

Run the Python script from your terminal:

```bash
python gemma_rag.py
```

### Expected Output

You will see output showing the steps, and the final results will be answers that are **grounded in the text you provided** in `corporate_policy.txt`, demonstrating the end-to-end RAG workflow.

```
--- 1. Loading Gemma 2B (GGUF) via llama-cpp-python ---
Model loaded successfully.
--- 2. Ingesting Corporate Policy Data ---
Creating Vector Store in ./chroma_db...
Vector Store created and persisted.

--- 3. Running Retrieval-Augmented Query ---

QUERY 1: When am I required to be in the office and what is the maximum food budget?
RESPONSE 1:
You are required to be in the office on Tuesdays and Thursdays. The official lunch stipend is $15 per day, which can be used between 11:30 AM and 2:00 PM.

QUERY 2: What is the policy for submitting an urgent vacation request?
RESPONSE 2:
Last-minute vacation requests (less than 7 days in advance) require explicit approval from the departmental Vice President. All requests should be submitted through the internal HR portal at least 14 days in advance.
```

This guide demonstrates a complete, Python-native workflow that uses your local GGUF model (`Gemma`) for a real-world task (`RAG`) without relying on external model servers.

Would you like to explore how to stream the LLM response instead of waiting for the full output?