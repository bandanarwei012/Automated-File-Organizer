# Automated File Organizer

A simple but powerful Python script to organize files in a directory into subfolders based on their file type. This helps in decluttering folders like "Downloads" or "Desktop".

## Features

- **Configurable:** Easily define your own categories and file extensions using the `config.json` file.
- **Smart:** Automatically creates destination folders if they don't exist.
- **Safe:** Moves files and prints the action for each file. It will not delete anything.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## How to Use

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/automated-file-organizer.git
    cd automated-file-organizer
    ```

2.  **Customize the Configuration (Optional):**
    Open the `config.json` file and modify the categories and file extensions to suit your needs. Any file type not listed will be moved to a folder named "Other".

3.  **Run the Script:**
    You can run the script in two ways:

    *   **Provide the path as a command-line argument:**
        ```bash
        python organize.py "/path/to/your/folder"
        ```
        For example, to organize your Downloads folder:
        ```bash
        python organize.py "C:/Users/YourUser/Downloads"
        ```

    *   **Run without arguments and enter the path when prompted:**
        ```bash
        python organize.py
        ```
        The script will then ask you to input the directory path.

## Project Structure
