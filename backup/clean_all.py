import os

log_files = ["json_request.txt", "log.txt"]
nonexistent_files = []
deleted_files = []

for file in log_files:
    if os.path.exists(file):
        os.remove(file)
        deleted_files.append(file)
    else:
        nonexistent_files.append(file)

if nonexistent_files:
    print(f"\033[91m🔴 Les fichiers suivants n'existent pas : {', '.join(nonexistent_files)} 🔴\033[0m")
if deleted_files:
    print(f"\033[92m🟢 Les fichiers suivants ont été supprimés avec succès : {', '.join(deleted_files)} 🟢\033[0m")
