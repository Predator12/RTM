from flask import Blueprint, render_template, session, request, redirect
from flask_login import login_required
from pymodm.files import File

from app.mongo_folder.users_models import UserMongoModel

from app import logger, mongo_con

main = Blueprint('main', __name__)
mongo = mongo_con()

@main.route('/')
@login_required
def index():
    return render_template('index.html')


@main.route('/profile')
@login_required
def profile():
    user = UserMongoModel.objects.get({"name": session['_user_id']})
    return render_template('profile.html', name=user.name, lastname=user.lastname,
                           email=user.email, img="upload_image/{}".format(user.img))


@main.route('/upload_image', methods=['POST'])
@login_required
def upload_image_to_mongo():
    if "image" in request.files:
        img = request.files.get("image")
        logger.info("img {}".format(img))
        user_name = session['_user_id']
        user = UserMongoModel.objects.get({"name": user_name})
        user.img = img.filename
        user.save()
        mongo.save_file(img.filename, img)

    return redirect("/profile")


@main.route('/upload_image/<name>')
@login_required
def mage_to_mongo(name):
    return mongo.send_file(name)


@main.route('/create_user')
@login_required
def create_user():
    logger.info("Start create user")

    user = UserMongoModel()
    user.name = "Pavlo"
    user.password = "12345678"
    user.lastname = "Panchyshak"
    user.surname = "Mikhailovich"
    user.email = "panchyshak@gmail.com"
    user.save()

    return "User Created Success"
