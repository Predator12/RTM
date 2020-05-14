from pymodm import MongoModel, fields
from pymongo import ASCENDING
from pymongo.operations import IndexModel

from app.consts import PYMODB_ALIAS


class PatientsMongoModel(MongoModel):
    name = fields.CharField()
    lastname = fields.CharField()
    surname = fields.CharField()
    room = fields.IntegerField()

    class Meta:
        collection_name = "patiets"
        connection_alias = PYMODB_ALIAS
