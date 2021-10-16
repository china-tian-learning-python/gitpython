from flask_sqlalchemy import SQLAlchemy

# app=create_app()
db = SQLAlchemy()

def peize(app):
    db.init_app(app)