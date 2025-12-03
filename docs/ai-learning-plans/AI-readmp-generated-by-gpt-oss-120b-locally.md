## Quick‑Start Learning Plan  
**Goal:** Be able to **design, train, evaluate, and deploy** locally‑run AI/ML models (LLMs, vision, tabular, etc.) using Python, and to build reproducible **workflows/pipelines** that can be run on a personal laptop or a modest workstation.

**learning roadmap**

| Week | Focus | Key Topics & Milestones | Resources / Tools |
|------|-------|--------------------------|-------------------|
| **1️⃣ Foundations (7 days)** | Python for data‑science + basic math | • Python syntax, virtual environments (`venv`/`conda`)  <br>• Numpy & pandas basics  <br>• Linear‑algebra refresher (vectors, matrices)  <br>• Gradient‑descent intuition | • “Python Crash Course” – 2‑hour video series (YouTube)  <br>• Official docs: <https://numpy.org/doc/>, <https://pandas.pydata.org/docs/>  <br>• Khan Academy Linear Algebra |
| **2️⃣ Core ML Stack (7 days)** | Scikit‑learn & model lifecycle | • Load / clean data, train‑test split  <br>• Supervised models (linear regression, decision trees, SVM)  <br>• Model evaluation (cross‑val, metrics)  <br>• Persistence with `joblib` / `pickle` | • Scikit‑learn tutorial: <https://scikit-learn.org/stable/tutorial/basic/tutorial.html> |
| **3️⃣ Deep Learning Basics (7 days)** | PyTorch (or TensorFlow) fundamentals | • Tensors, autograd, simple NN  <br>• Training loop, loss functions, optimizers  <br>• Saving & loading checkpoints  <br>• GPU vs CPU usage (`torch.cuda.is_available()`) | • “Deep Learning with PyTorch: A 60‑Minute Blitz” (official)  <br>• Fast.ai free course – Lesson 1 |
| **4️⃣ Local LLMs & Vision Models (10 days)** | Running pre‑trained transformer models offline | • Install `transformers`, `accelerate`  <br>• Load a small model (e.g., Llama‑2‑7B‑Chat quantized with GGML, or Mistral‑7B)  <br>• Inference script: tokenization → generation  <br>• Simple fine‑tuning via LoRA (PEFT) on a toy dataset | • Hugging Face docs – `transformers` quickstart  <br>• `llama.cpp` repo for GGML quantized models  <br>• PEFT tutorial: <https://github.com/huggingface/peft> |
| **5️⃣ Data & Experiment Management (7 days)** | Versioning data, configs, results | • `git` + DVC for datasets  <br>• `hydra` or `OmegaConf` for config files  <br>• Logging with MLflow (local server)  <br>• Reproducible random seeds | • DVC tutorial: <https://dvc.org/doc/start>  <br>• MLflow quickstart: <https://www.mlflow.org/docs/latest/tutorial.html> |
| **6️⃣ Workflow / Pipeline Automation (7 days)** | Building repeatable pipelines | • `prefect` or `dagster` for orchestrating tasks locally  <br>• Containerise with Docker (optional)  <br>• CLI entry‑point (`click`) to run the whole pipeline: data → train → eval → deploy | • Prefect docs – “Getting Started”  <br>• Docker basics: <https://docs.docker.com/get-started/> |
| **7️⃣ Deployment on Your Machine (5 days)** | Serve models locally for inference | • Simple REST API with FastAPI or Flask  <br>• Model loading at startup, GPU‑aware endpoint  <br>• Optional: expose via `ngrok` for remote testing  <br>• Benchmark latency & memory usage | • FastAPI tutorial: <https://fastapi.tiangolo.com/tutorial/> |
| **8️⃣ Capstone Project (10 days)** | End‑to‑end mini‑product | **Example:** “Local Chatbot for a Knowledge Base”  <br>1. Scrape / collect a small FAQ dataset → store with DVC.  <br>2. Fine‑tune a 7B LLM using LoRA on the dataset.  <br>3. Track experiments with MLflow.  <br>4. Build a Prefect pipeline that (a) prepares data, (b) trains, (c) evaluates, (d) builds Docker image.  <br>5. Serve via FastAPI; test locally and through `ngrok`. | Use all tools you set up; write a short README describing the workflow. |


## Daily Study Template (≈2 h per day)

| Time | Activity |
|------|----------|
| 0‑15 min | Review previous notes, list today’s objectives |
| 15‑45 min | Watch/read tutorial / lecture |
| 45‑90 min | Hands‑on coding: follow the tutorial, then modify a bit |
| 90‑105 min | Write a short summary in your own words (Markdown notebook) |
| 105‑120 min | Push code to GitHub, tag version, commit any data changes with DVC |

---

## Essential Tools & Install Commands

```bash
# Python environment
conda create -n ai_local python=3.11 && conda activate ai_local

# Core libs
pip install numpy pandas scikit-learn matplotlib seaborn tqdm

# Deep learning
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu118   # or cpu only
pip install transformers accelerate datasets peft

# Experiment tracking & versioning
pip install mlflow dvc[ssh] hydra-core omegaconf

# Workflow orchestration
pip install prefect  # or dagster

# API serving
pip install fastapi uvicorn

# Optional (Docker)
sudo apt-get install docker.io   # Ubuntu/Debian
```

---

## Quick Reference Cheat‑Sheet (Python snippets)

```python
# 1️⃣ Load a small LLM locally (GGML quantized) with transformers + accelerate
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

model_id = "TheBloke/Llama-2-7B-Chat-GGML"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",