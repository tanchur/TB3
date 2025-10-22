import math


class MortgageCalculator:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.monthly_rate = annual_rate / 100 / 12
        self.months = years * 12

    def calculate_monthly_payment(self):
        if self.monthly_rate == 0:
            return round(self.principal / self.months, 2)  # Округляем до копеек

        factor = math.pow(1 + self.monthly_rate, self.months)
        monthly_payment = self.principal * self.monthly_rate * factor / (factor - 1)
        return round(monthly_payment, 2)  # Округляем до копеек

    def calculate_total_payment(self):
        monthly_payment = self.calculate_monthly_payment()
        total = monthly_payment * self.months
        return round(total, 2)  # Округляем до копеек

    def calculate_total_interest(self):
        total_payment = self.calculate_total_payment()
        return round(total_payment - self.principal, 2)  # Округляем до копеек

    def get_amortization_schedule(self, months=12):
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()

        for month in range(1, min(months + 1, self.months + 1)):
            interest = balance * self.monthly_rate
            principal = monthly_payment - interest

            # Корректируем последний платеж
            if principal > balance:
                principal = balance
                monthly_payment = principal + interest

            balance -= principal

            schedule.append({
                'month': month,
                'payment': round(monthly_payment, 2),
                'principal': round(principal, 2),
                'interest': round(interest, 2),
                'balance': round(balance, 2)
            })

            if balance <= 0:
                break

        return schedule