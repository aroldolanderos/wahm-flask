from flask import Blueprint, request
from components.income.models import Incomes
from components.income.schemas import (
    IncomeSchemaForm,
    IncomeSchemaResponse
)
from components.income.store import IncomeStore

api_incomes = Blueprint('incomes', __name__, url_prefix='/incomes')


# + GET /incomes/
@api_incomes.route('/', methods=['GET'])
def get_list():
    incomes = Incomes.query.all()
    result = IncomeSchemaResponse(many=True).dump(incomes)
    return {'incomes': result}


# + POST /incomes/
@api_incomes.route('/', methods=['POST'])
def create():
    form_data = IncomeSchemaForm().load(request.json)
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
