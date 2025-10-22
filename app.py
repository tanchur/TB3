import tkinter as tk
from tkinter import ttk, messagebox
from calculator import MortgageCalculator


class MortgageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор ипотеки")
        self.root.geometry("500x600")

        self.setup_ui()

    def setup_ui(self):
        # Поля ввода
        ttk.Label(self.root, text="Сумма кредита:").pack(pady=5)
        self.principal_entry = ttk.Entry(self.root)
        self.principal_entry.pack(pady=5)

        ttk.Label(self.root, text="Годовая процентная ставка (%):").pack(pady=5)
        self.rate_entry = ttk.Entry(self.root)
        self.rate_entry.pack(pady=5)

        ttk.Label(self.root, text="Срок кредита (лет):").pack(pady=5)
        self.years_entry = ttk.Entry(self.root)
        self.years_entry.pack(pady=5)

        # Кнопка расчета
        ttk.Button(self.root, text="Рассчитать", command=self.calculate).pack(pady=10)

        # Результаты
        self.results_frame = ttk.LabelFrame(self.root, text="Результаты")
        self.results_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.results_text = tk.Text(self.results_frame, height=15, width=50)
        self.results_text.pack(pady=10, padx=10, fill="both", expand=True)

    def calculate(self):
        try:
            principal = float(self.principal_entry.get())
            rate = float(self.rate_entry.get())
            years = int(self.years_entry.get())

            calculator = MortgageCalculator(principal, rate, years)

            monthly_payment = calculator.calculate_monthly_payment()
            total_payment = calculator.calculate_total_payment()
            total_interest = calculator.calculate_total_interest()
            schedule = calculator.get_amortization_schedule(12)

            results = f"Ежемесячный платеж: {monthly_payment:.2f} ₽\n"
            results += f"Общая сумма выплат: {total_payment:.2f} ₽\n"
            results += f"Общие проценты: {total_interest:.2f} ₽\n\n"
            results += "График платежей (первые 12 месяцев):\n"
            results += "Месяц | Платеж | Основной долг | Проценты | Остаток\n"

            for payment in schedule:
                results += f"{payment['month']:2} | {payment['payment']:7.2f} | {payment['principal']:7.2f} | {payment['interest']:7.2f} | {payment['balance']:7.2f}\n"

            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(1.0, results)

        except ValueError as e:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числовые значения")


if __name__ == "__main__":
    root = tk.Tk()
    app = MortgageApp(root)
    root.mainloop()