## Overview

**BewareGitHub** is a simplistic tool, crafted with Python, designed to automatically clone and backup GitHub repositories to local storage and servers. By monitoring GitHub Webhooks, it autonomously triggers a backup process and creates a local copy of the repository whenever updates are detected in the remote repository.

## Key Features

- **Automatic Cloning**: Configurable to autonomously clone specified GitHub repositories.
- **Local Backups**: Generates local storage copies of GitHub repositories, facilitating offline access and secure storage.
- **Scheduled Backups**: Default backup times are set at 12:00, 18:00, 00:00, and 6:00.
- **Real-time Webhook Response**: Responds to GitHub Webhooks to ensure real-time backups upon repository updates.
- **Conditional Backup on Commit**: Automatically initiates a backup process when the commit message contains the character ‘备’. This feature ensures that critical updates, denoted by the user through their commit messages, prompt an immediate backup, safeguarding the latest changes efficiently.

## User Guide

### Basic Configuration

First and foremost, configure the following variables within the script to cater to your usage scenario:

```python
REPO_HTTPS_URL = "https://github.com/USERNAME/REPO.git"  # GitHub Repository URL
USERNAME = "YOUR_USERNAME"  # GitHub Username
PASSWORD = "YOUR_PASSWORD"  # GitHub Personal access tokens
REPO_DIR = "./REPO"  # Local Repository Path
BACKUP_DIR = "./BACKUP"  # Local Backup Path
CACHE_DIR = "./cache"  # Cache Path
LOG_FILE = "./log.txt"  # Log File Path
BACKUP_TYPE = 3  # Backup Type 1: Enable Local Scheduled Backup, 2: Enable Remote Scheduled Backup, 3: Disable Scheduled Backup
```

Note: Apply for Personal access tokens within [Developer Settings](https://github.com/settings/tokens), ensuring repository access permissions are enabled.

### Operating BewareGitHub

Upon configuration completion, execute BewareGitHub with the following command:

```bash
python beware_github.py
```

This command launches BewareGitHub and its intrinsic Flask service, awaiting Webhook requests from GitHub.

### Configuring GitHub Webhook

To ensure BewareGitHub responds to changes in the GitHub repository, Webhook configuration within the GitHub repository is necessary. Below are the detailed steps:

1. **Configure Public Server IP/Domain**: Ensure your server is accessible by GitHub.
2. **Navigate to Repository Settings**: On the GitHub repository page, click "Settings" -> "Webhooks".
3. **Add Webhook**: Click "Add webhook".
4. **Webhook Configuration**:
   - **Payload URL**: Input `http://YOUR_SERVER_IP:6110/webhook` (replace `YOUR_SERVER_IP` with your actual server IP/domain).
   - **Content type**: Select `application/json`.
   - **Active**: Ensure this option is selected to activate the Webhook.
5. **Save Webhook**: Click "Add webhook" to finalize the configuration.

Now, whenever a new push event occurs in your GitHub repository, BewareGitHub will automatically activate the relevant cloning or backup processes.

## Log

All operations and system events are logged, and can be located within the file at the configured `LOG_FILE` path, serving to trace BewareGitHub activity and troubleshoot potential issues.
