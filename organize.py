import os
import shutil
import json
import sys

def load_config(config_path='config.json'):
    """Loads the configuration file for file categories."""
    try:
        with open(config_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{config_path}'.")
        return None

def organize_directory(path, config):
    """
    Organizes files in the given directory based on the rules in the config.
    
    Args:
        path (str): The path to the directory to organize.
        config (dict): A dictionary mapping folder names to file extensions.
    """
    if not os.path.isdir(path):
        print(f"Error: The specified path '{path}' is not a valid directory.")
        return

    print(f"Scanning directory: {path}\n")
    files_moved = 0
    
    # Create a reverse mapping from extension to folder name for quick lookups
    extension_mapping = {ext: folder for folder, exts in config.items() for ext in exts}

    # Iterate over all items in the source directory
    for filename in os.listdir(path):
        source_file_path = os.path.join(path, filename)

        # Skip if it's a directory
        if os.path.isdir(source_file_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)
        file_extension = file_extension.lower()

        # Determine the destination folder
        destination_folder_name = extension_mapping.get(file_extension, 'Other')
        destination_folder_path = os.path.join(path, destination_folder_name)

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder_path, exist_ok=True)
        
        destination_file_path = os.path.join(destination_folder_path, filename)

        # Move the file
        try:
            shutil.move(source_file_path, destination_file_path)
            print(f"Moved: '{filename}' -> {destination_folder_name}/")
            files_moved += 1
        except Exception as e:
            print(f"Error moving '{filename}': {e}")
            
    print(f"\nOrganization complete. Total files moved: {files_moved}")

if __name__ == "__main__":
    # Load configuration
    config = load_config()
    
    if config:
        # Get directory from command-line argument or prompt the user
        if len(sys.argv) > 1:
            target_directory = sys.argv[1]
        else:
            target_directory = input("Enter the path of the directory to organize: ")
        
        organize_directory(target_directory, config)
