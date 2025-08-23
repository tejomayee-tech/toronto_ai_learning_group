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

### Step 4: Code for `app.py` and `index.html`

Populate your files with the following code. The `index.html` file includes the Marked.js library for secure markdown rendering.

#### `C:\secure-web-llm\model\app.py`

```python
from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import ollama

app = Flask(__name__)
messages = [] 
model_name = 'llama3.2' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    messages.append({'role': 'user', 'content': user_message})

    # The generator function will yield chunks as they arrive
    def generate_stream():
        full_response_content = ""
        try:
            stream = ollama.chat(
                model=model_name,
                messages=messages,
                stream=True,  # Crucially, enable streaming
            )
            for chunk in stream:
                content = chunk['message']['content']
                if content:
                    full_response_content += content
                    yield content  # Yield the content chunk
        except Exception as e:
            yield f"Error: An unexpected error occurred: {e}"
        finally:
            messages.append({'role': 'assistant', 'content': full_response_content})

    # Return a streaming response
    return Response(stream_with_context(generate_stream()), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

#### `C:\secure-web-llm\model\templates\index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ollama Chat</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f2f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
        }
        .chat-container {
            width: 100%;
            max-width: 800px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            display: flex;
            flex-direction: column;
            height: 90vh;
            overflow: hidden;
        }
        #chat-display {
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
            border-bottom: 1px solid #ddd;
        }
        .message {
            margin-bottom: 15px;
            padding: 10px;
            border-radius: 18px;
            max-width: 80%;
            word-wrap: break-word;
        }
        .user-message {
            background-color: #007bff;
            color: white;
            margin-left: auto;
            text-align: right;
        }
        .ollama-message {
            background-color: #e9e9eb;
            color: #333;
            text-align: left;
        }
        /* Optional: Add basic styling for markdown elements */
        .ollama-message pre {
            background-color: #f6f8fa;
            border-radius: 6px;
            padding: 16px;
            overflow-x: auto;
        }
        .ollama-message code {
            font-family: 'Courier New', Courier, monospace;
        }
        #input-form {
            display: flex;
            padding: 20px;
            background-color: #fff;
        }
        #user-input {
            flex-grow: 1;
            padding: 10px;
            border-radius: 20px;
            border: 1px solid #ddd;
            font-size: 16px;
            margin-right: 10px;
        }
        #send-button {
            padding: 10px 20px;
            border: none;
            background-color: #007bff;
            color: white;
            border-radius: 20px;
            cursor: pointer;
            font-size: 16px;
        }
        #send-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="chat-container">
        <div id="chat-display">
            </div>
        <form id="input-form">
            <input type="text" id="user-input" placeholder="Type your message..." autocomplete="off">
            <button type="submit" id="send-button">Send</button>
        </form>
    </div>

    <script>
        const chatDisplay = document.getElementById('chat-display');
        const inputForm = document.getElementById('input-form');
        const userInput = document.getElementById('user-input');

        function appendMessage(sender, message) {
            const messageDiv = document.createElement('div');
            messageDiv.classList.add('message');
            messageDiv.classList.add(sender === 'user' ? 'user-message' : 'ollama-message');
            
            // This is the key line: converting markdown to HTML
            messageDiv.innerHTML = marked.parse(message);
            
            chatDisplay.appendChild(messageDiv);
            chatDisplay.scrollTop = chatDisplay.scrollHeight;
        }

        appendMessage('ollama', 'Welcome to Ollama Chat! How can I help you today?');

        inputForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const message = userInput.value.trim();
            if (!message) return;

            appendMessage('user', message);
            userInput.value = '';

            userInput.disabled = true;
            document.getElementById('send-button').disabled = true;
            appendMessage('ollama', 'Ollama is thinking...');

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message })
                });

                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }

                const data = await response.json();
                
                chatDisplay.removeChild(chatDisplay.lastChild);
                appendMessage('ollama', data.response);

            } catch (error) {
                console.error('Error:', error);
                chatDisplay.removeChild(chatDisplay.lastChild);
                appendMessage('ollama', 'Sorry, something went wrong. Please try again.');
            } finally {
                userInput.disabled = false;
                document.getElementById('send-button').disabled = false;
                userInput.focus();
            }
        });
    </script>
</body>
</html>
```

-----

### Step 5: Setup the Python Virtual Environment and Packages

This is a critical step to manage your project's dependencies.

1.  **Open your terminal** and navigate to your main project directory.
    ```bash
    cd C:\secure-web-llm
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
    cd C:\secure-web-llm\model
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