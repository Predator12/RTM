import sys

from loguru import logger as initial_logger
from flask import Flask
from flask_login import LoginManager
from flask_pymongo import PyMongo
from app.mongo_folder import UserMongoModel

from app.consts import USER_NAME, USER_PASSWORD


def init_logger(logger):
    log_format = \
        "{time} - level={level} - " \
        "[{file}:{line} - {function}() thread_id - {thread}]:\n{message}"

    log_file_path = "logs/rtm.log"
    logger.add(
        sys.stderr,
        format=log_format,
        level="DEBUG",
        backtrace=True,
        diagnose=True
    )

    logger.add(
        log_file_path,
        format=log_format,
        rotation="50 MB",
        compression="zip",
        level="DEBUG",
        backtrace=True,
        diagnose=True
    )
    logger.bind(request_id="N/A")

    return logger


logger = init_logger(initial_logger)


def create_app():
    app = Flask(__name__, static_url_path='/static')

    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['MONGO_URI'] = "mongodb://{}:{}@ds229380.mlab.com:29380/rtm?retryWrites=false".format(
        USER_NAME,
        USER_PASSWORD
    )
    app.config['retryWrites'] = False
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from app.mongo_folder import UserMongoModel

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return UserMongoModel.objects.get({"name": user_id})

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for main parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # blueprint for patients parts of app
    from .patients import patients as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


def mongo_con():
    mongo = PyMongo(create_app())
    return mongo
