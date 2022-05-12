import pytest
from components.income.models import Income


def test_create_income():
    """
    Given Income class instance
    When set attributes for description & amount
    Then check values of description & amount are valid
    """
    income = Income(description='january salary', amount=2500)
    assert income.description == 'january salary'
    assert income.amount == 2500


def test_fail_create_income_without_description():
    """
    Given Income class instance
    When set attributes only for amount
    Then check TypeError exception is raised
    """
    with pytest.raises(TypeError):
        Income(amount=2500)


def test_fail_create_income_without_amount():
    """
    Given Income class instance
    When set attributes only for description
    Then check TypeError exception is raised
    """
    with pytest.raises(TypeError):
        Income(description='january salary')


def test_fail_create_income_without_params():
    """
    Given Income class instance
    When set none attributes for object
    Then check TypeError exception is raised
    """
    with pytest.raises(TypeError):
        Income()
