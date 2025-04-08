import feedparser
import json

def collect():
    """
    Collects bug bounty related writeups from Medium using the RSS feed.
    
    Returns:
        list: A list of writeups with title, URL, publication date, source, and tags.
    """
    rss_url = "https://medium.com/feed/tag/bug-bounty"  # URL of the Medium RSS feed
    feed = feedparser.parse(rss_url)

    writeups = []

    print("🔍 Collecting writeups from Medium...\n")

    # Ensure there are entries in the feed
    if not feed.entries:
        print("⚠️ No writeups found in the feed.")
        return []

    # Process each entry in the feed
    for entry in feed.entries:
        writeup = {
            "title": entry.title,
            "url": entry.link,
            "published": entry.published,
            "source": "Medium",
            "tags": extract_tags(entry)  # Tags extracted dynamically from the RSS
        }
        writeups.append(writeup)

    return writeups

def extract_tags(entry):
    """
    Extracts tags from the Medium entry. Can be customized if needed.
    
    Parameters:
        entry (dict): The entry dictionary from the RSS feed.

    Returns:
        list: A list of tags for the entry.
    """
    return ["bug-bounty"]  # Static tag, can be expanded if necessary.

def save_writeups_to_file(writeups, filename="writeups_medium.json"):
    """
    Saves the collected writeups to a JSON file.
    
    Parameters:
        writeups (list): The list of writeups to be saved.
        filename (str): The name of the file to save the writeups.
    """
    with open(filename, "w") as f:
        json.dump(writeups, f, indent=2)

    print(f"\n✅ Saved {len(writeups)} writeups to {filename}.")

# Main function to collect and save writeups
def main():
    writeups = collect()  # Collect the writeups from Medium

    if writeups:
        save_writeups_to_file(writeups)  # Save them if any were collected
    else:
        print("❌ No writeups collected.")

if __name__ == "__main__":
    main()
