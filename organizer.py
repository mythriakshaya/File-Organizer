import os
import shutil

# Define file categories
file_types = {
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "HTML": [".html", ".htm"],
    "Python Scripts": [".py"],
}

# Get the current folder path
folder_path = os.getcwd()

# Create folders if they don’t exist
for folder in file_types.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

# Organize files
for file in os.listdir(folder_path):
    file_ext = os.path.splitext(file)[1]  # Get file extension
    for category, extensions in file_types.items():
        if file_ext in extensions:
            shutil.move(file, os.path.join(folder_path, category, file))
            print(f"Moved {file} to {category}")

print("✅ Organization Complete!")

