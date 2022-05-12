import pytest
from components.income.schemas import (
    IncomeValidationSchema,
    IncomeResponseSchema
)
from marshmallow import ValidationError


def test_list_income_validate_schema():
    """
    Given Income dict
    When serialize using IncomeValidationSchema
    Then verifies that the serialization corresponds
    """
    income = dict(description='january salary', amount=1500.0,
                  currency='CLP')
    result = IncomeValidationSchema().load(income)
    assert len(result) == 3  # only 3 fields
    assert result['description'] == 'january salary'
    assert result['amount'] == 1500.0
    assert result['currency'] == 'CLP'


def test_validation_error_without_amount_in_income_response_schema():
    """
    Given Income dict
    When the amount is not entered
    Then raise a ValidationError
    """
    income = dict(description='january salary', currency='CLP')
    with pytest.raises(ValidationError):
        IncomeValidationSchema().load(income)


def test_validation_error_without_description_in_income_response_schema():
    """
    Given Income dict
    When the description is not entered
    Then raise a ValidationError
    """
    income = dict(amount=1500.0, currency='CLP')
    with pytest.raises(ValidationError):
        IncomeValidationSchema().load(income)


def test_list_income_response_schema():
    """
    Given Income dict
    When serialize using IncomeResponseSchema for multiple incomes
    Then verifies that the serialization corresponds
    """
    incomes = [
        dict(id=1, description='january salary', amount=1500.0,
             currency='CLP'),
        dict(id=2, description='february salary', amount=2500.0,
             currency='CLP'),
        dict(id=3, description='march salary', amount=3500.0,
             currency='CLP'),
    ]
    result = IncomeResponseSchema(many=True).dump(incomes)
    assert len(result) == 3  # only 3 incomes
    assert len(result[0]) == 4  # only 4 fields per income
    assert len(result[1]) == 4  # only 4 fields per income
    assert len(result[2]) == 4  # only 4 fields per income
    assert result[0]['description'] == 'january salary'
    assert result[1]['description'] == 'february salary'
    assert result[2]['description'] == 'march salary'


def test_single_income_response_schema():
    """
    Given Income dict
    When serialize using IncomeResponseSchema for single income
    Then verifies that the serialization corresponds
    """
    income = dict(id=1, description='january salary', amount=1500.0,
                  currency='CLP')
    result = IncomeResponseSchema().dump(income)
    assert result['id'] == 1
    assert result['description'] == 'january salary'
    assert result['amount'] == 1500.0
    assert result['currency'] == 'CLP'
