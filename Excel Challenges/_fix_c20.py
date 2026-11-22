import json

path = r"c:\Users\WIN11\Downloads\_delete_later\Python_General_Test\Excel Challenges\Challenges.ipynb"

with open(path, "r", encoding="utf-8") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell.get("id") == "cell-044":
        # Clear the error output so the cell is clean to re-run
        cell["outputs"] = []
        cell["execution_count"] = None
        cell["source"] = [
            "from datetime import datetime, timedelta\n",
            "\n",
            "def move_last24h_xlsx_files_to_backup(actual_folder, backup_folder):\n",
            "    now = datetime.now()\n",
            "    try:\n",
            "        # if not os.path.backup_folder:\n",
            "        if not os.path.exists(backup_folder):\n",
            "            os.makedirs(backup_folder)\n",
            "        for file in os.listdir(actual_folder):\n",
            "            # if file.endswith(\"xlsx\"):\n",
            "            if file.endswith(\".xlsx\"):\n",
            "                full_path = os.path.join(actual_folder, file)\n",
            "                # file_modified_time = datetime.fromtimestamp(file)\n",
            "                file_modified_time = datetime.fromtimestamp(os.path.getmtime(full_path))\n",
            "                if now - file_modified_time < timedelta(hours=24):\n",
            "                    # shutil.copy(file, backup_folder)\n",
            "                    shutil.copy(full_path, os.path.join(backup_folder, file))\n",
            "                    logger.info(f\"File {file} copied to backup folder.\")\n",
            "                else:\n",
            "                    logger.info(f\"File {file} was not copied (older than 24h).\")\n",
            "    except Exception as e:\n",
            "        logger.error(f\"Error: {e}\")\n",
            "\n",
            "move_last24h_xlsx_files_to_backup(actual_folder=r\"C:\\Users\\WIN11\\Downloads\\_delete_later\\Python_General_Test\\Excel Challenges\",\n",
            "                                    backup_folder=r\"C:\\Users\\WIN11\\Downloads\\_delete_later\\Python_General_Test\\Excel Challenges\\backup\")",
        ]
        break

with open(path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=True)
    f.write("\n")

print("Done")
