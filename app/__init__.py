from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)  # or Config if you're not using separate config classes
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
