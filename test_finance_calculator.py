import pytest
from finance_calculator import FinanceCalculator

@pytest.fixture
def calculator():
    return FinanceCalculator()

def test_initial_balance(calculator):
    assert calculator.get_balance() == 0

def test_add_income(calculator):
    calculator.add_income(1000, "Зарплата")
    assert calculator.get_balance() == 1000
    assert calculator.get_transactions() == [("Зарплата", 1000)]

def test_add_expense(calculator):
    calculator.add_income(1000)
    calculator.add_expense(500, "Продукты")
    assert calculator.get_balance() == 500
    assert calculator.get_transactions() == [("Доход", 1000), ("Продукты", -500)]

def test_expense_exceeds_balance(calculator):
    calculator.add_income(300)
    with pytest.raises(ValueError, match="Обнаружено недостаточное количество."):
        calculator.add_expense(500)

def test_invalid_income_amount(calculator):
    with pytest.raises(ValueError, match="Доход должен быть больше 0."):
        calculator.add_income(-100)

def test_invalid_expense_amount(calculator):
    with pytest.raises(ValueError, match="Расход должен быть больше 0."):
        calculator.add_expense(-50)

print("Тесты завершены!")
