from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from app import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config.DevelopmentConfig)
# app.config["SQLALCHEMY_DATABASE_URI"] = config.BaseConfig.SQLALCHEMY_DATABASE_URI
db = SQLAlchemy(app)
# db.init_app(app)
from app.web import models

migrate = Migrate()
migrate.init_app(app, db)
def create_app():
    from app.web import wb
    app.register_blueprint(wb, url_prefix="/user")
    return app