from marshmallow import Schema, fields


class IncomeSchemaForm(Schema):
    description = fields.String(
        required=True,
        error_messages={
            "required": {"message": "Description is required", "code": 400}
        }
    )
    amount = fields.Float(
        required=True,
        error_messages={
            "required": {"message": "Amount is required", "code": 400}
        }
    )
    currency = fields.String()


class IncomeSchemaResponse(Schema):
    id = fields.Integer()
    description = fields.String()
    amount = fields.Float()
    currency = fields.String()
    datetime = fields.DateTime()
