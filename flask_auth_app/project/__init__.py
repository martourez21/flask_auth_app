from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    migrate.init_app(app, db)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgresql://postgres:postgres@localhost:5432/employees'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=True

    db.init_app(app)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app