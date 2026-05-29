import requests
import feedparser
import random
import re
from app import app
from extensions import db
from models import News


# -----------------------------------------
# SEARCH TERMS FOR BING RSS
# -----------------------------------------
SEARCH_TERMS = [
    "mountaineering",
    "trekking",
    "climbing",
    "expedition",
    "hiking",
    "himalaya",
    "everest"
]


# -----------------------------------------
# HUMAN‑STYLE REWRITE ENGINE
# -----------------------------------------
def rewrite_text_local(text):
    rewritten = text.strip()

    filler_sentences = [
        "Local officials familiar with the situation said the update has drawn attention among trekkers and guides in the region.",
        "People following the development noted that it reflects ongoing changes in mountain conditions and travel patterns.",
        "Several observers mentioned that the situation adds new context to the challenges faced by high‑altitude communities.",
        "Those who frequently travel in the area believe this could influence future trekking plans and safety guidelines.",
        "Experts say such developments often highlight broader patterns in weather, climate, and adventure tourism.",
        "Residents near popular routes commented that interest in the region continues to grow each season.",
        "Adventure groups have been sharing reactions and insights as more details become available.",
        "Environmental specialists emphasize that preparation and awareness remain essential for anyone exploring remote mountain terrain."
    ]

    while len(rewritten.split()) < 220:
        rewritten += " " + random.choice(filler_sentences)

    words = rewritten.split()
    paragraphs = []
    chunk = []

    for i, word in enumerate(words, 1):
        chunk.append(word)
        if i % random.randint(70, 95) == 0:
            paragraphs.append(" ".join(chunk))
            chunk = []

    if chunk:
        paragraphs.append(" ".join(chunk))

    return "\n\n".join(paragraphs)


# -----------------------------------------
# BBC / CNN STYLE TITLE GENERATOR
# -----------------------------------------
def rewrite_title_local(title):
    patterns = [
        "{}: New Report Released",
        "Officials Confirm Update on {}",
        "Fresh Details Emerge About {}",
        "Authorities Issue Statement on {}",
        "{} Raises New Questions",
        "Experts Assess Latest Developments in {}",
        "{} Sparks Regional Attention",
        "New Findings Shed Light on {}",
        "Update: {}",
        "{} Under Review After Recent Events",
        "What We Know So Far About {}",
        "Investigation Continues Into {}",
        "Latest Developments Surrounding {}",
        "{}: Key Information Released"
    ]
    return random.choice(patterns).format(title)


# -----------------------------------------
# META DESCRIPTION GENERATOR
# -----------------------------------------
def generate_meta_description(text):
    clean = re.sub(r"\s+", " ", text)
    return clean[:150]


# -----------------------------------------
# SLUG GENERATOR
# -----------------------------------------
def generate_slug(title):
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", title.lower()).strip("-")
    return slug[:60]


# -----------------------------------------
# TAG GENERATOR
# -----------------------------------------
def generate_tags(text):
    keywords = ["mountain", "trekking", "climbing", "expedition", "hiking", "everest", "himalaya"]
    tags = [k for k in keywords if k in text.lower()]
    if not tags:
        tags = ["adventure", "outdoors", "travel"]
    return ", ".join(tags)


# -----------------------------------------
# AUTO‑FEATURED IMAGE (UNSPLASH)
# -----------------------------------------
def generate_image_url(text):
    keywords = [
        "mountain", "trekking", "climbing", "hiking",
        "expedition", "everest", "himalaya", "adventure", "outdoors"
    ]

    for k in keywords:
        if k in text.lower():
            return f"https://source.unsplash.com/1200x700/?{k}"

    return "https://source.unsplash.com/1200x700/?mountain"


# -----------------------------------------
# MAIN FETCHER FUNCTION
# -----------------------------------------
def fetch_and_save_news():
    with app.app_context():
        print("Fetching rewritten mountain & trekking news...")

        for term in SEARCH_TERMS:
            url = f"https://www.bing.com/news/search?q={term}&format=rss"

            r = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
            feed = feedparser.parse(r.text)

            print(f"{term}: {len(feed.entries)} articles")

            for entry in feed.entries:
                original_title = entry.title
                original_summary = getattr(entry, "summary", "")
                link = entry.link

                if News.query.filter_by(source_url=link).first():
                    continue

                rewritten_title = rewrite_title_local(original_title)
                rewritten_summary = rewrite_text_local(original_summary)
                meta_desc = generate_meta_description(rewritten_summary)
                slug = generate_slug(rewritten_title)
                tags = generate_tags(rewritten_summary)

                image_url = generate_image_url(rewritten_summary)
                print("IMAGE URL GENERATED:", image_url)

                news_item = News(
                    title=rewritten_title,
                    summary=rewritten_summary,
                    category="Trekking",
                    image_url=image_url,
                    meta_title=rewritten_title,
                    meta_description=meta_desc,
                    source_url=link,
                    slug=slug,
                    tags=tags
                )

                print("SAVED IMAGE URL:", news_item.image_url)

                db.session.add(news_item)

        db.session.commit()
        print("Rewritten news updated successfully.")


# -----------------------------------------
# RUN SCRIPT
# -----------------------------------------
if __name__ == "__main__":
    fetch_and_save_news()
