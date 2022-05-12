from flask import Blueprint, request
from components.income.response import IncomeResponse
from components.income.schemas import (
    IncomeValidationSchema,
    IncomeResponseSchema
)
from components.income.store import IncomeStore
from marshmallow import ValidationError

api_incomes = Blueprint('incomes', __name__, url_prefix='/incomes')


# + GET /incomes/
@api_incomes.route('/', methods=['GET'])
def get_list():
    incomes = IncomeStore.find_all()
    result = IncomeResponseSchema(many=True).dump(incomes)
    return IncomeResponse.success(result, 200)


# + POST /incomes/
@api_incomes.route('/', methods=['POST'])
def create():
    try:
        form_data = IncomeValidationSchema().load(request.json)
    except ValidationError as error:
        return IncomeResponse.error(error.messages, 400)

    new_income = IncomeStore.create(form_data)
    return {'income': f"{new_income}"}, 201


# + GET /incomes/<id>
@api_incomes.route('/<id>', methods=['GET'])
def get_by_id(id):
    return {'income': 'Income demo - get by id: %s' % id}


# + PUT /incomes/<id>
@api_incomes.route('/<id>', methods=['PUT'])
def update_by_id(id):
    return {'income': 'Income demo - update by id: %s' % id}
