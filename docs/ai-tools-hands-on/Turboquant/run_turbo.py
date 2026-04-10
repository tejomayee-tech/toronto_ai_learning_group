import lmstudio as lms
import time

# 1. Use the Scoped Client (Zero-Config)
# This automatically finds your local daemon on Ubuntu
print("Connecting to LM Studio...")

with lms.Client() as client:
    model_path = "lmstudio-community/gemma-2-2b-it"
    
    try:
        # 2. Load with TurboQuant 3-bit cache
        print(f"Loading {model_path}...")
        model = client.llm.load_new_instance(
            model_path,
            config={
                "kv_cache": {"type": "turboquant_3bit"},
                "gpu": {"ratio": 0}  # CPU only for testing
            }
        )
        print("Model is ready!")

        # 3. Inference Test
        prompt = "Explain why TurboQuant is good for mobile devices in one sentence."
        print(f"\nPrompt: {prompt}")

        response = model.respond(prompt)
        print(f"\nAI: {response.content}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

# The connection and model instance are automatically cleaned up here