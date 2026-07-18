from flask_sqlalchemy import SQLAlchemy
from flask import Flask 
import os

db=SQLAlchemy()


def create():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="my_secret"
    
    database_url = os.getenv("DATABASE_URL")

    if database_url:
        database_url = database_url.replace("postgres://", "postgresql://", 1)
        app.config["SQLALCHEMY_DATABASE_URI"] = database_url
    else:
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

    app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
        "pool_pre_ping": True,
    }
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)


    from app.models import Blog


    from app.routes.auth import auth_bp
    from app.routes.blog import blog_bp
    

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)

    return app


