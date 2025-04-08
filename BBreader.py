import argparse
from collectors import pentesterland, medium
from core.classify import classify_writeups
import json
import os
import subprocess

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

def filter_writeups(topic=None, source=None):
    writeups = load_writeups()
    filtered = [
        w for w in writeups
        if (not topic or topic in w["tags"]) and (not source or w["source"] == source)
    ]
    for w in filtered:
        print(f"{w['date']} - {w['title']} [{w['source']}]")
        print(w["url"])
        print("Tags:", ", ".join(w["tags"]))
        print("-" * 80)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--collect", action="store_true", help="Collect writeups")
    parser.add_argument("--filter", action="store_true", help="Filter writeups")
    parser.add_argument("--source", help="Source name (e.g. pentesterland, medium)")
    parser.add_argument("--topic", help="Filter by topic (e.g. xss, ssrf)")
    parser.add_argument("--update", action="store_true", help="Update writeups")

    args = parser.parse_args()

    if args.collect:
        writeups = pentesterland.collect() + medium.collect()
        classified = classify_writeups(writeups)
        save_writeups(classified)
        print("✅ Collection complete.")

    elif args.filter:
        filter_writeups(topic=args.topic, source=args.source)

    elif args.update:
        print("🔄 Updating writeups...")
        writeups = pentesterland.collect() + medium.collect()
        classified = classify_writeups(writeups)
        save_writeups(classified)
        print("✅ Update done.")

if __name__ == "__main__":
    main()
