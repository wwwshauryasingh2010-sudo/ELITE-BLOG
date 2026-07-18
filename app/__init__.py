from flask_sqlalchemy import SQLAlchemy
from flask import Flask 

db=SQLAlchemy()


def create():
    app=Flask(__name__)
    app.config["SECRET_KEY"]="my_secret"
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///site.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

    db.init_app(app)


    from app.models import Blog


    from app.routes.auth import auth_bp
    from app.routes.blog import blog_bp
    

    app.register_blueprint(auth_bp)
    app.register_blueprint(blog_bp)

    return app


