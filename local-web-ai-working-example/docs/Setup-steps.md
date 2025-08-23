## Local Web AI Working Example


### Step 1: Install Ollama

First, you need to install and set up the Ollama server, which runs the LLMs locally on your machine.

1.  Go to the official Ollama website at **ollama.ai**.
2.  Download the appropriate installer for your operating system (Windows, macOS, or Linux).
3.  Run the installer and follow the on-screen instructions.


#### using Ollama directly

1. Open ollama from windows start menu
2. Select a model and say hi, it will start downoading the model
3. Once download is complete you can start taking to it

>**Note:** This interface is provided by ollama, we can run more controlled and we based AI assistant app with further steps below. It show how easy it becomes with just a tiny bit of effort.

-----

### Step 2: Install the LLM and Check Installation

After installing Ollama, you need to download the language model you want to use.

1.  Open your terminal (e.g., Command Prompt on Windows).
2.  Run the `ollama pull` command to download the **Llama 3.2** model.
    ```bash
    ollama pull llama3.2
    ```
    This may take some time depending on your internet speed.
3.  Verify that the model is installed by listing all local models.
    ```bash
    ollama list
    ```
    You should see `llama3.2` in the output.

-----

### Step 3: Project Setup and File Structure

Next, create the necessary folders and files for your Flask application. The structure is crucial for Flask to correctly find your templates.

```
Project.
└───local-web-ai-working-example
    │
    └───model
        │   app.py
        │
        └───templates
                index.html
```

-----
### Step 4: Clone Repo

1. create an accont on github.com and create a token or passowrd (for help see: https://youtu.be/J-CSiw5CFWE?si=f2pJlK0l2zZO6YHF) 
2. Run below command by right clicking in any folder of your computer and select open terminal here. In the command window paste the below text and hit enter.

```bash

git clone https://github.com/tejomayee-tech/toronto_ai_learning_group.git

```

3. Now you have access to sharing group library. 

### Step 5: Setup the Python Virtual Environment and Packages

This is a critical step to manage your project's dependencies.

1.  **Open your terminal** and navigate to your main project directory.
    ```bash
    cd C:\local-web-ai-working-example
    ```
2.  **Create and activate a virtual environment**.
    ```bash
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
    Your terminal prompt should now be prefixed with `(.venv)`.
3.  **Install the required packages** with a single command.
    ```bash
    pip install Flask ollama
    ```

-----

### Step 6: Run the Application

With all the files and dependencies in place, you are ready to run your application.

1.  **Start the Ollama server.** If it's not already running as a background service, open a **separate terminal** and run:
    ```bash
    ollama serve
    ```
2.  **Go to your project's `model` directory.**
    ```bash
    cd C:\local-web-ai-working-example\model
    ```
3.  **Run the Flask application.**
    ```bash
    flask --app app.py run
    ```
4.  **Open your web browser** and navigate to `http://127.0.0.1:5000`. You should see your chat application.

### Step 7: View Running LLM

>![Run](/docs/run.png)

>![working screen](/docs/working-local-llm.png)


### Step 8: Basic check on privacy

>![local-llm](/docs/test-local-llm.png)


>![gemini](/docs/Gemini.png)