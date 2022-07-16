from config import Config
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message = ('Login to access your Pokemon.')
bootstrap = Bootstrap5


def create_app():
    app = Flask(__name__)

    # connect Config class to our app instance
    app.config.from_object(Config)

    # initialize instances
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    bootstrap.init_app(app)

    # initialize app with login manager
    login_manager.init_app(app)

    # register blueprints with our app instance

    from app.blueprints.auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    from app.blueprints.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app
