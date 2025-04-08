import feedparser
import json

def fetch_medium_writeups():
    rss_url = "https://medium.com/feed/tag/bug-bounty"  # می‌تونیم چند تا URL هم به این اضافه کنیم
    feed = feedparser.parse(rss_url)

    writeups = []

    print("🔍 Collecting writeups from Medium...\n")

    for entry in feed.entries:
        writeups.append({
            "title": entry.title,
            "url": entry.link,
            "published": entry.published,
            "source": "Medium",
            "tags": ["bug-bounty"]  # می‌تونیم تگ‌ها رو از خود RSS هم استخراج کنیم
        })

    return writeups

# ذخیره‌سازی به فایل
writeups = fetch_medium_writeups()
with open("writeups_medium.json", "w") as f:
    json.dump(writeups, f, indent=2)

print(f"\n✅ Collected {len(writeups)} writeups from Medium.")
