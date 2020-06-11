# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Email, Str, Int

from apps.messages import MSG_FIELD_REQUIRED


class CollaboratorRegistrationSchema(Schema):
    name = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    email = Email(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    password = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    rf = Int(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )


class CollaboratorSchema(Schema):
    id = Str()
    name = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    email = Email(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    cpf = Str()
    rf = Str()