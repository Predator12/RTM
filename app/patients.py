from flask import Blueprint, render_template, session, request, redirect
from flask_login import login_required
from pymodm.files import File

from app.mongo_folder.patiets_mongo import PatientsMongoModel

from app import logger, mongo_con

patients = Blueprint('patients', __name__)


@patients.route('/patients_list')
@login_required
def patients_list():
    patients = PatientsMongoModel.objects
    return render_template('patients.html', patients=patients)


@patients.route('/new_patient')
@login_required
def create_patient():
    return render_template('new_patient.html')


@patients.route('/new_patient',  methods=['POST'])
@login_required
def create_patient_post():
    patient = PatientsMongoModel()

    patient.name = request.form.get('name')
    patient.lastname = request.form.get('lastname')
    patient.surname = request.form.get('surname')
    patient.room = int(request.form.get('room'))
    patient.save()
    return redirect('/patients_list')

