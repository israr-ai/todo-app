# create_db.py
from main import app, db  # import from main.py (not app.py)

with app.app_context():
    db.create_all()
    print("✅ Database created at external_data/mydata.db")
