# app/schemas/responses.py
from marshmallow import Schema, fields

class PaginationSchema(Schema):
    page = fields.Integer()
    per_page = fields.Integer()
    total = fields.Integer()
    pages = fields.Integer()

class ErrorSchema(Schema):
    code = fields.Integer()
    message = fields.String()
    details = fields.Dict(keys=fields.String(), values=fields.String())

class SuccessResponse(Schema):
    status = fields.String(default="success")
    data = fields.Dict(keys=fields.String())
    message = fields.String()

class ErrorResponse(Schema):
    status = fields.String(default="error")
    error = fields.Nested(ErrorSchema)

class PaginatedResponse(Schema):
    items = fields.List(fields.Nested('BaseSchema'))
    pagination = fields.Nested(PaginationSchema)