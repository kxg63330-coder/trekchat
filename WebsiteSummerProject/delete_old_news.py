from app import app
from extensions import db
from models import News

with app.app_context():
    deleted = News.query.delete()
    db.session.commit()
    print(f"Deleted {deleted} old articles successfully.")
