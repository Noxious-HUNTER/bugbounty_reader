from collectors import pentesterland, medium
from core.classify import classify_writeups
import json
import subprocess
import os

DATA_PATH = "data/writeups.json"

def load_writeups():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r") as f:
            return json.load(f)
    return []

def save_writeups(writeups):
    with open("new_writeups.json", "w") as f:
        json.dump(writeups, f, indent=4)

    subprocess.run(f"cat new_writeups.json | anew {DATA_PATH}", shell=True)
    os.remove("new_writeups.json")

def update():
    print("🔄 Fetching new writeups...")
    writeups = pentesterland.collect() + medium.collect()
    classified = classify_writeups(writeups)
    save_writeups(classified)
    print("✅ Writeups updated.")

if __name__ == "__main__":
    update()
