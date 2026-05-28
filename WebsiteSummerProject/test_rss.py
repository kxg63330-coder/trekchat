import requests
import feedparser

url = "https://explorersweb.com/feed/"

try:
    r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    print("HTTP Status:", r.status_code)
    print("Content length:", len(r.text))
    feed = feedparser.parse(r.text)
    print("Entries:", len(feed.entries))
except Exception as e:
    print("Error:", e)
