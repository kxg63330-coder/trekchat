import os
from flask import Flask, render_template, request, redirect, session
import requests

from extensions import db
from werkzeug.security import check_password_hash, generate_password_hash
from flask_migrate import Migrate
import markdown
from markupsafe import Markup
from sqlalchemy import or_
from datetime import datetime
from models import Blog, Comment, Route, News, User

print("WORKING DIR:", os.getcwd())

app = Flask(__name__, template_folder="templates", static_folder="static")

# ---------------------------------------------------------
# DATABASE CONFIG (instance folder)
# ---------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "instance")
DB_PATH = os.path.join(INSTANCE_DIR, "database.db")

os.makedirs(INSTANCE_DIR, exist_ok=True)

print("DB PATH:", DB_PATH)

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

app.secret_key = "supersecretkey123"


# ---------------------------------------------------------
# SOS EMAIL FUNCTION
# ---------------------------------------------------------
import smtplib
from email.mime.text import MIMEText

import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "static/uploads/news"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# ---------------------------------------------------------
# AUTO NEWS CONTENT GENERATOR (SEO + ADSENSE OPTIMIZED)
#
# ---------------------------------------------------------
# AUTO SEO + ADSENSE OPTIMIZED NEWS GENERATOR
# ---------------------------------------------------------
def generate_seo_news(title, summary, category):
    keywords = [category, "trekking", "travel", "mountains", "adventure", "Nepal", "Himalaya"]
    keyword_str = ", ".join(keywords)

    return f"""
<h2>{title}</h2>

<p>{summary}</p>

<h3>Overview</h3>
<p>{summary} This article explores the latest developments in the {category.lower()} world, focusing on high‑search topics such as {keyword_str}. Readers searching for verified updates and expert insights will find this content valuable and AdSense‑friendly.</p>

<h3>Key Highlights</h3>
<ul>
    <li>Latest updates on {title}</li>
    <li>SEO keywords: {keyword_str}</li>
    <li>Expert opinions and verified sources</li>
    <li>Travel and safety recommendations</li>
</ul>

<h3>Detailed Analysis</h3>
<p>The {category.lower()} community has shown growing interest in this topic. This article provides a comprehensive breakdown, ensuring originality and compliance with Google AdSense content policies. It avoids duplicate or scraped text and focuses on informative, human‑style writing.</p>

<h3>Impact on Trekkers & Travelers</h3>
<p>For adventure enthusiasts, this update highlights how current trends may influence trekking routes, travel planning, and safety measures. Always verify local conditions before planning expeditions.</p>

<h3>Frequently Asked Questions</h3>
<p><strong>Is this content original?</strong> Yes — it is auto‑generated and rewritten for uniqueness.</p>
<p><strong>Is it AdSense‑safe?</strong> Absolutely. It avoids prohibited topics and ensures readability and keyword relevance.</p>

<h3>Conclusion</h3>
<p>This SEO‑optimized article helps readers discover reliable information while maintaining AdSense‑friendly formatting. Stay tuned for more updates on {category.lower()} and related topics.</p>
"""
def generate_image_url(text):
    # Keyword → Pexels image mapping
    image_map = {
        "mountain": "https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg",
        "trekking": "https://images.pexels.com/photos/196464/pexels-photo-196464.jpeg",
        "climbing": "https://images.pexels.com/photos/460937/pexels-photo-460937.jpeg",
        "hiking": "https://images.pexels.com/photos/2444403/pexels-photo-2444403.jpeg",
        "expedition": "https://images.pexels.com/photos/672358/pexels-photo-672358.jpeg",
        "everest": "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg",
        "himalaya": "https://images.pexels.com/photos/417173/pexels-photo-417173.jpeg",
        "adventure": "https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg",
        "outdoors": "https://images.pexels.com/photos/196464/pexels-photo-196464.jpeg"
    }

    text_lower = text.lower()

    # Match keyword to image
    for keyword, url in image_map.items():
        if keyword in text_lower:
            return f"{url}?auto=compress&cs=tinysrgb&w=1200&h=700"

    # Default fallback image
    return "https://images.pexels.com/photos/414171/pexels-photo-414171.jpeg?auto=compress&cs=tinysrgb&w=1200&h=700"

def expand_news_content(title, summary, category):
    return f"""
<h2>{title}</h2>

<p>{summary}</p>

<h3>Overview</h3>
<p>{summary} This development has gained significant attention in the {category.lower()} community, and readers are actively searching for reliable updates. This article provides a detailed breakdown, expert insights, and the latest verified information.</p>

<h3>Why This News Matters</h3>
<p>This topic has become one of the most searched subjects online due to its impact on trekkers, travelers, and adventure enthusiasts. Many people are looking for trustworthy explanations, safety updates, and future implications. This expanded coverage helps readers understand the full context behind the event.</p>

<h3>Detailed Breakdown</h3>
<p>The situation continues to evolve, and early reports indicate several important factors that readers should be aware of. Experts suggest monitoring official updates, verifying information from credible sources, and staying informed about any changes that may affect travel or trekking plans.</p>

<h3>Impact on Trekkers & Travelers</h3>
<p>For those planning expeditions, this news may influence route conditions, weather expectations, or safety guidelines. It is recommended to stay updated with local authorities, trekking agencies, and weather forecasts before making any decisions.</p>

<h3>SEO‑Optimized Key Insights</h3>
<ul>
    <li>Latest updates on {title}</li>
    <li>High‑search‑volume keywords related to {category}</li>
    <li>Safety tips and travel recommendations</li>
    <li>Expert opinions and verified information</li>
</ul>

<h3>Frequently Asked Questions</h3>
<p><strong>Is this information verified?</strong> Yes, this article is based on publicly available updates and expert analysis.</p>
<p><strong>Should trekkers change their plans?</strong> It depends on the region and current conditions. Always check official advisories.</p>

<h3>Final Thoughts</h3>
<p>This article will continue to be updated as more information becomes available. Stay connected for the latest developments, expert insights, and safety recommendations.</p>
"""

def send_sos_email(to_email, subject, body):
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SMTP_USER = "gyawalikrish0@gmail.com"  # <-- replace with your email
    SMTP_PASS = "ehgw nqry zvdq dqgf"    # <-- replace with your app password

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SMTP_USER
    msg["To"] = to_email

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(msg)


migrate = Migrate(app, db)

# LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            session['is_admin'] = user.is_admin

            return redirect('/admin' if user.is_admin else '/')

        return "Invalid username or password"

    return render_template('login.html')


# ADMIN DASHBOARD
@app.route('/admin')
def admin_dashboard():
    if not session.get('is_admin'):
        return "Access denied"

    total_posts = Blog.query.count()
    users = User.query.all()

    return render_template('admin_dashboard.html', total_posts=total_posts, users=users)
@app.route('/')
def home():
    from models import Route, Blog
    import requests

    # Popular routes
    popular_routes = Route.query.all()

    # Popular blogs (latest 3)
    popular_posts = Blog.query.order_by(Blog.date.desc()).limit(3).all()

    # Weather.gov API (works on Windows)
    cities = {
        "Warrensburg": (38.76, -93.74),
        "New York": (40.7128, -74.0060),
        "London": (51.5074, -0.1278),
        "Tokyo": (35.6895, 139.6917),
        "Delhi": (28.7041, 77.1025)
    }

    weather_data = []

    for city, (lat, lon) in cities.items():
        try:
            point_url = f"https://api.weather.gov/points/{lat},{lon}"
            point_data = requests.get(point_url, timeout=5).json()

            forecast_url = point_data["properties"]["forecast"]
            forecast_data = requests.get(forecast_url, timeout=5).json()
            current = forecast_data["properties"]["periods"][0]

            weather_data.append({
                "city": city,
                "temp": current["temperature"],
                "windspeed": current["windSpeed"],
                "summary": current["shortForecast"]
            })

        except Exception as e:
            print(f"Weather error for {city}:", e)
            weather_data.append({
                "city": city,
                "temp": "N/A",
                "windspeed": "N/A",
                "summary": "Unavailable"
            })

    return render_template(
        'index.html',   # ⭐ THIS IS THE FIX
        popular_routes=popular_routes,
        popular_posts=popular_posts,
        weather_data=weather_data
    )

# ROUTES PAGE
@app.route('/routes')
def routes_page():
    routes = Route.query.all()
    return render_template('routes.html', routes=routes)


# WEATHER PAGE
@app.route("/weather")
def weather():
    import requests

    countries = {
        "USA": (38.0, -97.0),
        "Canada": (56.1304, -106.3468),
        "UK": (55.3781, -3.4360),
        "France": (46.2276, 2.2137),
        "Italy": (41.8719, 12.5674),
        "Switzerland": (46.8182, 8.2275),
        "Germany": (51.1657, 10.4515),
        "Spain": (40.4637, -3.7492),
        "Portugal": (39.3999, -8.2245),
        "Greece": (39.0742, 21.8243),
        "Turkey": (38.9637, 35.2433),
        "UAE": (23.4241, 53.8478),
        "Saudi Arabia": (23.8859, 45.0792),
        "India": (20.5937, 78.9629),
        "Nepal": (28.3949, 84.1240),
        "Bhutan": (27.5142, 90.4336),
        "China": (35.8617, 104.1954),
        "Japan": (36.2048, 138.2529),
        "South Korea": (35.9078, 127.7669),
        "Thailand": (15.8700, 100.9925),
        "Indonesia": (0.7893, 113.9213),
        "Malaysia": (4.2105, 101.9758),
        "Vietnam": (14.0583, 108.2772),
        "Australia": (-25.2744, 133.7751),
        "New Zealand": (-40.9006, 174.8860),
        "South Africa": (-30.5595, 22.9375),
        "Egypt": (26.8206, 30.8025),
        "Morocco": (31.7917, -7.0926),
        "Brazil": (-14.2350, -51.9253),
        "Argentina": (-38.4161, -63.6167),
        "Chile": (-35.6751, -71.5430),
        "Peru": (-9.1900, -75.0152),
        "Mexico": (23.6345, -102.5528),
        "Iceland": (64.9631, -19.0208),
        "Norway": (60.4720, 8.4689),
        "Sweden": (60.1282, 18.6435),
        "Finland": (61.9241, 25.7482),
        "Russia": (61.5240, 105.3188)
    }

    weather_list = []

    for country, (lat, lon) in countries.items():
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            data = requests.get(url, timeout=5).json()
            current = data.get("current_weather", {})

            weather_list.append({
                "country": country,
                "temp": current.get("temperature", "N/A"),
                "windspeed": current.get("windspeed", "N/A"),
                "code": current.get("weathercode", "N/A")
            })
        except:
            weather_list.append({
                "country": country,
                "temp": "N/A",
                "windspeed": "N/A",
                "code": "N/A"
            })

    return render_template("weather.html", weather_list=weather_list)


# ADD POST
from werkzeug.utils import secure_filename
import os

@app.route('/add-post', methods=['GET', 'POST'])
def add_post():
    if not session.get('is_admin'):
        return "Access denied"

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        seo_title = request.form['seo_title']
        meta_description = request.form['meta_description']
        category = request.form['category']
        tags = request.form['tags']
        action = request.form['action']

        # Handle file upload
        file = request.files.get('featured_image')
        featured_image = "/static/uploads/default.jpg"

        if file and file.filename:
            filename = secure_filename(file.filename)

            # FULL ABSOLUTE PATH (Windows fix)
            upload_folder = os.path.join(app.root_path, "static", "uploads")
            os.makedirs(upload_folder, exist_ok=True)

            file_path = os.path.join(upload_folder, filename)
            file.save(file_path)

            # URL path for browser
            featured_image = f"/static/uploads/{filename}"

        new_post = Blog(
            title=title,
            content=content,
            featured_image=featured_image,
            seo_title=seo_title,
            meta_description=meta_description,
            category=category,
            tags=tags,
            is_draft=(action == "draft")
        )

        db.session.add(new_post)
        db.session.commit()

        return redirect('/blog')

    return render_template('add_post.html')


@app.route('/blog')
def blog():
    page = request.args.get('page', 1, type=int)
    q = request.args.get('q', '')
    category = request.args.get('cat', 'All')

    query = Blog.query.order_by(Blog.date.desc())

    if q:
        query = query.filter(
            or_(Blog.title.ilike(f'%{q}%'),
                Blog.content.ilike(f'%{q}%'))
        )

    if category != 'All':
        query = query.filter_by(category=category)

    posts = query.paginate(page=page, per_page=6)
    categories = ['All', 'Adventure', 'Tips', 'Weather', 'Safety', 'Routes']

    return render_template(
        'blog.html',
        posts=posts,
        q=q,
        category=category,
        categories=categories
    )

# VIEW POST
@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Blog.query.get_or_404(post_id)
    return render_template('view_post.html', post=post)


# DELETE POST
@app.route('/delete-post/<int:post_id>')
def delete_post(post_id):
    if not session.get('is_admin'):
        return "Access denied"

    post = Blog.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/admin')


# USER MANAGEMENT
@app.route('/admin/users')
def manage_users():
    if not session.get('is_admin'):
        return "Access denied"

    users = User.query.all()
    return render_template('manage_users.html', users=users)


@app.route('/admin/make-admin/<int:user_id>')
def make_admin(user_id):
    if not session.get('is_admin'):
        return "Access denied"

    user = User.query.get_or_404(user_id)
    user.is_admin = True
    db.session.commit()
    return redirect('/admin/users')


@app.route('/admin/remove-admin/<int:user_id>')
def remove_admin(user_id):
    if not session.get('is_admin'):
        return "Access denied"

    user = User.query.get_or_404(user_id)
    user.is_admin = False
    db.session.commit()
    return redirect('/admin/users')


@app.route('/admin/delete-user/<int:user_id>')
def delete_user(user_id):
    if not session.get('is_admin'):
        return "Access denied"

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect('/admin/users')


# LOGOUT
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/add-comment/<int:post_id>', methods=['POST'])
def add_comment(post_id):
    username = request.form['username']
    content = request.form['content']

    new_comment = Comment(post_id=post_id, username=username, content=content)
    db.session.add(new_comment)
    db.session.commit()

    return redirect(f'/post/{post_id}')


@app.route('/delete-comment/<int:comment_id>')
def delete_comment(comment_id):
    if not session.get('is_admin'):
        return "Access denied"

    comment = Comment.query.get_or_404(comment_id)
    post_id = comment.post_id

    db.session.delete(comment)
    db.session.commit()

    return redirect(f'/post/{post_id}')

@app.route('/add-route', methods=['GET', 'POST'])
def add_route():
    if request.method == 'POST':
        name = request.form['name']
        country = request.form['country']
        difficulty = request.form['difficulty']
        distance = request.form['distance']
        description = request.form['description']
        image_url = request.form['image_url']

        new_route = Route(
            name=name,
            country=country,
            difficulty=difficulty,
            distance_km=distance,
            description=description,
            image_url=image_url
        )

        db.session.add(new_route)
        db.session.commit()

    return render_template('add_route.html')

@app.route('/route/<int:route_id>')
def route_detail(route_id):
    from models import Route
    route = Route.query.get_or_404(route_id)
    return render_template('route_detail.html', route=route)

@app.route('/edit-post/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    if not session.get('is_admin'):
        return "Access denied"

    post = Blog.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.seo_title = request.form['seo_title']
        post.meta_description = request.form['meta_description']
        post.category = request.form['category']
        post.tags = request.form['tags']

        # Handle new image upload
        file = request.files.get('featured_image')
        if file and file.filename:
            filename = secure_filename(file.filename)
            upload_path = os.path.join(app.root_path, "static", "uploads", filename)
            file.save(upload_path)
            post.featured_image = f"/static/uploads/{filename}"

        db.session.commit()
        return redirect(f"/post/{post.id}")

    return render_template("edit_post.html", post=post)


@app.context_processor
def inject_year():
    return {"current_year": datetime.now().year}


@app.route("/sitemap.xml")
def sitemap():
    posts = Blog.query.all()
    return render_template("sitemap.xml", posts=posts), 200, {"Content-Type": "application/xml"}

@app.route("/trek-cost")
def trek_cost():
    return render_template("trek_cost.html")

@app.route("/packing-list")
def packing_list():
    return render_template("packing_list.html")

def generate_packing_list(region, season, difficulty, days):
    packing = {
        "Clothing": [
            "2–3 moisture-wicking T-shirts",
            "1–2 trekking pants",
            "Thermal base layer",
            "Fleece jacket",
            "Rain jacket / poncho",
            "Warm cap + sun cap",
            "Light gloves"
        ],
        "Footwear": [
            "Trekking shoes with good grip",
            "Camp sandals",
            "3–4 pairs of trekking socks"
        ],
        "Gear": [
            "Backpack (40–60L)",
            "Rain cover",
            "Trekking poles",
            "Headlamp + batteries",
            "Water bottle / hydration bladder"
        ],
        "Safety": [
            "First-aid kit",
            "Personal medicines",
            "Sunscreen SPF 50",
            "Lip balm",
            "Electrolyte packets"
        ],
        "Electronics": [
            "Power bank",
            "Phone + charger",
            "Camera (optional)"
        ],
        "Toiletries": [
            "Toothbrush + paste",
            "Soap / biodegradable wash",
            "Quick-dry towel",
            "Wet wipes",
            "Hand sanitizer"
        ],
        "Documents": [
            "ID proof",
            "Permits (if required)",
            "Cash (remote areas have no ATMs)"
        ]
    }

    # Region-specific
    if region in ["Uttarakhand", "Himachal", "Kashmir", "Everest Region", "Annapurna Region"]:
        packing["Clothing"].append("Extra thermal layer")
        packing["Gear"].append("Microspikes (winter)")
        packing["Safety"].append("Altitude sickness tablets (Diamox)")

    if region in ["Maharashtra", "Karnataka", "Local Hills"]:
        packing["Clothing"].append("Light cotton clothing")
        packing["Safety"].append("Leech socks (monsoon)")

    # Season-specific
    if season == "Winter":
        packing["Clothing"] += ["Heavy down jacket", "Balaclava", "Wool gloves"]
        packing["Gear"].append("Hot water bag")

    if season == "Monsoon":
        packing["Gear"].append("Waterproof backpack liner")
        packing["Footwear"].append("Quick-dry socks")

    if season == "Summer":
        packing["Safety"].append("Hydration salts")
        packing["Clothing"].append("UV-protection sleeves")

    # Difficulty-specific
    if difficulty == "Challenging":
        packing["Gear"].append("High-ankle trekking boots")
        packing["Safety"].append("Knee support")
        packing["Gear"].append("Emergency blanket")

    return packing
@app.route("/ai-trek-planner", methods=["GET", "POST"])
def ai_trek_planner():
    plan = None

    if request.method == "POST":
        region = request.form.get("region")
        days = int(request.form.get("days") or 3)
        budget = int(request.form.get("budget") or 10000)
        experience = request.form.get("experience")
        season = request.form.get("season")

        difficulty = "Easy"
        if days >= 5 or experience == "intermediate":
            difficulty = "Moderate"
        if days >= 7 or experience == "advanced":
            difficulty = "Challenging"

        base_cost_per_day = 2000
        if region in ["Himalayas", "Alps"]:
            base_cost_per_day = 3000
        if season in ["Winter", "Monsoon"]:
            base_cost_per_day += 500

        estimated_cost = base_cost_per_day * days

        itinerary = []
        for d in range(1, days + 1):
            if d == 1:
                title = "Arrival & Acclimatization"
                desc = f"Reach the {region} base area, check gear, warm-up hike."
            elif d == days:
                title = "Return & Buffer Day"
                desc = "Descend safely, travel back to base town."
            else:
                title = f"Trek Day {d}"
                desc = f"Scenic trekking day in the {region}."
            itinerary.append({"day": d, "title": title, "desc": desc})

        packing_list = generate_packing_list(region, season, difficulty, days)

        safety_tips = [
            "Never trek alone.",
            "Inform someone about your itinerary.",
            "Stay hydrated.",
            "Check weather daily.",
            "Turn back if conditions feel unsafe."
        ]

        plan = {
            "region": region,
            "days": days,
            "budget": budget,
            "experience": experience,
            "season": season,
            "difficulty": difficulty,
            "estimated_cost": estimated_cost,
            "itinerary": itinerary,
            "packing_list": packing_list,
            "safety_tips": safety_tips,
        }

    return render_template("ai_trek_planner.html", plan=plan)
@app.route("/emergency-alerts")
def emergency_alerts():
    import requests
    import feedparser

    alerts = {
        "gdacs": [],
        "reliefweb": [],
        "nasa_fires": [],
        "local_weather": []
    }

    # -------------------------------
    # 1. GDACS GLOBAL DISASTER ALERTS
    # -------------------------------
    try:
        headers = {"User-Agent": "Mozilla/5.0 (TrekChat Alerts)"}
        xml = requests.get("https://www.gdacs.org/xml/rss.xml", headers=headers, timeout=10).text
        feed = feedparser.parse(xml)

        for entry in feed.entries[:20]:
            alerts["gdacs"].append({
                "title": entry.get("title"),
                "summary": entry.get("summary"),
                "link": entry.get("link"),
                "date": entry.get("published", "Unknown")
            })
    except Exception as e:
        print("GDACS ERROR:", e)

    # -------------------------------------
    # 2. RELIEFWEB HUMANITARIAN EMERGENCIES
    # -------------------------------------
    try:
        rw_url = "https://api.reliefweb.int/v1/disasters?appname=TrekChat&profile=full&limit=20"
        rw_data = requests.get(rw_url, timeout=10).json()

        for item in rw_data.get("data", []):
            fields = item.get("fields", {})
            alerts["reliefweb"].append({
                "name": fields.get("name"),
                "status": fields.get("status"),
                "type": fields.get("type", [{}])[0].get("name", "Unknown"),
                "country": fields.get("country", [{}])[0].get("name", "Unknown"),
                "date": fields.get("date", {}).get("created", "Unknown"),
                "url": fields.get("url")
            })
    except Exception as e:
        print("RELIEFWEB ERROR:", e)

    # -------------------------------
    # 3. NASA FIRMS WILDFIRE ALERTS
    # -------------------------------
    try:
        nasa_url = "https://firms.modaps.eosdis.nasa.gov/api/area/csv/USA/24h"
        # NASA FIRMS requires an API key normally, so we use a public sample feed:
        nasa_sample = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_USA_24h.csv"
        csv_data = requests.get(nasa_sample, timeout=10).text.splitlines()

        for row in csv_data[1:50]:  # skip header
            cols = row.split(",")
            if len(cols) > 5:
                alerts["nasa_fires"].append({
                    "latitude": cols[0],
                    "longitude": cols[1],
                    "brightness": cols[2],
                    "acq_date": cols[5]
                })
    except Exception as e:
        print("NASA FIRMS ERROR:", e)

    # -----------------------------------
    # 4. LOCAL WEATHER DANGER (Open-Meteo)
    # -----------------------------------
    regions = {
        "Himalayas": (30.0668, 79.0193),
        "Kashmir": (34.0837, 74.7973),
        "Nepal": (28.3949, 84.1240),
        "Maharashtra": (19.7515, 75.7139)
    }

    for region, (lat, lon) in regions.items():
        try:
            url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
            data = requests.get(url, timeout=10).json()

            w = data.get("current_weather", {})
            temp = w.get("temperature")
            wind = w.get("windspeed")
            code = w.get("weathercode")

            warnings = []

            if temp is not None:
                if temp < -5:
                    warnings.append("Extreme cold warning")
                if temp > 35:
                    warnings.append("Heatwave alert")

            if wind and wind > 40:
                warnings.append("High wind danger")

            if code in [65, 66, 67]:
                warnings.append("Heavy rain warning")
            if code in [71, 73, 75]:
                warnings.append("Snowfall alert")

            alerts["local_weather"].append({
                "region": region,
                "temperature": temp,
                "wind": wind,
                "warnings": warnings
            })

        except Exception as e:
            print("WEATHER ERROR:", e)

    return render_template("emergency_alerts.html", alerts=alerts)

@app.route("/sos", methods=["GET", "POST"])
def sos():
    if request.method == "POST":
        user_name = request.form.get("user_name")
        emergency_email = request.form.get("emergency_email")
        emergency_phone = request.form.get("emergency_phone")
        location = request.form.get("location")
        message = request.form.get("message") or "SOS triggered from TrekChat."

        body = f"""
🚨 EMERGENCY SOS ALERT

User: {user_name}
Location: {location}
Emergency Phone: {emergency_phone}

Message:
{message}
"""

        send_sos_email(
            to_email=emergency_email,
            subject="🚨 TrekChat SOS Alert",
            body=body
        )

        return render_template("sos_sent.html", user_name=user_name)

    return render_template("sos.html")


from flask import redirect, url_for, flash

@app.route("/admin/news")
def admin_news_list():
    if not session.get("is_admin"):
        return "Access denied"

    all_news = News.query.order_by(News.created_at.desc()).all()
    return render_template("admin_news_list.html", news=all_news)


@app.route("/admin/news/<int:news_id>/delete")
def admin_news_delete(news_id):
    if not session.get("is_admin"):
        return "Access denied"

    item = News.query.get_or_404(news_id)
    db.session.delete(item)
    db.session.commit()

    return redirect("/admin/news")

@app.route("/admin/news/<int:news_id>/edit", methods=["GET", "POST"])
def admin_news_edit(news_id):
    if not session.get("is_admin"):
        return "Access denied"

    item = News.query.get_or_404(news_id)
    categories = ["Trekking", "Climbing", "Travel", "Expedition", "General"]

    if request.method == "POST":
        item.title = request.form["title"]
        item.summary = request.form["summary"]
        item.category = request.form["category"]
        item.image_url = request.form["image_url"]
        item.meta_title = request.form["meta_title"]
        item.meta_description = request.form["meta_description"]
        item.content = request.form["content"]   # ⭐ THIS WAS MISSING

        db.session.commit()
        return redirect("/admin/news")

    return render_template("admin_news_edit.html", item=item, categories=categories)

@app.route("/news")
def news_page():
    page = request.args.get("page", 1, type=int)
    category = request.args.get("category")

    query = News.query

    if category:
        query = query.filter_by(category=category)

    pagination = query.order_by(News.created_at.desc()).paginate(page=page, per_page=10)
    news_items = pagination.items

    categories = ["Trekking", "Climbing", "Travel", "Expedition", "General"]

    return render_template(
        "news.html",
        news=news_items,
        categories=categories,
        selected=category,
        pagination=pagination
    )
@app.route("/news/<slug>")
def news_detail_page(slug):
    item = News.query.filter_by(slug=slug).first_or_404()
    return render_template("news_detail.html", item=item)

@app.route('/admin/news/add', methods=['GET', 'POST'])
def admin_news_add():
    if not session.get("is_admin"):
        return "Access denied"

    categories = db.session.query(News.category).distinct().all()
    categories = [c[0] for c in categories]

    if request.method == 'POST':
        title = request.form['title']
        summary = request.form['summary']
        category = request.form['category']
        meta_title = request.form['meta_title']
        meta_description = request.form['meta_description']

        # Auto-generate SEO content + image
        content = generate_seo_news(title, summary, category)
        image_url = generate_image_url(title, category)

        slug = title.lower().replace(" ", "-")

        news = News(
            title=title,
            summary=summary,
            category=category,
            image_url=image_url,
            meta_title=meta_title,
            meta_description=meta_description,
            content=content,
            slug=slug
        )

        db.session.add(news)
        db.session.commit()
        return redirect('/admin/news')


    return render_template('admin_news_add.html', categories=categories)

@app.route("/nepal-treks")
def nepal_treks():
    treks = [
        {
            "name": "Everest Base Camp Trek",
            "duration": "14 Days",
            "difficulty": "Challenging",
            "price": "$1299",
            "image": "/static/images/nepal/ebc.jpg",
            "link": "https://wa.me/1234567890"
        },
        {
            "name": "Annapurna Base Camp Trek",
            "duration": "10 Days",
            "difficulty": "Moderate",
            "price": "$899",
            "image": "/static/images/nepal/abc.jpg",
            "link": "https://wa.me/1234567890"
        },
        {
            "name": "Mardi Himal Trek",
            "duration": "6 Days",
            "difficulty": "Easy–Moderate",
            "price": "$499",
            "image": "/static/images/nepal/mardi.jpg",
            "link": "https://wa.me/1234567890"
        },
        {
            "name": "Langtang Valley Trek",
            "duration": "7 Days",
            "difficulty": "Moderate",
            "price": "$599",
            "image": "/static/images/nepal/langtang.jpg",
            "link": "https://wa.me/1234567890"
        },
        {
            "name": "Manaslu Circuit Trek",
            "duration": "14 Days",
            "difficulty": "Challenging",
            "price": "$1199",
            "image": "/static/images/nepal/manaslu.jpg",
            "link": "https://wa.me/1234567890"
        }
    ]

    return render_template("nepal_treks.html", treks=treks)
@app.route("/nepal-treks/<slug>")
def nepal_trek_detail(slug):
    treks = {
        "everest-base-camp": {
            "name": "Everest Base Camp Trek",
            "duration": "14 Days",
            "difficulty": "Challenging",
            "price": "$1299",
            "image": "/static/images/nepal/ebc.jpg",
            "highlights": [
                "Scenic flight to Lukla",
                "Namche Bazaar acclimatization",
                "Tengboche Monastery",
                "Khumbu Glacier",
                "Kala Patthar sunrise viewpoint"
            ],
            "overview": "The Everest Base Camp Trek is Nepal’s most iconic adventure, taking you through Sherpa villages, high-altitude landscapes, and breathtaking Himalayan views."
        },

        "annapurna-base-camp": {
            "name": "Annapurna Base Camp Trek",
            "duration": "10 Days",
            "difficulty": "Moderate",
            "price": "$899",
            "image": "/static/images/nepal/abc.jpg",
            "highlights": [
                "Ghandruk village",
                "Machhapuchhre Base Camp",
                "Annapurna Sanctuary",
                "Hot springs at Jhinu"
            ],
            "overview": "A beautiful trek into the heart of the Annapurna Sanctuary, surrounded by 360° Himalayan peaks."
        },

        "mardi-himal": {
            "name": "Mardi Himal Trek",
            "duration": "6 Days",
            "difficulty": "Easy–Moderate",
            "price": "$499",
            "image": "/static/images/nepal/mardi.jpg",
            "highlights": [
                "Forest trails",
                "Mardi High Camp",
                "Close-up views of Machhapuchhre"
            ],
            "overview": "A short and scenic trek offering stunning views of Machhapuchhre and the Annapurna range."
        }
    }

    trek = treks.get(slug)

    if not trek:
        return "Trek not found", 404

    return render_template("nepal_trek_detail.html", trek=trek)

@app.route("/admin/news")
def admin_news():
    if not session.get("is_admin"):
        return "Access denied"

    news = News.query.order_by(News.created_at.desc()).all()
    return render_template("admin_news.html", news=news)

@app.route("/admin/news/add", methods=["GET", "POST"])
def admin_add_news():
    if not session.get("is_admin"):
        return "Access denied"

    if request.method == "POST":
        title = request.form["title"]
        summary = request.form["summary"]
        content = request.form["content"]
        category = request.form["category"]
        source_url = request.form["source_url"]
        meta_title = request.form["meta_title"]
        meta_description = request.form["meta_description"]
        tags = request.form["tags"]

        # Image upload
        file = request.files.get("image")
        image_url = None

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            image_url = f"/static/uploads/news/{filename}"

        slug = title.lower().replace(" ", "-")

        news = News(
            title=title,
            summary=summary,
            content=content,
            category=category,
            source_url=source_url,
            meta_title=meta_title,
            meta_description=meta_description,
            tags=tags,
            image_url=image_url,
            slug=slug
        )

        db.session.add(news)
        db.session.commit()

        return redirect("/admin/news")

    return render_template("admin_news_add.html")
@app.route("/admin/news/edit/<int:id>", methods=["GET", "POST"])
def admin_edit_news(id):
    if not session.get("is_admin"):
        return "Access denied"

    news = News.query.get_or_404(id)

    if request.method == "POST":
        news.title = request.form["title"]
        news.summary = request.form["summary"]
        news.content = request.form["content"]
        news.category = request.form["category"]
        news.source_url = request.form["source_url"]
        news.meta_title = request.form["meta_title"]
        news.meta_description = request.form["meta_description"]
        news.tags = request.form["tags"]

        # Replace image if new one uploaded
        file = request.files.get("image")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            news.image_url = f"/static/uploads/news/{filename}"

        db.session.commit()
        return redirect("/admin/news")

    return render_template("admin_news_edit.html", news=news)
@app.route("/admin/news/delete/<int:id>")
def admin_delete_news(id):
    if not session.get("is_admin"):
        return "Access denied"

    news = News.query.get_or_404(id)
    db.session.delete(news)
    db.session.commit()

    return redirect("/admin/news")

if __name__ == '__main__':
    app.run(debug=True)


