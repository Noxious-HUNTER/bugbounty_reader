import feedparser
from tqdm import tqdm

def collect():
    url = "https://medium.com/feed/@bugbounty"
    writeups = []

    print(f"📡 Fetching: {url}")
    feed = feedparser.parse(url)

    for entry in tqdm(feed.entries, desc="Extracting writeups"):
        writeups.append({
            "title": entry.title,
            "url": entry.link,
            "description": entry.summary,
            "date": entry.published,
            "source": "medium",
            "tags": ["bugbounty"]
        })

    return writeups
