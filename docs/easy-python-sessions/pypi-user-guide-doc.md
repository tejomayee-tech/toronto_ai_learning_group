# Tutorial for publishing a Python library to **PyPI** (Python Package Index) 

## 1\. 🏗️ Project Structure and Code

First, set up your project directory and create the core files. The recommended layout uses a `src` directory to cleanly separate your package source from other files like configuration, documentation, and tests.

```
pypitest-myutils/
├── src/
│   └── pypitest_myutils/  # <--- This is your actual Python package
│       └── __init__.py    # <--- Contains version and core code
└── README.md
└── LICENSE
└── pyproject.toml         # <--- Package metadata and build config
```

### Step 1.1: Create the Project Structure

Run these commands in your terminal to set up the directories:

```bash
mkdir pypitest-myutils
cd pypitest-myutils
mkdir src
mkdir src/pypitest_myutils
```

### Step 1.2: Add the Python Code (`src/pypitest_myutils/__init__.py`)

This file contains your library's actual functionality.

```python
# src/pypitest_myutils/__init__.py

__version__ = "0.0.1"

def reverse_string(s):
    """Reverses a given string."""
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    return s[::-1]

def greet(name="World"):
    """Returns a simple greeting."""
    return f"Hello, {name}!"

# Optional: Print the version when the package is imported
print(f"pypitest-myutils version {__version__} loaded.")
```

-----

## 2\. 📝 Define Package Metadata

You'll define all necessary package metadata and configuration in the **`pyproject.toml`** file, which is the modern standard for Python packaging.

### Step 2.1: Create `pyproject.toml`

Create this file in the root of your project (`pypitest-myutils/`). **Remember to replace placeholder information** like `YOUR_NAME` and `YOUR_EMAIL`.

```toml
# pyproject.toml

[build-system]
# Specify the build tools required (e.g., setuptools, hatchling)
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "pypitest-myutils" # Your unique package name on PyPI
version = "0.0.1"         # The initial version number
authors = [
    {name = "YOUR_NAME", email = "YOUR_EMAIL@example.com"},
]
description = "A simple example package with utility functions."
readme = "README.md"
requires-python = ">=3.8" # Minimum supported Python version
license = {text = "MIT License"} # Or {file = "LICENSE"}
keywords = ["utility", "example", "pypi", "tutorial"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
dependencies = [
    # Add any runtime dependencies here, e.g., "requests>=2.28.1"
]

[project.urls]
Homepage = "https://github.com/YOUR_USERNAME/pypitest-myutils"
"Bug Tracker" = "https://github.com/YOUR_USERNAME/pypitest-myutils/issues"

# Configure setuptools to find the package inside the 'src' directory
[tool.setuptools]
package-dir = {"" = "src"}
```

### Step 2.2: Add `README.md` and `LICENSE`

Create these files in the root directory.

  * **`README.md`**: This content will be displayed on your package's page on PyPI.
  * **`LICENSE`**: PyPI strongly recommends a license (MIT is common for open-source).

-----

## 3\. 📦 Build and Check

Now we use the `build` tool to create the distribution files.

### Step 3.1: Install Build Tools

Install the necessary tools, including `build` for packaging and `twine` for uploading.

```bash
pip install --upgrade build twine
```

### Step 3.2: Create the Distribution Files

Run the `build` command from the root of your project (`pypitest-myutils/`):

```bash
python -m build
```

This command creates a new directory called **`dist/`** containing two files:

1.  A **Source Distribution (`.tar.gz`)**: Contains the source code and metadata.
2.  A **Wheel Distribution (`.whl`)**: A pre-built package for faster installation.

### Step 3.3: Check the Package (Optional but Recommended)

Use `twine` to verify that your metadata will display correctly on PyPI.

```bash
twine check dist/*
```

> **Expected Output:** `Checking distribution dist/pypitest_myutils-0.0.1-py3-none-any.whl: PASSED`

-----

## 4\. 🔑 PyPI Account and Token

To upload, you need a PyPI account and an API token. **Never use your actual PyPI password for uploading.**

### Step 4.1: Register Accounts

1.  **TestPyPI:** Go to `https://test.pypi.org/account/register/` and create an account. **Always test here first\!**
2.  **PyPI:** Go to `https://pypi.org/account/register/` and create your main account.

### Step 4.2: Generate an API Token

1.  Log into your **TestPyPI** account (`test.pypi.org`).
2.  Go to your **Account Settings** and select **"Add API token"** under the **API tokens** section.
3.  Set the Scope to **"Entire account"** (or select your package name once it's created).
4.  **Copy the generated token immediately\!** You won't see it again. Save it securely. It will look like `pypi-................`.

-----

## 5\. 📤 Upload to TestPyPI

It is crucial to test the upload and installation process on **TestPyPI** before going to the live index.

### Step 5.1: Upload using `twine`

Run the following command, specifying the TestPyPI repository (`-r testpypi`).

```bash
python -m twine upload --repository testpypi dist/*
```

  * **Username:** Enter `__token__`
  * **Password:** Paste your TestPyPI API token (the one you copied in Step 4.2).

### Step 5.2: Test Installation

Once the upload succeeds, you can immediately test the installation:

```bash
# Create a new environment or shell to test the installation
pip install --index-url https://test.pypi.org/simple/ pypitest-myutils
```

Now, try running your code:

```python
# In a Python interpreter
from pypitest_myutils import greet, reverse_string

print(greet("Developer"))
# Expected: Hello, Developer!
print(reverse_string("Hello"))
# Expected: olleH
```

-----

## 6\. ✅ Final Upload to PyPI

If the TestPyPI process works perfectly, you can now upload to the main PyPI.

### Step 6.1: Get a PyPI API Token

Repeat **Step 4.2** on the main **PyPI** site (`https://pypi.org/`) to get a new token for the production index.

### Step 6.2: Upload to PyPI

Run the upload command again, this time *without* the `--repository testpypi` flag (it defaults to the main PyPI).

```bash
python -m twine upload dist/*
```

  * **Username:** Enter `__token__`
  * **Password:** Paste your **main PyPI** API token.

Congratulations\! Your package is now live and installable by anyone with:

```bash
pip install pypitest-myutils
```


# Step-by-step guide to setting up a workflow for continuous publishing.


## ⚙️ Prerequisites

Before you start, you must complete two crucial steps:

### 1\. Create a PyPI API Token

  * Go to your PyPI account settings at `https://pypi.org/manage/account/token/`.
  * Click **"Add API token"**.
  * Crucially, set the **Scope** to **"Project"** and select the name of your package (e.g., `pypitest-myutils`). Using a scoped token is far more secure than using an account-wide token.
  * **Copy the generated token.** You will only see it once.

### 2\. Add the Token to GitHub Secrets

  * Go to your package's GitHub repository (e.g., `https://github.com/YOUR_USERNAME/pypitest-myutils`).
  * Navigate to **Settings** $\to$ **Secrets and variables** $\to$ **Actions**.
  * Click **"New repository secret"**.
      * **Name:** `PYPI_API_TOKEN`
      * **Secret:** Paste the PyPI API token you copied above.

This secret allows your GitHub workflow to securely authenticate with PyPI without exposing the token in your code.

-----

## 🚀 Creating the GitHub Actions Workflow

Create a new directory and file in your repository: `.github/workflows/publish.yml`.

### Step 1: Create the Workflow File

```bash
mkdir -p .github/workflows
touch .github/workflows/publish.yml
```

### Step 2: Add the Workflow Code (`publish.yml`)

This YAML file defines the automated process. This workflow runs whenever you push a tag that starts with `v` (e.g., `v0.0.2`).

```yaml
# .github/workflows/publish.yml

name: Publish Python Package to PyPI

on:
  push:
    # Trigger the workflow only when a tag starting with 'v' is pushed
    tags:
      - 'v*'

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: Release # Use an environment for better protection and auditing

    steps:
      - name: 📦 Checkout code
        uses: actions/checkout@v4
        # Fetch tags to ensure the workflow knows the current version
        with:
          fetch-depth: 0

      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: 🛠️ Install dependencies and build
        run: |
          # Install the build tools
          pip install build
          # Create the .tar.gz and .whl files in the dist/ directory
          python -m build

      - name: 📤 Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          # Use the repository secret for authentication
          password: ${{ secrets.PYPI_API_TOKEN }}
          # Use the environment variable to extract the version from the tag
          # e.g., if the tag is v0.0.2, the version passed to PyPI is 0.0.2
          # PyPI publication is automatic for files in dist/
```

-----

## 🎯 The Final Automated Process

Once this file is committed and pushed to GitHub, here is how you perform a new release:

1.  **Update the Version:** In your `src/pypitest_myutils/__init__.py` (and optionally `pyproject.toml`), update the version string (e.g., from `"0.0.1"` to `"0.0.2"`).
2.  **Commit Changes:** Commit your updated files.
    ```bash
    git commit -am "Release v0.0.2: Feature fix."
    ```
3.  **Create and Push a Tag:** Create a Git tag that matches the new version, prefixed with `v`.
    ```bash
    git tag v0.0.2
    git push origin main --tags
    ```

As soon as the `v0.0.2` tag hits GitHub, the workflow will **automatically trigger**:

1.  It checks out the code.
2.  It uses Python to run `python -m build`.
3.  It securely uses `pypa/gh-action-pypi-publish` to upload the newly built files from `dist/` to PyPI using the `PYPI_API_TOKEN`.

Your new version, `0.0.2`, is now available via `pip install --upgrade pypitest-myutils`.