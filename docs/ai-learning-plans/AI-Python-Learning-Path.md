## 🎯 AI‑Learning Roadmap for a Python Developer  
*You already know the basics of Python (syntax, data structures, functions, OOP). This roadmap builds on that foundation and takes you from “I can code in Python” → “I can design, train, evaluate, and deploy modern AI/ML models”.*

---

## 1️⃣ HOW TO READ THIS ROADmap  

| Symbol | Meaning |
|--------|---------|
| **🗓️ Weeks** | Approximate time if you study ~10‑12 h per week (adjust to your schedule). |
| **📚 Resources** | Free or low‑cost links; you can swap in any equivalent material. |
| **🔧 Hands‑On** | Mini‑project / exercise that cements the concept. |
| **🚀 Milestone** | A concrete artefact you should have on GitHub (or a live demo). |
| **⚡️Tip** | Quick cheat‑sheet or shortcut to speed up learning. |

---

## 2️⃣ OVERVIEW OF THE PATH  

| Stage | Core Topics | Typical Duration | End‑Goal (Portfolio Piece) |
|-------|-------------|------------------|----------------------------|
| **0 – Refresher & Tooling** | Virtual envs, `pip/poetry`, Git, IDE debugging, type hints (`mypy`) | 1 wk | Clean repo with linting + CI badge |
| **1 – Math Foundations for ML** | Linear algebra (vectors, matrices), probability basics, calculus intuition, optimisation (gradient descent) | 2‑3 wks | Jupyter notebook “ML from Scratch” (no libraries) |
| **2 – Core Python ML Stack** | `numpy`, `pandas`, `matplotlib/seaborn`, `scikit‑learn` | 3 wks | End‑to‑end Kaggle “Titanic” pipeline (data cleaning → model → evaluation) |
| **3 – Deep Learning Fundamentals** | Tensor fundamentals, automatic differentiation, back‑propagation, regularisation | 2 wks | From‑scratch neural net in NumPy that learns XOR |
| **4 – PyTorch (or TensorFlow)** | Tensors, DataLoaders, nn.Module, training loops, GPU basics, torchvision, huggingface 🤗datasets | 3 wks | Image classifier on CIFAR‑10 with data augmentation + TensorBoard logs |
| **5 – Modern LLM & Generative AI** | Transformers architecture, attention, pre‑training vs fine‑tuning, Hugging Face `transformers`, Prompt engineering, Retrieval‑Augmented Generation (RAG) | 3 wks | Fine‑tune a small GPT‑2 on custom text + build a Gradio web UI |
| **6 – Production & MLOps** | Model packaging (`torch.save`/ONNX), Docker, FastAPI, CI/CD for ML, monitoring, experiment tracking (Weights & Biases / MLflow) | 3 wks | Deploy the fine‑tuned LLM as a REST API on Render/Render.com or Railway |
| **7 – Specialisation + Capstone** | Choose one track: Computer Vision, NLP, Tabular data, Reinforcement Learning, or Edge AI. Build a larger project (8‑12 wks). | 8‑12 wks | Full‑stack AI product (e.g., “AI‑powered document summarizer” web app) on GitHub with live demo. |

**Total:** ~20–25 weeks (~5–6 months part‑time).  
If you can study full‑time, compress by ~30 %.

---

## 3️⃣ DETAILED WEEK‑BY‑WEEK PLAN  

### **Week 0 – Set‑up & Clean Code**
| Day | Activity |
|-----|----------|
| Mon‑Tue | Create a *dedicated* AI‑learning repo. Initialise with `pyproject.toml` (use **Poetry**). Add pre‑commit hooks: `black`, `ruff`, `mypy`. |
| Wed‑Thu | Write a tiny script that loads a CSV, prints basic stats. Run `ruff` and fix all warnings. |
| Fri | Push to GitHub; enable **GitHub Actions** CI badge in README (lint → test). |
| Sat‑Sun | Optional: watch “Python Type Hints” (Corey Schafer) if you’re not comfortable with static typing. |

🚀 **Milestone:** A clean, linted repo ready for all future projects.

---

### **Weeks 1‑2 – Math Foundations (No‑library)**  
**Goal:** Understand *why* algorithms work before using black‑box libraries.  

| Resource | Key Chapters |
|----------|--------------|
| “Essence of Linear Algebra” (3Blue1Brown) – 6 short videos | Vectors, matrix multiplication, eigenvectors |
| “StatQuest: Statistics Fundamentals” playlist (YouTube) – episodes 1‑12 | Mean/variance, distributions, Bayes theorem |
| Blog post “A Gentle Intro to Gradient Descent” (distill.pub) | Cost surface, learning rate, convergence |

#### Hands‑On
- **Notebook 1:** Implement vector addition, dot product, matrix multiplication with pure Python lists.  
- **Notebook 2:** Write a gradient‑descent optimizer from scratch for a simple quadratic loss `f(w)= (w‑3)^2`. Plot the trajectory using `matplotlib`.

🚀 **Milestone:** A Jupyter notebook titled *“ML‑from‑scratch – Linear Algebra & Optimisation”* on GitHub.

---

### **Weeks 3‑5 – Core ML Stack (`scikit‑learn`)**  
| Week | Topics |
|------|--------|
| 3 | `numpy` fundamentals, broadcasting, random sampling. |
| 4 | `pandas` I/O, cleaning (missing values, type conversion), groupby/aggregation. |
| 5 | `matplotlib` + `seaborn` visualisation, basic statistical plots. |

#### Mini‑Project – **Titanic Survival Prediction**  
1. Pull the Kaggle dataset (or use the public CSV).  
2. Perform EDA: missingness heatmap, correlation matrix.  
3. Feature engineering: title extraction, family size, age binning.  
4. Train three models (`LogisticRegression`, `RandomForestClassifier`, `XGBClassifier`).  
5. Evaluate with cross‑validation; plot ROC curves.  

**Deliverables:**  
- Clean notebook (`titanic.ipynb`) with markdown explanations.  
- `requirements.txt`/`pyproject.toml`.  
- A **GitHub Pages** site that renders the notebook via `nbviewer`.

---

### **Weeks 6‑7 – Deep Learning from Scratch (NumPy)**  

| Day | Activity |
|-----|----------|
| Mon‑Tue | Read “Neural Networks and Deep Learning” – Chapter 1‑2 (online free book). |
| Wed‑Thu | Implement a **single‑layer perceptron** in NumPy for binary classification on the *make_moons* dataset. |
| Fri‑Sat | Extend to a **2‑layer MLP** with ReLU, train on MNIST (use `keras.datasets` just for loading). |
| Sun | Write a short blog post summarising back‑propagation equations (with LaTeX images). |

🚀 **Milestone:** Repo `nn-from-scratch/` containing `mlp.py`, training script, and a PNG of loss curves.

---

### **Weeks 8‑10 – PyTorch Mastery**  

| Resource | Core Sections |
|----------|----------------|
| Official PyTorch 2.0 tutorials (fast.ai style) | Tensors, autograd, nn.Module, DataLoaders, GPU training |
| “Deep Learning with PyTorch” (free book by Eli Stevens) | Chapters 3‑5 (CNNs, Transfer Learning) |
| “PyTorch Lightning Basics” (YouTube) | Boilerplate reduction, logging |

#### Project – **CIFAR‑10 Image Classifier**  
1. Use `torchvision.datasets.CIFAR10`, apply data augmentation (`RandomCrop`, `HorizontalFlip`).  
2. Build a simple ResNet‑18 from `torchvision.models`.  
3. Train on GPU (Google Colab free tier).  
4. Log metrics to **Weights & Biases** (free plan) and visualise with TensorBoard.  

**Deliverables:**  
- `train.py` + `model.py`.  
- `wandb` dashboard link in README.  
- Dockerfile that builds the environment (`torch==2.*`, `cuda` optional).  

---

### **Weeks 11‑13 – Modern LLM & Generative AI**  

| Topic | Resource |
|-------|----------|
| Transformer basics, self‑attention | “Attention is All You Need” (Harvard CS 287 lecture) + Illustrated transformer blog post (Jay Alammar) |
| Hugging Face `transformers` library | Official tutorial “Quick tour of 🤗 Transformers” |
| Prompt engineering & few‑shot learning | “Prompt Engineering Guide” (github.com/dair-ai/Prompt-Engineering-Guide) |
| Retrieval‑Augmented Generation (RAG) | “RAG Tutorial” – Hugging Face blog + LangChain quickstart |

#### Mini‑Project – **Fine‑tune GPT‑2 on Custom Corpus**  
1. Gather a small text corpus (e.g., your own blog posts, or open‑source recipes).  
2. Use `datasets` to load and tokenise.  
3. Fine‑tune with `Trainer` for ~2 epochs on Colab GPU.  
4. Build an interactive **Gradio** UI that takes a prompt and returns generated text.  


### **Week 14 – MLOps Foundations**

| 🗂️ Theory | 📖 Resources |
|-----------|--------------|
| **Why MLOps?** Lifecycle of an ML product, common failure modes. | “MLOps: Continuous Delivery and Automation Pipelines in Machine Learning” (O'Reilly) – Chapter 1. |
| **Model versioning & metadata** – `DVC`, `MLflow` tracking, `Weights & Biases`. | DVC tutorial *“Getting Started with Data Version Control”* (official docs). |
| **Experiment reproducibility** – random seeds, containerisation basics. | “Reproducible Machine Learning Experiments” (Kaggle Learn micro‑course). |

| 🛠️ Hands‑On |
|-------------|
| 1️⃣ Initialise a **DVC** repo inside your existing `cifar10/` project. Add the raw data (`CIFAR-10`) and the trained model checkpoint as DVC‑tracked files. Commit and push to a remote (GitHub + an S3 bucket or free `dvc.org` remote). |
| 2️⃣ Run a second training experiment with a different learning rate; log hyper‑parameters & metrics to **MLflow** locally (`mlflow ui`). Verify that you can compare runs side‑by‑side. |
| 3️⃣ Export the best checkpoint to **ONNX** (`torch.onnx.export`) and store it in DVC. |

| 🚀 Milestone |
|--------------|
| A **GitHub repo `cifar10-mlops/`** containing: <br>• DVC config + `.dvc` files.<br>• `mlflow` experiment logs (saved under `mlruns/`).<br>• README with badge showing “Latest model version: v0.2”. |

| ⚡️ Tip |
|--------|
| Use the **`make`** utility to chain steps (`make train`, `make evaluate`, `make push-model`). This keeps your workflow reproducible without writing a full CI script yet. |

---

### **Week 15 – Containerisation & API Service**

| 🗂️ Theory |
|-----------|
| Docker fundamentals: images, layers, `Dockerfile` best practices (multi‑stage builds). <br>FastAPI basics: path operations, request validation with Pydantic, async endpoints. <br>Serving PyTorch models (`torchserve`) vs custom FastAPI wrapper. |

| 📖 Resources |
|--------------|
| “Docker for Data Scientists” – free notebook on Kaggle Learn.<br>`fastapi.tiangolo.com` tutorial (first 3 sections).<br>Hugging Face `text-generation-inference` Docker image example. |

| 🛠️ Hands‑On |
|-------------|
| 1️⃣ Write a **FastAPI** app (`app.py`) that loads the ONNX model from DVC and exposes `/predict` (accepts JSON with an image base64 string, returns class probabilities). <br>2️⃣ Create a **multi‑stage Dockerfile**: stage 1 builds the environment, stage 2 copies only the runtime artefacts. <br>3️⃣ Build & run locally (`docker compose up -d`). Test with `curl` or Postman. |

| 🚀 Milestone |
|--------------|
| A public Docker image on **Docker Hub** (e.g., `yourusername/cifar10-api:latest`) and a **GitHub Actions workflow** that builds the image on every push to `main`. Include a badge in README showing “Docker build status”. |

| ⚡️ Tip |
|--------|
| Set `ENV PYTHONUNBUFFERED=1` in Dockerfile so logs appear instantly in `docker logs`. This helps debugging latency issues. |

---

### **Week 16 – CI/CD for ML (GitHub Actions)**

| 🗂️ Theory |
|-----------|
| GitHub Actions syntax, matrix builds, secrets management. <br>Deploy‑to‑cloud patterns: Render, Railway, Fly.io, or a simple **DigitalOcean App Platform** service. |

| 📖 Resources |
|--------------|
| “Continuous Integration for Machine Learning” – Medium article (by Patrick McClurg). <br>`actions/setup-python` and `docker/build-push-action`. |

| 🛠️ Hands‑On |
|-------------|
| 1️⃣ Add a **GitHub Actions** workflow (`.github/workflows/ci.yml`) that: <br>  • Lints with `ruff` + `black`. <br>  • Runs unit tests (`pytest`). <br>  • Builds the Docker image and pushes to Docker Hub (use encrypted secrets for credentials). |
| 2️⃣ Add a **deployment job** that, on tag release (`v*.*.*`), triggers a Deploy on Render (Render’s “Deploy from Docker Hub” integration). |
| 3️⃣ Verify the live endpoint returns predictions within < 200 ms. |

| 🚀 Milestone |
|--------------|
| A **GitHub Actions badge** in README + a live URL (`https://cifar10-api.onrender.com/predict`) that you can curl from anywhere. |

| ⚡️ Tip |
|--------|
| Keep the test suite tiny but fast (< 2 min). Use `pytest -q` and cache the Docker layers with `actions/cache`. This prevents CI time‑outs on free plans. |

---

### **Week 17 – Monitoring & Observability**

| 🗂️ Theory |
|-----------|
| Model drift, data quality alerts, latency monitoring, logging best practices (structured JSON logs). <br>Tools: Prometheus + Grafana, Sentry for error tracking, `mlflow` model registry. |

| 📖 Resources |
|--------------|
| “Monitoring Machine Learning Models in Production” – Google Cloud Blog (concepts apply to any stack). <br>Prometheus quick‑start guide (official docs). |

| 🛠️ Hands‑On |
|-------------|
| 1️⃣ Instrument FastAPI with **`prometheus_fastapi_instrumentator`** to expose `/metrics`. <br>2️⃣ Deploy a **Grafana dashboard** (via Docker Compose) that visualises request latency, error rate, and CPU usage. <br>3️⃣ Set up **Sentry** for Python to capture unhandled exceptions in the API. |

| 🚀 Milestone |
|--------------|
| A screenshot of the Grafana dashboard embedded in your repo’s README (or a live public Grafana instance). |

| ⚡️ Tip |
|--------|
| Use `uvicorn --log-level warning` when running locally to keep logs clean; Sentry will still capture stack traces. |

---

### **Weeks 18‑20 – SPECIALISATION TRACKS**  

Pick **one** of the following tracks (you can switch later, but commit to one for depth).  Each track includes a *mini‑capstone* that becomes a core portfolio piece.

| Track | Core Topics | Mini‑Capstone |
|-------|-------------|---------------|
| **Computer Vision (CV)** | Advanced CNNs (EfficientNet, ConvNeXt), object detection (YOLOv8), segmentation (U‑Net), OpenCV augmentation pipelines. | Build an *“AI‑powered defect detector”* for a public manufacturing dataset (e.g., Metal Surface Defects) → web UI that highlights defects on uploaded images. |
| **Natural Language Processing (NLP)** | Transformers fine‑tuning, token classification, seq2seq summarisation, LangChain RAG pipelines, evaluation metrics (BLEU, ROUGE). | Create a *“Legal‑Clause Summarizer”* using a fine‑tuned T5 model + Retrieval from a small corpus of contracts. |
| **Tabular / AutoML** | CatBoost, LightGBM, feature engineering for categorical data, AutoGluon, SHAP explainability. | Build an *“Insurance‑Risk Scoring API”* that returns risk probability and SHAP explanation plot per request. |
| **Reinforcement Learning (RL)** | OpenAI Gym, DQN, PPO, stable‑baselines3, vectorised environments, curriculum learning. | Train a **PPO** agent to solve the “LunarLanderContinuous-v2” task and expose a simple Flask UI that shows live gameplay via WebSockets. |
| **Edge AI / TinyML** | TensorFlow Lite, ONNX Runtime for mobile, model quantisation, Arduino/ESP32 deployment. | Deploy a tiny‑CNN (≤ 200 KB) on an ESP32‑Cam to perform *“real‑time face mask detection”* and stream results to a local web dashboard. |

#### Common Hands‑On Steps (for any track)

1️⃣ **Data acquisition & EDA** – store raw data under `data/raw/` and version with DVC.  
2️⃣ **Model training script** (`train_{track}.py`) that logs hyper‑parameters to MLflow.  
3️⃣ **Export & optimise** – e.g., convert to ONNX, apply post‑training quantisation if applicable.  
4️⃣ **Serve** – reuse the FastAPI template from Week 15; add a route specific to the task (e.g., `/detect-def