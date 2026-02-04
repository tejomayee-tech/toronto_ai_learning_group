# Automatic Backup

Just adding a google account in setting > accounts on ubuntu or zorin will show the google drive in files and its used to back up things instantly. 
Below is additional configration for persistant mounting.


## Zorin OS uses the GNOME desktop environment (or a customized version of it). GNOME has a built-in feature called "Online Accounts" that allows you to connect your Google account

> **Note** Best and Straightforward

    1. Go to Settings.
    1. Scroll down and click on Online Accounts.
    1. Click Add Account and select Google.
    1. Follow the prompts to sign in to your Google account and grant the necessary permissions.
    1. Once connected, you should see your Google Drive listed in your file manager (Nautilus).

A common point of confusion with GNOME Online Accounts (which Zorin OS uses). When you add your Google account in Settings > Online Accounts, it integrates Google Drive into your file manager (Nautilus). However, it's not a persistent local mount like a traditional drive. It's more of an "on-demand" connection. That's why you can only `cd` into it from the terminal *after* you've opened it in the Files app – opening it triggers the connection.

To get a truly persistent mount and automate syncing, you'll need to use one of the methods I mentioned previously, as GNOME Online Accounts alone isn't designed for that level of automation.

Let's break down how to achieve what you want, focusing on tools that can automate sync and a Python-based approach:

### 1. **Initializing a Persistent Google Drive Mount**

For automatic syncing, you need a mount point that's always there, regardless of whether you've opened Files.

**A. Using Rclone (Recommended for scripting and automation)**

Rclone is incredibly powerful for this. It can mount your Google Drive as a regular filesystem, which can then be used by other tools (like a Python script) for syncing.

**Steps:**

1.  **Install Rclone:**
    ```bash
    sudo apt install rclone
    ```

2.  **Configure Rclone for Google Drive:**
    ```bash
    rclone config
    ```
    * Follow the prompts. When it asks "New remote?", type `n`.
    * Give your remote a name (e.g., `gdrive`).
    * Select `drive` from the list of storage types (usually option `15` or similar).
    * For `client_id` and `client_secret`, you can usually leave them blank (Rclone will use its own defaults, which is fine for personal use).
    * For `scope`, choose the default full access (usually option `1`).
    * For `root_folder_id` and `service_account_file`, you can typically leave them blank.
    * When it asks "Edit advanced config?", choose `n`.
    * It will ask you "Use auto config?", choose `y`. This will open a browser for you to authenticate your Google account.
    * Once authenticated in the browser, you'll get a success message. Go back to the terminal and confirm.
    * You'll see a summary of your remote. Type `q` to quit the config.

3.  **Create a Mount Point:**
    Choose a directory where you want your Google Drive to appear locally. A common place is in your home directory.
    ```bash
    mkdir ~/GoogleDriveMount # Or any name you prefer
    ```

4.  **Mount Google Drive (Temporary for testing):**
    ```bash
    rclone mount gdrive: ~/GoogleDriveMount --vfs-cache-mode full &
    ```
    * `gdrive:` is the name you gave your remote in step 2.
    * `~/GoogleDriveMount` is your local mount point.
    * `--vfs-cache-mode full`: This option is important for performance and reliability when interacting with the mounted drive, especially if you're writing to it. It tells Rclone to cache file data locally.
    * `&`: Runs the command in the background, so your terminal isn't tied up.

    Now, you should be able to `cd ~/GoogleDriveMount` and see your Google Drive files.

5.  **Automate Mount on Startup (Using systemd for robustness):**
    For a truly automatic mount that persists across reboots, `systemd` is the preferred method on modern Linux systems like Zorin.

    * **Create a systemd service file:**
        ```bash
        nano ~/.config/systemd/user/google-drive.service
        ```
        Paste the following, replacing `your_username` with your actual username and `gdrive` if you named your Rclone remote differently:
        ```ini
        [Unit]
        Description=Rclone Google Drive Mount
        AssertPathIsDirectory=%h/GoogleDriveMount
        After=network-online.target

        [Service]
        Type=notify
        ExecStart=/usr/bin/rclone mount gdrive: %h/GoogleDriveMount --vfs-cache-mode full --allow-other --cache-dir=%h/.cache/rclone --log-file=%h/.local/share/rclone/rclone.log
        ExecStop=/bin/fusermount -uz %h/GoogleDriveMount
        Restart=on-failure
        RestartSec=10
        KillMode=none

        [Install]
        WantedBy=default.target
        ```
        **Explanation of options:**
        * `%h`: Shorthand for your home directory (`/home/your_username`).
        * `--allow-other`: Allows other users on the system to access the mount (though generally not needed for a personal sync).
        * `--cache-dir=%h/.cache/rclone`: Specifies a dedicated directory for Rclone's cache files.
        * `--log-file=%h/.local/share/rclone/rclone.log`: Creates a log file for Rclone, useful for debugging.
        * `ExecStop=/bin/fusermount -uz %h/GoogleDriveMount`: Ensures the drive is properly unmounted on shutdown.
        * `WantedBy=default.target`: Makes the service start when your user session starts.

    * **Create the log and cache directories (if they don't exist):**
        ```bash
        mkdir -p ~/.cache/rclone ~/.local/share/rclone
        ```

    * **Enable and start the service:**
        ```bash
        systemctl --user daemon-reload
        systemctl --user enable google-drive.service
        systemctl --user start google-drive.service
        ```
        To check its status:
        ```bash
        systemctl --user status google-drive.service
        ```
        Now, `~/GoogleDriveMount` should be mounted automatically on login.

### 2. **Automating Sync with your Documents Folder**

Once you have a persistently mounted Google Drive folder (`~/GoogleDriveMount`), you can use various tools for syncing.

**A. Using `rsync` (Simple & Robust)**

`rsync` is a fantastic command-line tool for synchronizing files and directories. It's efficient because it only copies changed parts of files.

* **One-way sync (Documents to Google Drive):**
    ```bash
    rsync -av --delete --exclude 'temp_files/' ~/Documents/ ~/GoogleDriveMount/Documents/
    ```
    * `-a`: Archive mode (recursively, preserves permissions, timestamps, etc.).
    * `-v`: Verbose output (shows what's happening).
    * `--delete`: Deletes files in the destination (`~/GoogleDriveMount/Documents/`) that are no longer in the source (`~/Documents/`). **Use with caution!**
    * `--exclude 'temp_files/'`: Excludes a specific folder from syncing. You can add multiple `--exclude` flags.
    * `~/Documents/`: Your local documents folder (note the trailing slash, meaning the *contents* of Documents).
    * `~/GoogleDriveMount/Documents/`: The target folder on your Google Drive mount.

* **Two-way sync (More complex, requires careful handling):**
    True two-way sync with `rsync` can be tricky because it doesn't track changes from both sides simultaneously. You'd typically run two `rsync` commands, one in each direction, but this can lead to conflicts if the same file is modified on both sides between syncs.
    For robust two-way sync, a dedicated client like **Insync** is far superior.

**B. Automating `rsync` with Cron or systemd timer:**

* **Cron (for simple scheduled tasks):**
    ```bash
    crontab -e
    ```
    Add a line like this to run the sync every hour:
    ```cron
    0 * * * * /usr/bin/rsync -av --delete ~/Documents/ ~/GoogleDriveMount/Documents/ >> ~/.local/share/rclone/rsync_documents.log 2>&1
    ```
    This will run at the top of every hour. The `>> ...` redirects output to a log file.

* **systemd timer (more modern and flexible):**
    This is generally preferred over `cron` for user-specific background tasks.

    1.  **Create a service unit:**
        ```bash
        nano ~/.config/systemd/user/sync-documents-to-gdrive.service
        ```
        ```ini
        [Unit]
        Description=Sync Documents to Google Drive
        Requires=google-drive.service # Ensures Rclone mount is active
        After=google-drive.service

        [Service]
        Type=oneshot
        ExecStart=/usr/bin/rsync -av --delete --exclude='temp_files/' %h/Documents/ %h/GoogleDriveMount/Documents/
        StandardOutput=append:/home/%u/.local/share/rclone/sync_documents.log
        StandardError=append:/home/%u/.local/share/rclone/sync_documents.log
        ```

    2.  **Create a timer unit:**
        ```bash
        nano ~/.config/systemd/user/sync-documents-to-gdrive.timer
        ```
        ```ini
        [Unit]
        Description=Run sync-documents-to-gdrive service hourly

        [Timer]
        OnCalendar=hourly
        Persistent=true # Ensures it runs even if system was off
        AccuracySec=1min # For better precision

        [Install]
        WantedBy=timers.target
        ```

    3.  **Enable and start the timer:**
        ```bash
        systemctl --user daemon-reload
        systemctl --user enable sync-documents-to-gdrive.timer
        systemctl --user start sync-documents-to-gdrive.timer
        ```
        You can check the timer status with `systemctl --user status sync-documents-to-gdrive.timer`.

### 3. **Python Program for Syncing in the Background**

Yes, you can absolutely write a Python program for this! The Google Drive API is well-documented, and there are Python client libraries.

**A. Using `PyDrive` (Simplified Google Drive API interaction)**

`PyDrive` is a wrapper around the Google Drive API that makes common tasks much easier.

**Steps:**

1.  **Enable Google Drive API:**
    Go to the Google Cloud Console ([console.cloud.google.com](https://console.cloud.google.com/)).
    * Create a new project (or select an existing one).
    * Go to "APIs & Services" > "Library". Search for "Google Drive API" and enable it.
    * Go to "APIs & Services" > "Credentials".
        * Click "Create Credentials" > "OAuth client ID".
        * Choose "Desktop app" as the application type and give it a name.
        * Download the JSON file (it will be something like `client_secret_YOUR_CLIENT_ID.json`). **Rename this file to `client_secrets.json`** and place it in the same directory as your Python script.

2.  **Install `PyDrive`:**
    ```bash
    pip install PyDrive google-api-python-client
    ```

3.  **Basic Python Sync Script (`sync_documents.py`):**

    This example shows a one-way sync (local to Drive) for new/modified files. A full two-way sync is more complex, requiring careful handling of file IDs, timestamps, and conflict resolution.

    ```python
    from pydrive.auth import GoogleAuth
    from pydrive.drive import GoogleDrive
    import os
    import time

    LOCAL_DOCUMENTS_DIR = os.path.expanduser("~/Documents")
    GDRIVE_PARENT_FOLDER_NAME = "MySyncedDocuments" # Name of the folder on Google Drive
    CLIENT_SECRETS_FILE = "client_secrets.json" # Downloaded from Google Cloud Console

    def get_gdrive_service():
        gauth = GoogleAuth()
        # Try to load saved client credentials
        gauth.LoadCredentialsFile("mycreds.txt")
        if gauth.credentials is None:
            # Authenticate if they're not there
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            # Refresh them if expired
            gauth.Refresh()
        else:
            # Initialize the saved credentials
            gauth.Authorize()
        # Save the current credentials to a file
        gauth.SaveCredentialsFile("mycreds.txt")
        drive = GoogleDrive(gauth)
        return drive

    def get_or_create_folder(drive_service, folder_name, parent_id=None):
        query = f"title = '{folder_name}' and mimeType = 'application/vnd.google-apps.folder' and trashed = false"
        if parent_id:
            query += f" and '{parent_id}' in parents"

        folder_list = drive_service.ListFile({'q': query}).GetList()

        if folder_list:
            return folder_list[0]['id']
        else:
            print(f"Creating folder: {folder_name}")
            folder_metadata = {
                'title': folder_name,
                'mimeType': 'application/vnd.google-apps.folder'
            }
            if parent_id:
                folder_metadata['parents'] = [{'id': parent_id}]
            folder = drive_service.CreateFile(folder_metadata)
            folder.Upload()
            return folder['id']

    def sync_local_to_gdrive(drive_service, local_dir, gdrive_folder_id):
        print(f"Syncing {local_dir} to Google Drive folder ID: {gdrive_folder_id}")
        local_files = {}
        for root, _, files in os.walk(local_dir):
            for file in files:
                local_path = os.path.join(root, file)
                # Get relative path to store on Drive
                rel_path = os.path.relpath(local_path, local_dir)
                local_files[rel_path] = local_path

        # Get existing files on Google Drive for comparison
        gdrive_files = {}
        file_list = drive_service.ListFile({'q': f"'{gdrive_folder_id}' in parents and trashed = false"}).GetList()
        for file in file_list:
            gdrive_files[file['title']] = file # Store PyDrive file object

        for rel_path, local_path in local_files.items():
            file_name = os.path.basename(local_path)
            # This simplified script assumes files are directly in the target folder on Drive.
            # For subfolders, you'd need recursive folder creation logic.

            if file_name in gdrive_files:
                gdrive_file = gdrive_files[file_name]
                local_modified_time = os.path.getmtime(local_path)
                # Convert Google Drive's modifiedDate to a Unix timestamp
                gdrive_modified_time_str = gdrive_file['modifiedDate']
                gdrive_modified_time = time.mktime(time.strptime(gdrive_modified_time_str, '%Y-%m-%dT%H:%M:%S.%fZ'))

                if local_modified_time > gdrive_modified_time:
                    print(f"Updating: {file_name}")
                    gdrive_file.SetContentFile(local_path)
                    gdrive_file.Upload()
                else:
                    # print(f"No update needed for: {file_name}")
                    pass
            else:
                print(f"Uploading new file: {file_name}")
                new_file = drive_service.CreateFile({'title': file_name, 'parents': [{'id': gdrive_folder_id}]})
                new_file.SetContentFile(local_path)
                new_file.Upload()

        # You might also want to implement deletion detection (files removed locally, delete on Drive)
        # and syncing from Drive to local (files changed/added on Drive, download to local).
        # This requires more complex logic to prevent data loss.

    def main():
        drive = get_gdrive_service()
        gdrive_root_folder_id = get_or_create_folder(drive, GDRIVE_PARENT_FOLDER_NAME)

        # For syncing subfolders, you'd need to extend get_or_create_folder
        # and sync_local_to_gdrive to handle recursion.
        # Example: syncing ~/Documents to MySyncedDocuments/Documents on Drive
        documents_on_gdrive_id = get_or_create_folder(drive, "Documents", gdrive_root_folder_id)

        sync_local_to_gdrive(drive, LOCAL_DOCUMENTS_DIR, documents_on_gdrive_id)
        print("Sync completed.")

    if __name__ == "__main__":
        main()
    ```

**Important considerations for the Python script:**

* **Authentication:** The `LocalWebserverAuth()` will open a browser window for initial authentication. After that, `mycreds.txt` will store the tokens for future runs.
* **Two-way Sync Complexity:** The provided script is a basic *one-way* sync (local to Drive) for new/modified files. True bidirectional sync is significantly more complex:
    * **File IDs:** You need to store Google Drive file IDs locally to track changes efficiently.
    * **Deletion:** How do you handle files deleted on one side?
    * **Conflicts:** What happens if a file is modified on both local and Drive between syncs? You need a conflict resolution strategy (e.g., keep newest, create a copy, prompt user).
    * **Google Docs:** Google Docs, Sheets, and Slides are special file types. The API can export them to standard formats (e.g., DOCX, XLSX), but syncing them as native Google documents requires more logic.
* **Error Handling:** Add robust `try-except` blocks for network issues, API errors, etc.
* **Background Execution:**
    * You can run this script periodically using `cron` or `systemd` timers, just like `rsync`.
    * You could also turn it into a long-running daemon using libraries like `python-daemon` and then use `inotify` (Linux kernel feature) to watch the local `~/Documents` folder for real-time changes and trigger uploads. This is more advanced.

**B. Using `rclone` with Python (Best of both worlds)**

Instead of writing complex API logic in Python, you can use Python to *orchestrate* `rclone` commands. This is often simpler and more robust, as `rclone` handles all the complex syncing logic.

```python
import subprocess
import os
import time

LOCAL_DOCUMENTS_DIR = os.path.expanduser("~/Documents")
GDRIVE_REMOTE_PATH = "gdrive:Documents" # Assuming 'gdrive' is your Rclone remote name and you want to sync to a 'Documents' folder on Drive

def run_rclone_sync():
    print(f"Starting Rclone sync from {LOCAL_DOCUMENTS_DIR} to {GDRIVE_REMOTE_PATH}")
    # Use rsync's sync command for one-way sync (local to cloud)
    # --delete-excluded to remove files on remote if they are excluded locally
    # --delete-after to delete files after transfer (safer than before)
    # --exclude patterns can be added as needed
    command = [
        "rclone", "sync",
        LOCAL_DOCUMENTS_DIR,
        GDRIVE_REMOTE_PATH,
        "--verbose",
        "--log-file", os.path.expanduser("~/.local/share/rclone/python_sync.log"),
        "--checkers", "8", # Number of checksum verifiers
        "--transfers", "4", # Number of parallel file transfers
        "--progress" # Show progress during sync
    ]

    try:
        # Run the command and capture output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print("Rclone sync successful.")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Rclone sync failed with error code {e.returncode}")
        print("STDOUT:", e.stdout)
        print("STDERR:", e.stderr)
    except FileNotFoundError:
        print("Error: rclone command not found. Make sure rclone is installed and in your PATH.")

def main_loop():
    while True:
        run_rclone_sync()
        print("Waiting for 30 minutes before next sync...")
        time.sleep(30 * 60) # Sync every 30 minutes

if __name__ == "__main__":
    # Ensure log directory exists
    os.makedirs(os.path.expanduser("~/.local/share/rclone"), exist_ok=True)
    main_loop()
```

This Python script simply executes the `rclone sync` command. You would then run this Python script in the background, perhaps using `nohup` or `screen`/`tmux` or even a `systemd` service for the Python script itself.

**To run the Python script in the background:**

* **Using `nohup` (simple, keeps running after terminal close):**
    ```bash
    nohup python3 /path/to/your/sync_documents.py &
    ```
    Output will be redirected to `nohup.out`.

* **Using `systemd` (recommended for robustness and auto-restart):**
    This is similar to how you set up the `rclone mount` service.

    1.  **Create a service file:**
        ```bash
        nano ~/.config/systemd/user/python-gdrive-sync.service
        ```
        ```ini
        [Unit]
        Description=Python Google Drive Document Sync
        After=network-online.target google-drive.service # Depends on network and Rclone mount
        Requires=google-drive.service

        [Service]
        ExecStart=/usr/bin/python3 /path/to/your/sync_documents.py
        WorkingDirectory=/path/to/your/script/directory # Where client_secrets.json is
        StandardOutput=append:/home/%u/.local/share/rclone/python_sync_daemon.log
        StandardError=append:/home/%u/.local/share/rclone/python_sync_daemon.log
        Restart=on-failure
        RestartSec=30

        [Install]
        WantedBy=default.target
        ```
        **Remember to replace `/path/to/your/sync_documents.py` and `/path/to/your/script/directory` with actual paths.**

    2.  **Enable and start the service:**
        ```bash
        systemctl --user daemon-reload
        systemctl --user enable python-gdrive-sync.service
        systemctl --user start python-gdrive-sync.service
        ```

For a truly reliable, automated, and bidirectional sync solution, **Insync** remains the easiest and most feature-rich option for Linux. However, if you prefer a free, open-source, and highly customizable solution, combining **Rclone** for mounting and syncing with `cron` or `systemd` timers, or even a simple Python script to orchestrate `rclone`, will give you excellent results.