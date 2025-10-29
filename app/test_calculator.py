import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.calculator import MortgageCalculator


class TestMortgageCalculator(unittest.TestCase):

    def test_monthly_payment(self):
        calculator = MortgageCalculator(1000000, 5, 10)
        monthly_payment = calculator.calculate_monthly_payment()
        # Ожидаемое значение из онлайн-калькуляторов
        self.assertEqual(monthly_payment, 10606.55)

    def test_total_payment(self):
        calculator = MortgageCalculator(1000000, 5, 10)
        total_payment = calculator.calculate_total_payment()
        # 10606.55 * 120 = 1272786.0
        self.assertEqual(total_payment, 1272786.0)

    def test_total_interest(self):
        calculator = MortgageCalculator(1000000, 5, 10)
        total_interest = calculator.calculate_total_interest()
        # 1272786.0 - 1000000 = 272786.0
        self.assertEqual(total_interest, 272786.0)

    def test_zero_interest(self):
        calculator = MortgageCalculator(100000, 0, 5)
        monthly_payment = calculator.calculate_monthly_payment()
        # 100000 / 60 = 1666.666... округляется до 1666.67
        self.assertEqual(monthly_payment, 1666.67)

    def test_amortization_schedule(self):
        calculator = MortgageCalculator(100000, 5, 1)
        schedule = calculator.get_amortization_schedule(3)

        self.assertEqual(len(schedule), 3)

        # Проверяем структуру данных
        for payment in schedule:
            self.assertIn('month', payment)
            self.assertIn('payment', payment)
            self.assertIn('principal', payment)
            self.assertIn('interest', payment)
            self.assertIn('balance', payment)

            # Проверяем, что платеж = основной долг + проценты
            self.assertAlmostEqual(
                payment['payment'],
                payment['principal'] + payment['interest'],
                delta=0.01
            )

    def test_amortization_schedule_accuracy(self):
        """Проверка точности графика платежей"""
        calculator = MortgageCalculator(100000, 5, 1)
        schedule = calculator.get_amortization_schedule(1)

        if schedule:
            first_payment = schedule[0]
            expected_interest = 100000 * (5 / 100 / 12)  # ~416.67
            self.assertAlmostEqual(first_payment['interest'], 416.67, delta=1.0)


if __name__ == '__main__':
    unittest.main()