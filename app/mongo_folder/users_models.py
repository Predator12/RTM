from pymodm import MongoModel, fields
from pymongo import ASCENDING
from pymongo.operations import IndexModel

from app.consts import PYMODB_ALIAS


class UserMongoModel(MongoModel):
    name = fields.CharField()
    lastname = fields.CharField()
    surname = fields.CharField()
    email = fields.CharField()
    password = fields.CharField()
    img = fields.CharField()

    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.name


    class Meta:
        collection_name = "users"
        connection_alias = PYMODB_ALIAS
