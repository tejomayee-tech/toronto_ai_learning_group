To uninstall Visual Studio Code that you installed via the Debian (.deb) file on a Debian/Ubuntu-based system, you should use the package manager's remove command with the correct package name.

The package name for the official VS Code installation from the `.deb` file is typically **`code`**.

Here are the steps to completely uninstall it:

## 1\. Uninstall the VS Code Package

Open your terminal and run the following command to remove the VS Code application and its configuration files. Using `purge` is recommended for a clean removal.

```bash
sudo apt purge code
```

  * **`sudo`**: Runs the command with root privileges.
  * **`apt purge`**: Uninstalls the specified package **and** removes its system-wide configuration files.
  * **`code`**: The package name for Visual Studio Code.

-----

## 2\. Remove Unnecessary Dependencies

After removing the main package, run this command to automatically remove any dependencies that were installed with VS Code and are no longer needed by other programs on your system.

```bash
sudo apt autoremove
```

-----

## 3\. Delete User Configuration Files (Optional)

The commands above remove the core application files, but they usually leave behind user-specific configuration and extension data in your home directory. If you want a **complete** removal, run these commands to delete those directories:

```bash
rm -rf ~/.config/Code
rm -rf ~/.vscode
```

  * **`rm -rf`**: Recursively and forcefully deletes the specified directory and its contents.
  * **`~/.config/Code`**: Contains user settings, cached data, and workspaces.
  * **`~/.vscode`**: Contains your installed extensions.

> ⚠️ **Caution**: Once you run the `rm -rf` commands, the data is permanently deleted. If you plan to reinstall VS Code later and want to keep your extensions or settings, skip this step.