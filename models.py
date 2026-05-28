from extensions import db
from datetime import datetime

# ---------------------------------------------------------
# TREK ROUTES
# ---------------------------------------------------------
class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    country = db.Column(db.String(100))
    difficulty = db.Column(db.String(50))
    distance_km = db.Column(db.Float)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(500))

    # SEO + Trekking Details
    overview = db.Column(db.Text)
    best_season = db.Column(db.String(200))
    elevation_gain = db.Column(db.String(100))
    duration_days = db.Column(db.Integer)
    starting_point = db.Column(db.String(200))
    ending_point = db.Column(db.String(200))

    # Maps + Itinerary
    map_embed = db.Column(db.Text)
    itinerary = db.Column(db.JSON)

    # SEO Sections
    how_to_reach = db.Column(db.Text)
    permits = db.Column(db.Text)
    packing_list = db.Column(db.Text)
    safety_tips = db.Column(db.Text)
    accommodation = db.Column(db.Text)
    weather = db.Column(db.Text)
    faqs = db.Column(db.JSON)

    seo_content = db.Column(db.Text)


# ---------------------------------------------------------
# BLOG POSTS
# ---------------------------------------------------------
class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Main content
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    # Featured image
    featured_image = db.Column(db.String(300), default="default.jpg")

    # Category
    category = db.Column(db.String(50), default="General")

    # Tags
    tags = db.Column(db.String(300))

    # SEO
    seo_title = db.Column(db.String(200))
    meta_description = db.Column(db.String(300))

    # Date
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Draft or Published
    is_draft = db.Column(db.Boolean, default=False)

    # Author
    author = db.Column(db.String(100), default="Admin")

    # Slug
    slug = db.Column(db.String(300), unique=True)


# ---------------------------------------------------------
# EMERGENCY ALERTS
# ---------------------------------------------------------
class Emergency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(300))
    location = db.Column(db.String(200))


# ---------------------------------------------------------
# COMMENTS
# ---------------------------------------------------------
class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('blog.id'), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relationship
    post = db.relationship('Blog', backref=db.backref('comments', lazy=True))


# ---------------------------------------------------------
# USERS
# ---------------------------------------------------------
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(120))
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    # Optional PRO fields
    emergency_name = db.Column(db.String(150))
    emergency_phone = db.Column(db.String(50))
    emergency_email = db.Column(db.String(150))
    is_pro = db.Column(db.Boolean, default=False)


# ---------------------------------------------------------
# NEWS ARTICLES
# ---------------------------------------------------------
class News(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    summary = db.Column(db.Text)

    # ⭐ Long content field (this is what you needed)
    content = db.Column(db.Text)

    category = db.Column(db.String(100))
    image_url = db.Column(db.String(500))
    meta_title = db.Column(db.String(255))
    meta_description = db.Column(db.String(255))
    source_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    slug = db.Column(db.String(255))
    tags = db.Column(db.String(255))
