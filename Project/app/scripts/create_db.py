import os, sys
sys.path.append(os.getcwd())
from app.app import db

if __name__ == "__main__":
    db.create_all()
