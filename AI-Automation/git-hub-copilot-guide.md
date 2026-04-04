Set up AI-driven automation using Visual Studio Code, GitHub Copilot, and Playwright

### **Step 1: Install Essential Prerequisites**
Before starting, ensure your environment has the following tools installed:
*   **Node.js:** Necessary for executing JavaScript and TypeScript code on your machine.
*   **Visual Studio Code (VS Code):** The primary code editor where the integration takes place.
*   **GitHub Account:** Required to access GitHub Copilot and store your code in the cloud.

### **Step 2: Connect GitHub Copilot to VS Code**
1.  Open VS Code and locate the **Chat** icon or the "Use AI features with Copilot for free" prompt.
2.  Click **"Continue with GitHub"** to authenticate your account.
3.  Authorize Visual Studio Code in your browser to finalize the connection.

### **Step 3: Configure the AI Agent and Models**
*   **Select a Model:** In the chat dropdown, you can choose from different large language models (LLMs) like GPT, Claude, or Gemini, depending on your needs.
*   **Choose Agent Mode:** Change the chat type to **"Agent"** (often represented by a specific icon). This allows the AI to not just answer questions, but to **execute commands, create files, and interact with your terminal**.

### **Step 4: Enable the Playwright MCP Server**
The **Model Context Protocol (MCP)** allows the AI to use specific tools, such as manipulating a web browser.
1.  Go to the **Extensions** view in VS Code and locate the **MCP Servers** section.
2.  Enable the **MCP Marketplace** and search for the **Playwright MCP Server** published by **Microsoft**.
3.  Install the server to give the AI the "ability" to navigate and interact with web pages.

### **Step 5: Project Setup and MCP Configuration**
1.  Create a new folder for your project and open it in VS Code.
2.  Create a folder named `.vscode` at the root and a file inside it called `settings.json`.
3.  Copy and paste the **MCP Server configuration** into this file to link the Playwright tools to your AI agent.

### **Step 6: Initialize the Automation Project via AI**
Using the Chat Agent, provide a prompt such as: *"Create a project in this folder to automate a web application using Playwright with TypeScript"*. 
*   The AI will automatically generate the project skeleton, install necessary packages (like `playwright`), and create initial configuration files.
*   Review and **"Keep"** the changes the AI proposes.

### **Step 7: Define Custom AI Instructions (Best Practice)**
To make the AI more "deterministic" and ensure it follows professional standards (like the **Page Object Model**), create a specialized instruction file.
1.  Create a folder named `.github` at the root.
2.  Inside, create a file named `copilot-instructions.md`.
3.  Add instructions defining the **tech stack**, the **AI's persona** (e.g., Senior Test Automation Engineer), and **architectural rules** such as prohibiting selectors inside test files and requiring the use of page objects.

### **Step 8: Generate and Run Automation Scripts**
1.  **Generate Tests:** Prompt the AI to create a specific test (e.g., *"Create a test that navigates to [URL], authenticates with [user], and adds a product to the cart using page objects"*).
2.  **Review and Fix:** If the AI makes an error or the test fails, you can use the **"Fix with Copilot"** button or provide the error logs to the chat for a solution.
3.  **Execute:** Run your tests in the terminal using commands like `npx playwright test`. You can add the `--headed` flag to watch the AI-controlled browser perform the actions in real-time.