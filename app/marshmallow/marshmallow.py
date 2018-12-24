from app.database.models import Tasks
from app import ma
from marshmallow import Schema, fields, ValidationError


class TasksSchema(ma.ModelSchema):
    class Meta:
        model = Tasks


def not_blank(data):
    if not data.strip():
        raise ValidationError('Data is empty')


class TaskSchema(Schema):
    unique_id = fields.Integer()
    title = fields.String(required=True, validate=not_blank)
    description = fields.String()
    done = fields.Boolean()

    class Meta:
        strict = True
