print("run.py started")

from app import create
print("app created")
from app import db
from app.models import Blog

print("Imports successful")

app = create()

print("App created")

with app.app_context():
    db.create_all()

print("Database created")

if __name__ == "__main__":
    print("Starting Flask...")
    app.run(debug=True)