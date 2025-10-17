# Welcome to docs

## Quick Run: Mapped documents local site



```bash
    python3 -m pip install --upgrade pip setuptools wheel
    pip install mkdocs==1.5.3
    pip install mkdocs-material
    mkdocs serve -a 127.0.0.1:8000
    mkdocs build
    mkdocs gh-deploy
```

## Step-by-Step Guide to Set Up MkDocs

### 1\. Initialize the Git Repository (Local)

First, create a new directory for your project, initialize it as a Git repository, and create a basic README.

```bash
# 1. Create a new directory for your project
mkdir my-new-docs-repo

# 2. Move into the directory
cd my-new-docs-repo

# 3. Initialize Git
git init

# 4. Create a placeholder README
echo "# My Project Documentation" > README.md
```

-----

### 2\. Set up the Python Environment and Dependencies

It's best practice to use a **Python virtual environment** to isolate your project's dependencies.

```bash
# 1. Create a virtual environment named 'venv'
python -m venv venv

# 2. Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate

# On Windows (Command Prompt):
# venv\Scripts\activate.bat

# On Windows (PowerShell):
# venv\Scripts\Activate.ps1

# 3. Install MkDocs and the Material theme
pip install mkdocs mkdocs-material
```

-----

### 3\. Initialize the MkDocs Project

Now, use the `mkdocs` command to scaffold the initial file structure.

```bash
# Initialize the MkDocs project
mkdocs new .
```

This command creates two key items:

1.  **`mkdocs.yml`**: The main configuration file.
2.  **`docs/` directory**: The folder where all your Markdown files will live. It will contain an initial `index.md` file.

-----

### 4\. Configure `mkdocs.yml`

Edit the auto-generated `mkdocs.yml` file to match your desired structure and theme (using the Material theme).

Replace the contents of your `mkdocs.yml` with the following configuration (or adapt it based on your needs):

```yaml
site_name: AI Learning Group
site_dir: site
docs_dir: docs
repo_url: https://github.com/your-username/my-new-docs-repo # <--- UPDATE THIS
repo_name: my-new-docs-repo
edit_uri: edit/main/docs/ # Allows users to click 'Edit this page'

# Configure the Material theme
theme:
  name: material
  palette:
    scheme: slate # dark mode
    primary: deep purple
    accent: purple
  features:
    - navigation.instant
    - navigation.tabs
    - search.suggest
    - toc.follow

# Add necessary extensions and plugins
markdown_extensions:
  - footnotes
  - admonition
  - pymdownx.details

plugins:
  - search

# Define the navigation structure
nav:
  - Home: index.md
  - Docs:
    - AI PC Build: ai-pc/pc-for-running-20b-llm.md
```

> **Note on File Structure:** For the `nav` above to work, you must create the directory and file: `docs/ai-pc/pc-for-running-20b-llm.md`.

-----

### 5\. Create Your Content Files

Create the content file referenced in the navigation:

```bash
# Create the subdirectory
mkdir -p docs/ai-pc

# Create the content file
touch docs/ai-pc/pc-for-running-20b-llm.md
```

You can now edit `docs/index.md` and `docs/ai-pc/pc-for-running-20b-llm.md` with your actual documentation content.

-----

### 6\. Test Locally

Run the local development server to see your documentation in action.

```bash
mkdocs serve -a 127.0.0.1:8000
```

Open your browser to the address provided (usually **[http://127.0.0.1:8000](https://www.google.com/search?q=http://127.0.0.1:8000)**). The server will automatically reload when you make changes to any of your Markdown or configuration files.

-----

### 7\. Commit and Push to Git

Once you are happy with the setup, commit your initial files to your local repository and push them to your remote Git hosting service (like GitHub, GitLab, or Bitbucket).

```bash
# 1. Add generated files (excluding the virtual environment)
git add .

# 2. (Optional but recommended) Create a .gitignore file
echo "venv/" >> .gitignore
git add .gitignore

# 3. Commit the initial setup
git commit -m "Initial MkDocs setup with Material theme"

# 4. Add your remote (if not already done)
# git remote add origin <your-repo-url>

# 5. Push the changes
# git push -u origin main
```