import pytest
from finance_calculator import FinanceCalculator

@pytest.fixture
def calculator():
    return FinanceCalculator()

def test_initial_balance(calculator):
    assert calculator.get_balance() == 0

def test_add_income(calculator):
    calculator.add_income(1000, "Salary")
    assert calculator.get_balance() == 1000
    assert calculator.get_transactions() == [("Salary", 1000)]

def test_add_expense(calculator):
    calculator.add_income(1000)
    calculator.add_expense(500, "Groceries")
    assert calculator.get_balance() == 500
    assert calculator.get_transactions() == [("Income", 1000), ("Groceries", -500)]

def test_expense_exceeds_balance(calculator):
    calculator.add_income(300)
    with pytest.raises(ValueError, match="Insufficient funds."):
        calculator.add_expense(500)

def test_invalid_income_amount(calculator):
    with pytest.raises(ValueError, match="Income must be greater than zero."):
        calculator.add_income(-100)

def test_invalid_expense_amount(calculator):
    with pytest.raises(ValueError, match="Expense must be greater than zero."):
        calculator.add_expense(-50)


print("Tests done!")
