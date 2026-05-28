import sqlite3

conn = sqlite3.connect("instance/database.db")
cursor = conn.cursor()

columns = [
    ("content", "TEXT"),
    ("image_url", "VARCHAR(500)"),
    ("meta_title", "VARCHAR(255)"),
    ("meta_description", "VARCHAR(255)"),
    ("slug", "VARCHAR(255)")
]

for col, col_type in columns:
    try:
        cursor.execute(f"ALTER TABLE news ADD COLUMN {col} {col_type};")
        print(f"Added column: {col}")
    except Exception as e:
        print(f"Skipping {col}: {e}")

conn.commit()
conn.close()

print("Done!")
