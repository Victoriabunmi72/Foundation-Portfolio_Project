import os, sys
sys.path.append(os.getcwd())
from main import db, app

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
