import threading
import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.constants import *
import ollama

OLLAMA_HOST = "http://localhost:11434"
DEFAULT_MODEL = "llama3.1:8b"


class ChatManager:
    def __init__(self):
        self.history = []

    def add_user(self, message):
        self.history.append({"role": "user", "content": message})

    def add_assistant(self, message):
        self.history.append({"role": "assistant", "content": message})

    def build_prompt(self):
        prompt = ""
        for msg in self.history:
            prompt += f"{msg['role'].upper()}: {msg['content']}\n"
        prompt += "ASSISTANT: "
        return prompt


class OllamaClient:
    def __init__(self, model=DEFAULT_MODEL):
        self.model = model
        self.client = ollama.Client(host=OLLAMA_HOST)

    def generate(self, prompt):
        result = self.client.generate(
            model=self.model,
            prompt=prompt,
            stream=False
        )
        return result["response"]


class OllamaChatGUI:
    def __init__(self):
        self.window = ttk.Window(
            title="Ollama Chat (Local LLM)",
            themename="cyborg",
            size=(900, 600)
        )

        self.chat_manager = ChatManager()
        self.llm = OllamaClient()

        self.build_ui()

    def build_ui(self):
        self.chat_box = ScrolledText(
            master=self.window,
            wrap="word",
            padding=10,
            autohide=True
        )
        self.chat_box.pack(fill=BOTH, expand=YES, padx=10, pady=10)

        # Detect older or newer ttkbootstrap versions
        if hasattr(self.chat_box, "text"):
            self.text_widget = self.chat_box.text
        else:
            self.text_widget = self.chat_box

        # Disable user editing
        try:
            self.text_widget.configure(state="disabled")
        except:
            pass

        bottom = ttk.Frame(self.window)
        bottom.pack(fill=X, padx=10, pady=5)

        self.entry = ttk.Entry(bottom)
        self.entry.pack(side=LEFT, fill=X, expand=YES, padx=(0, 10))
        self.entry.bind("<Return>", self.send_message)

        send_btn = ttk.Button(bottom, text="Send", bootstyle=PRIMARY, command=self.send_message)
        send_btn.pack(side=RIGHT)

    def send_message(self, event=None):
        msg = self.entry.get().strip()
        if not msg:
            return

        self.entry.delete(0, END)

        self.append_text(f"You: {msg}\n")
        self.chat_manager.add_user(msg)

        threading.Thread(target=self.process_llm, daemon=True).start()

    def process_llm(self):
        prompt = self.chat_manager.build_prompt()
        reply = self.llm.generate(prompt)

        self.chat_manager.add_assistant(reply)
        self.append_text(f"Assistant: {reply}\n")

    def append_text(self, text):
        # Temporarily enable editing
        try:
            self.text_widget.configure(state="normal")
        except:
            pass

        self.text_widget.insert(END, text)

        try:
            self.text_widget.configure(state="disabled")
        except:
            pass

        self.text_widget.see(END)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    app = OllamaChatGUI()
    app.run()
