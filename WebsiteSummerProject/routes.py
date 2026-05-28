from flask import render_template, request, redirect
from app import app
from models import Route, Blog, Emergency, News   # <-- Added News model
from extensions import db
import requests
import os
import re
from werkzeug.utils import secure_filename
from slugify import slugify   # <-- Added slugify

API_KEY = "3f8a8d45fd9441e3b83152520261405"

# -----------------------------
# IMAGE FETCHER (Pexels API)
# -----------------------------
PEXELS_API_KEY = "wlq17X0Os2yfEIAvTWkvLOp3EacPoIRr1fSZKY3gLtcxupZzdcYuYaNV"

def get_image(query):
    headers = {"Authorization": PEXELS_API_KEY}
    url = f"https://api.pexels.com/v1/search?query={query}&per_page=1"
    r = requests.get(url, headers=headers).json()
    if "photos" in r and len(r["photos"]) > 0:
        return r["photos"][0]["src"]["large"]
    return "/static/default.jpg"


# -----------------------------
# LONG CONTENT GENERATOR
# -----------------------------
def generate_long_content(title, summary):
    return f"""
<h2>{title}</h2>

<p>{summary}</p>

<h3>Overview</h3>
<p>The Himalayan region of Nepal, including Everest, Annapurna, and Manaslu, continues to attract global attention due to its dramatic weather patterns, climbing expeditions, and environmental challenges.</p>

<h3>Current Situation</h3>
<p>Recent updates indicate shifting weather conditions, increased trekking activity, and ongoing conservation efforts. Local authorities and mountaineering agencies have issued advisories for climbers and trekkers in the Everest and Annapurna regions.</p>

<h3>Impact on Climbers and Trekkers</h3>
<ul>
    <li>Visibility changes affecting summit pushes</li>
    <li>Temperature fluctuations in high‑altitude camps</li>
    <li>Route adjustments by Sherpa teams</li>
    <li>Increased monitoring of avalanche‑prone zones</li>
</ul>

<h3>Expert Insights</h3>
<p>Guides and expedition leaders report that conditions remain manageable but require caution.</p>

<h3>Conclusion</h3>
<p>The Himalayas remain one of the world’s most dynamic mountain environments. Whether in Everest Base Camp, Annapurna Circuit, or Manaslu region, trekkers are encouraged to follow safety guidelines and stay informed.</p>
"""


# -----------------------------
# WEATHER
# -----------------------------
@app.route('/weather')
def weather():
    city = "Warrensburg"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    weather_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
        "humidity": data["main"]["humidity"]
    }

    return render_template("weather.html", weather=weather_data)


# -----------------------------
# HOME
# -----------------------------


# -----------------------------
# HOMEPAGE DATA (TEMPORARY FIX)
# -----------------------------

popular_routes = [
    {
        "id": 1,
        "name": "Everest Base Camp",
        "country": "Nepal",
        "difficulty": "Hard",
        "distance_km": 65,
        "image_url": "/static/images/everest.jpg"
    },
    {
        "id": 2,
        "name": "Annapurna Circuit",
        "country": "Nepal",
        "difficulty": "Medium",
        "distance_km": 160,
        "image_url": "/static/images/annapurna.jpg"
    }
]

weather_data = [
    {"city": "Kathmandu", "temp": 22, "windspeed": 5},
    {"city": "Pokhara", "temp": 25, "windspeed": 3}
]

popular_posts = [
    {
        "id": 1,
        "title": "Top 10 Trekking Tips",
        "content": "Always carry enough water and check the weather...",
        "featured_image": "/static/images/blog1.jpg"
    },
    {
        "id": 2,
        "title": "Best Himalayan Treks",
        "content": "The Himalayas offer some of the most beautiful routes...",
        "featured_image": "/static/images/blog2.jpg"
    }
]

@app.route('/')
def home():
    return render_template(
        'index.html',
        popular_routes=popular_routes,
        weather_data=weather_data,
        popular_posts=popular_posts
    )

# -----------------------------
# ROUTES PAGE
# -----------------------------
@app.route('/routes')
def routes():
    all_routes = Route.query.all()
    return render_template('routes.html', routes=all_routes)


# -----------------------------
# BLOG PAGE
# -----------------------------
@app.route('/blog')
def blog():
    posts = Blog.query.all()
    return render_template('blog.html', posts=posts)


# -----------------------------
# EMERGENCY ALERT
@app.route('/emergency', methods=['GET', 'POST'])
def emergency():
    if request.method == 'POST':
        msg = request.form['message']
        loc = request.form['location']

        alert = Emergency(message=msg, location=loc)
        db.session.add(alert)
        db.session.commit()

    return redirect('/emergency-alerts')

# -----------------------------
# ROUTE DETAIL PAGE
# -----------------------------
@app.route('/route/<int:route_id>')
def route_detail(route_id):
    route = Route.query.get_or_404(route_id)
    return render_template('route_detail.html', route=route)


# -----------------------------
# ADD BLOG POST
# -----------------------------
@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        seo_title = request.form['seo_title']
        meta_description = request.form['meta_description']
        category = request.form['category']
        tags = request.form['tags']
        action = request.form['action']

        slug = slugify(title)

        image_file = request.files.get('featured_image')
        image_path = None

        if image_file and image_file.filename != "":
            filename = secure_filename(image_file.filename)
            image_path = os.path.join("static/uploads", filename)
            image_file.save(image_path)

        new_post = Blog(
            title=title,
            content=content,
            seo_title=seo_title,
            meta_description=meta_description,
            category=category,
            tags=tags,
            featured_image=image_path,
            is_draft=(action == "draft"),
            slug=slug
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect('/blog')

    return render_template('add_post.html')


@app.route('/proxy_image')
def proxy_image():
    import requests
    from flask import Response, request

    url = request.args.get('url')
    if not url:
        return "No URL provided", 400

    try:
        r = requests.get(url, timeout=5)
        return Response(r.content, mimetype=r.headers.get("Content-Type"))
    except:
        return "Failed to fetch image", 500


@app.route('/global-alerts')
def global_alerts():
    url = "https://api.reliefweb.int/v1/disasters?appname=travelapp&profile=full&limit=20"
    data = requests.get(url).json()

    alerts = []
    for item in data.get("data", []):
        fields = item.get("fields", {})
        alerts.append({
            "title": fields.get("name"),
            "type": fields.get("type"),
            "country": fields.get("country", [{}])[0].get("name", "Unknown"),
            "date": fields.get("date", {}).get("created"),
            "status": fields.get("status"),
        })

    return render_template("global_alerts.html", alerts=alerts)


REGIONS = {
    "asia": [
        "India", "Nepal", "China", "Japan", "Pakistan", "Bangladesh",
        "Sri Lanka", "Indonesia", "Malaysia", "Thailand", "Vietnam",
        "Philippines", "South Korea", "North Korea", "Mongolia"
    ],
    "europe": [
        "United Kingdom", "France", "Germany", "Italy", "Spain",
        "Norway", "Sweden", "Finland", "Poland", "Ukraine",
        "Netherlands", "Belgium", "Switzerland", "Austria"
    ],
    "africa": [
        "Kenya", "South Africa", "Nigeria", "Ethiopia", "Egypt",
        "Morocco", "Ghana", "Uganda", "Tanzania", "Algeria"
    ],
    "north_america": [
        "United States", "Canada", "Mexico"
    ],
    "south_america": [
        "Brazil", "Argentina", "Chile", "Peru", "Colombia"
    ],
    "oceania": [
        "Australia", "New Zealand", "Fiji", "Papua New Guinea"
    ]
}
@app.route('/emergency-alerts')
def emergency_alerts():
    import requests
    import feedparser

    headers = {
        "User-Agent": "Mozilla/5.0 (TrekChat Emergency Alerts)"
    }

    world_alerts = []

    # -------------------------
    # 1. GDACS (RSS via requests)
    # -------------------------
    try:
        gdacs_xml = requests.get("https://www.gdacs.org/xml/rss.xml", headers=headers, timeout=5).text
        gdacs_feed = feedparser.parse(gdacs_xml)

        for entry in gdacs_feed.entries:
            world_alerts.append({
                "source": "GDACS",
                "title": entry.get("title", "No title"),
                "summary": entry.get("summary", "No summary"),
                "link": entry.get("link", "#"),
                "date": entry.get("published", "Unknown date")
            })
    except Exception as e:
        print("GDACS ERROR:", e)

    # -------------------------
    # 2. ReliefWeb (API with headers)
    # -------------------------
    try:
        rw_url = "https://api.reliefweb.int/v1/disasters?profile=full&limit=20"
        rw_data = requests.get(rw_url, headers=headers, timeout=5).json()

        for item in rw_data.get("data", []):
            fields = item.get("fields", {})
            world_alerts.append({
                "source": "ReliefWeb",
                "title": fields.get("name"),
                "summary": fields.get("description", "No summary"),
                "link": fields.get("url", "#"),
                "date": fields.get("date", {}).get("created", "Unknown date")
            })
    except Exception as e:
        print("RELIEFWEB ERROR:", e)

    # -------------------------
    # 3. NASA FIRMS (Public endpoint)
    # -------------------------
    try:
        nasa_url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_Global_24h.csv"
        nasa_csv = requests.get(nasa_url, headers=headers, timeout=5).text
        lines = nasa_csv.split("\n")[1:20]

        for line in lines:
            cols = line.split(",")
            if len(cols) > 5:
                world_alerts.append({
                    "source": "NASA FIRMS",
                    "title": "Wildfire Detected",
                    "summary": f"Location: {cols[0]}, {cols[1]} — Brightness: {cols[2]}",
                    "link": "https://firms.modaps.eosdis.nasa.gov/",
                    "date": cols[5]
                })
    except Exception as e:
        print("NASA ERROR:", e)

    print("WORLD ALERTS:", len(world_alerts))

    return render_template("emergency_alerts.html", world_alerts=world_alerts)
