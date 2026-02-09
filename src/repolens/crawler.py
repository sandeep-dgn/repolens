import os

def scan_repository(root_path="."):
    """Check: Can I see the files?"""
    files_found = []
    ignore_list = {'.git', '.venv', '__pycache__', 'node_modules'}

    for root, dirs, files in os.walk(root_path):
        dirs[:] = [d for d in dirs if d not in ignore_list]
        for file in files:
            if file.endswith(('.py', '.md')):
                files_found.append(os.path.join(root, file))
    return files_found

def get_code_context(file_paths):
    """Check: Can I read the files?"""
    context = ""
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                context += f"\n--- FILE: {path} ---\n{f.read()}\n"
        except Exception as e:
            print(f"⚠️ Skip {path}: {e}")
    return context