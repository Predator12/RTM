import pymodm

from app import create_app
from app.consts import PYMODB_ALIAS, USER_NAME, USER_PASSWORD

if __name__ == "__main__":
    mongodb_connect_uri = "mongodb://{}:{}@ds229380.mlab.com:29380/rtm".format(USER_NAME, USER_PASSWORD)
    pymodm.connect(mongodb_connect_uri, alias=PYMODB_ALIAS, retryWrites=False)
    app = create_app()
    app.debug = True
    app.run(host='0.0.0.0', port=8000)
