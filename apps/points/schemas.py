# -*- coding: utf-8 -*-

from marshmallow import Schema
from marshmallow.fields import Str, Int, Email

from apps.messages import MSG_FIELD_REQUIRED


class PointRegistrationSchema(Schema):
    date = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    time = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    rf = Int(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )


class PointSchema(Schema):
    id = Str()
    date = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    time = Str(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )
    rf = Int(
        required=True,
        error_messages={'required': MSG_FIELD_REQUIRED}
    )