from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)
# Global list to store conversation history
messages = [] 
model_name = 'llama3.2' 

@app.route('/')
def index():
    """Serves the main HTML chat page."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handles chat messages from the user and sends them to Ollama."""
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    messages.append({'role': 'user', 'content': user_message})

    try:
        response_stream = ollama.chat(
            model=model_name,
            messages=messages,
            stream=False
        )
        
        ollama_response = response_stream['message']['content']
        messages.append({'role': 'assistant', 'content': ollama_response})

        return jsonify({"response": ollama_response})

    except ollama.ResponseError as e:
        error_msg = f"Ollama Error: {e.error}"
        print(error_msg)
        return jsonify({"error": error_msg}), 500
    except Exception as e:
        error_msg = f"An unexpected error occurred: {e}"
        print(error_msg)
        return jsonify({"error": error_msg}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)