import os
import shutil

target_dir = r"C:\Users\momom\OneDrive\Pictures"

EXTENSIONS = {
    ".pdf": "PDFs",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".docx": "Documents",
    ".blend" : "Blender"
    }

files = os.listdir(target_dir)

for file in files:
    file_path = os.path.join(target_dir, file)
    if os.path.isdir(file_path):
        continue

    _, ext = os.path.splitext(file)
    ext = ext.lower()

    if ext in EXTENSIONS:
        folder_name = EXTENSIONS[ext]
        folder_path = os.path.join(target_dir, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)


        shutil.move(file_path, os.path.join(folder_path, file))
        print(f"Moved {file} -> {folder_name}/")