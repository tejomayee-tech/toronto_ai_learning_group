# n8n - Step-by-step setup guide with Docker Desktop

## Demo

<iframe 
    src="https://drive.google.com/file/d/1F-7CetDJM8elcM5XAS7uj_L2pXwFxa5d/preview" 
    width="720" 
    height="360" 
    allow="autoplay" 
    frameborder="0" 
    allowfullscreen
></iframe>

### steps

1. Download and install [docker desktop](https://www.docker.com/products/docker-desktop/)

    **Note**: Its better install with recommended options like wsl
 
    <img src="../images/001.png" alt="Image 1" width="400">

    <img src="../images/004.png" alt="Image 2" width="400">
    
    **Info**: If you installed with default options, the below wsl window will open, you can close it safely.
    
    <img src="../images/005.png" alt="Image 3" width="400">

2. After installion is complete, restart might be needed, then lookup "Docker Desktop" in windows start meny and open it.

    <img src="../images/006.png" alt="Image 4" width="400">

3. CLick Search on top and type n8n in seach window, and then click pull for n8n image

    <img src="../images/008.png" alt="Image 5" width="400">

    <img src="../images/009.png" alt="Image 6" width="400">

    <img src="../images/010.png" alt="Image 7" width="400">

4. Run the container and provide the parameters and values shown in screenshot below

    <img src="../images/011.png" alt="Image 8" width="400">

    <img src="../images/011a.png" alt="Image 9" width="400">

    <img src="../images/012.png" alt="Image 10" width="400">

5. URL will be generated, open it in browser and create a free account

    <img src="../images/013.png" alt="Image 11" width="400">

    <img src="../images/014.png" alt="Image 12" width="400">

6. On home page, click on create workflow to see workflow screen.

    <img src="../images/016.png" alt="Image 13" width="400">

7. We'll take a step back to add community nodes for n8n

    <img src="../images/017.png" alt="Image 14" width="400">

    <img src="../images/018.png" alt="Image 15" width="400">

    <img src="../images/020.png" alt="Image 16" width="400">

8. Open the new workflow again, search for triggers and add chat trigger, nothing to modify in settings, click back.

    <img src="../images/021.png" alt="Image 17" width="400">

    <img src="../images/022.png" alt="Image 18" width="400">

    <img src="../images/023.png" alt="Image 19" width="400">

    <img src="../images/024.png" alt="Image 20" width="400">

9. Now lets look for AI agent and add it, no setting to modify for now, click back and agent should be added with nodes for chat model, memory and tool.

    <img src="../images/025.png" alt="Image 21" width="400">

    <img src="../images/026.png" alt="Image 22" width="400">

    <img src="../images/027.png" alt="Image 23" width="400">

10. Now lets click on chat model node of the agent and search for Ollama chat model , selct it, in config screen, click add credential and enter docker url shown, no api key needed as it local LLM, connection will be tested and click close and select the LLM.**NOTE** you might need to reopen to see LLM sometimes.

    <img src="../images/028.png" alt="Image 24" width="400">

    <img src="../images/032.png" alt="Image 25" width="400">

    <img src="../images/033.png" alt="Image 26" width="400">

11. Click on memory of the AI agent and add simple memory node.

    <img src="../images/034.png" alt="Image 27" width="400"> 
