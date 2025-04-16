from flask import Flask 
from flask_pymongo import PyMongo 
from flask_cors import CORS 
from config import Config

# mongo = PyMongo()

def create():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    CORS(app)
    from .extensions import mongo
    mongo.init_app(app)
    
    print("mongo instance:", mongo)
    print("mongo.db:", mongo.db)
 
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
