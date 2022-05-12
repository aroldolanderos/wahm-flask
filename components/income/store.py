from components.income.models import Income
from database import db


class IncomeStore:
    @staticmethod
    def create(data):
        new_income = Income(**data)
        db.session.add(new_income)
        db.session.commit()
        return new_income

    @staticmethod
    def update(id, data):
        pass

    @staticmethod
    def find_all():
        return Income.query.all()

    @staticmethod
    def find_by_id(id):
        pass
