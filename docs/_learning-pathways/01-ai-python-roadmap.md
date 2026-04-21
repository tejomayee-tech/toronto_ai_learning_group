# Python Developer's AI Roadmap

*You already know Python basics (syntax, data structures, functions, OOP). This roadmap takes you from "I can code in Python" to "I can build and deploy AI models" — with small, achievable steps.*

**Timeframe:** ~5-6 months part-time (10-12 hours/week)

---

## Overview

| Stage | Focus | Duration | Portfolio Piece |
|-------|-------|----------|----------------|
| 0 | Clean Code & Setup | 1 week | Linted, CI-ready repo |
| 1 | Math Foundations | 2-3 weeks | ML from Scratch notebook |
| 2 | Core ML Stack | 3 weeks | Kaggle Titanic pipeline |
| 3 | Deep Learning from Scratch | 2 weeks | Neural net in NumPy |
| 4 | PyTorch | 3 weeks | CIFAR-10 classifier |
| 5 | Modern LLMs & RAG | 3 weeks | Fine-tuned GPT-2 + Gradio UI |
| 6 | Production & MLOps | 3 weeks | Deployed AI API |
| 7 | Specialization + Capstone | 8-12 weeks | Full AI product |

---

## Stage 0: Clean Setup (1 Week)

**Goal:** A professional-grade development environment.

| Day | Task |
|-----|------|
| Mon-Tue | Create AI learning repo with `pyproject.toml` (Poetry). Add pre-commit: `black`, `ruff`, `mypy` |
| Wed-Thu | Write a script that loads CSV data and prints stats. Fix all lint warnings |
| Fri | Push to GitHub. Enable GitHub Actions CI badge |
| Sat-Sun | Optional: Study Python type hints if needed |

**Milestone:** A clean, linted repo ready for all future work.

---

## Stage 1: Math Foundations (Weeks 1-2)

**Goal:** Understand *why* algorithms work before using black-box libraries.

| Topic | Resource |
|-------|------|
| Linear algebra (vectors, matrices) | 3Blue1Brown "Essence of Linear Algebra" (6 videos) |
| Probability basics | StatQuest "Statistics Fundamentals" (episodes 1-12) |
| Gradient descent intuition | distill.pub "A Gentle Intro to Gradient Descent" |

### Mini-Projects
1. Implement vector operations with pure Python lists
2. Write gradient descent for `f(w) = (w-3)^2` from scratch. Plot with matplotlib

**Milestone:** Jupyter notebook "ML-from-Scratch" on GitHub

---

## Stage 2: Core ML Stack (Weeks 3-5)

| Week | Focus |
|------|-------|
| 3 | NumPy: arrays, broadcasting, random sampling |
| 4 | Pandas: I/O, cleaning, groupby/aggregation |
| 5 | Matplotlib + Seaborn: data visualization |

### Project: Titanic Survival Prediction

1. Load the Kaggle Titanic dataset
2. EDA: missingness heatmap, correlation matrix
3. Feature engineering: title extraction, family size, age binning
4. Train 3 models: `LogisticRegression`, `RandomForestClassifier`, `XGBClassifier`
5. Evaluate with cross-validation, plot ROC curves

**Deliverables:**
- `titanic.ipynb` with markdown explanations
- `requirements.txt` or `pyproject.toml`
- GitHub Pages site via nbviewer

---

## Stage 3: Deep Learning from Scratch (Weeks 6-7)

| Day | Task |
|-----|------|
| Mon-Tue | Read "Neural Networks and Deep Learning" Chapters 1-2 (free online) |
| Wed-Thu | Build a single-layer perceptron in NumPy (make_moons dataset) |
| Fri-Sat | Extend to a 2-layer MLP with ReLU (train on MNIST) |
| Sun | Write a blog post explaining back-propagation |

**Milestone:** Repo `nn-from-scratch/` with `mlp.py`, training script, loss curve PNG

---

## Stage 4: PyTorch (Weeks 8-10)

| Topic | Resource |
|-------|------|
| Tensors, autograd, nn.Module | PyTorch 2.0 official tutorials |
| CNNs, Transfer Learning | "Deep Learning with PyTorch" (Eli Stevens, free) |
| Lightning basics | PyTorch Lightning YouTube tutorials |

### Project: CIFAR-10 Image Classifier

1. Use `torchvision.datasets.CIFAR10` with data augmentation
2. Build ResNet-18 from `torchvision.models`
3. Train on GPU (Google Colab free tier)
4. Log metrics to Weights & Biases

**Deliverables:**
- `train.py` + `model.py`
- WandB dashboard link in README
- Dockerfile with `torch==2.*`

---

## Stage 5: Modern LLMs & RAG (Weeks 11-13)

| Topic | Resource |
|-------|------|
| Transformer basics | "Attention is All You Need" + Jay Alammar's Illustrated Transformer |
| Hugging Face `transformers` | Official quick-tour tutorial |
| Prompt engineering | dair-ai/Prompt-Engineering-Guide |
| RAG | Hugging Face RAG tutorial + LangChain quickstart |

### Project: Fine-tune GPT-2 on Custom Corpus

1. Gather a small text corpus (blog posts, recipes, etc.)
2. Use `datasets` to load and tokenize
3. Fine-tune with `Trainer` for ~2 epochs on Colab GPU
4. Build interactive Gradio UI

---

## Stage 6: Production & MLOps (Weeks 14-16)

| Week | Focus |
|------|-------|
| 14 | DVC for data versioning, MLflow for experiment tracking |
| 15 | Docker containerization, FastAPI for model serving |
| 16 | GitHub Actions CI/CD, cloud deployment |

### Project: Deploy Your Model

1. Instrument FastAPI with `prometheus_fastapi_instrumentator`
2. Multi-stage Dockerfile for your model API
3. GitHub Actions workflow (lint, test, build Docker image)
4. Deploy to Render.com or Railway

**Milestone:** Live API URL that returns predictions

---

## Stage 7: Specialization (Weeks 17-28)

Pick **one** track:

| Track | What You'll Build |
|-------|------|
| **Computer Vision** | AI defect detector for manufacturing images |
| **NLP** | Legal-clause summarizer with fine-tuned T5 + RAG |
| **Tabular/ML** | Insurance-risk scoring API with SHAP explanations |
| **Edge AI** | Face mask detection on ESP32-Cam |
| **MLOps** | Full production pipeline with monitoring and drift detection |

---

## Daily Study Template (2 hours/day)

| Time | Activity |
|------|------|
| 0-15 min | Review previous notes |
| 15-45 min | Tutorial/lecture |
| 45-90 min | Hands-on coding |
| 90-105 min | Write summary in your own words |
| 105-120 min | Push code to GitHub |

---

## Essential Tools

```bash
# Core
pip install numpy pandas scikit-learn matplotlib seaborn tqdm

# Deep learning
pip install torch torchvision torchaudio

# LLMs
pip install transformers accelerate datasets peft

# MLOps
pip install mlflow dvc hydra-core omegaconf

# Serving
pip install fastapi uvicorn gradio
```

---

## Key Principles

1. **Build before you read** — Code first, understand theory later
2. **One project at a time** — Complete each stage before moving on
3. **Public learning** — Share progress, get feedback
4. **Open source first** — Master free tools before paying for them

---

> *"The best way to learn AI is to build AI."*
