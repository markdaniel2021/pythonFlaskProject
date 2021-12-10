from marshmallow import fields, validates, ValidationError
from flask_marshmallow import Marshmallow
from .model import User

ma = Marshmallow()


def configure(app):
    ma.init_app(app)


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User

    username = fields.Str(required=True)
    password = fields.Str(required=True)
    age = fields.Str(required=True)
    fullname = fields.Str(required=True)