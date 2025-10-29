
import tkinter as tk
from tkinter import messagebox


class FinanceCalculatorApp:
    def __init__(self, root):
        self.calculator = FinanceCalculator()

        root.title("Finance Calculator")
        root.geometry("400x300")

        # Labels and Entry fields
        self.amount_label = tk.Label(root, text="Число:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.description_label = tk.Label(root, text="Описание:")
        self.description_label.pack()

        self.description_entry = tk.Entry(root)
        self.description_entry.pack()

        # Buttons
        self.add_income_button = tk.Button(root, text="Добавить доход", command=self.add_income)
        self.add_income_button.pack()

        self.add_expense_button = tk.Button(root, text="Добавить расход", command=self.add_expense)
        self.add_expense_button.pack()

        self.show_balance_button = tk.Button(root, text="Баланс", command=self.show_balance)
        self.show_balance_button.pack()

        self.show_transactions_button = tk.Button(root, text="История операций", command=self.show_transactions)
        self.show_transactions_button.pack()

    def add_income(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get() or "Баланс"
            self.calculator.add_income(amount, description)
            messagebox.showinfo("Выполнено!", "Доход добавлен!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_expense(self):
        try:
            amount = float(self.amount_entry.get())
            description = self.description_entry.get() or "Расход"
            self.calculator.add_expense(amount, description)
            messagebox.showinfo("Выполнено!", "Расход добавлен!")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def show_balance(self):
        balance = self.calculator.get_balance()
        messagebox.showinfo("Баланс", f"Ваш баланс: {balance:.2f}$")

    def show_transactions(self):
        transactions = self.calculator.get_transactions()
        transactions_str = "\n".join([f"{desc}: {amt:.2f}" for desc, amt in transactions])
        messagebox.showinfo("Операции", transactions_str or "Пусто...")


class FinanceCalculator:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def add_income(self, amount, description="Доход"):
        if amount <= 0:
            raise ValueError("Доход должен быть больше 0.")
        self.balance += amount
        self.transactions.append((description, amount))

    def add_expense(self, amount, description="Расход"):
        if amount <= 0:
            raise ValueError("Расход должен быть больше 0.")
        if amount > self.balance:
            raise ValueError("Обнаружено недостаточное количество.")
        self.balance -= amount
        self.transactions.append((description, -amount))

    def get_balance(self):
        return self.balance

    def get_transactions(self):
        return self.transactions


if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceCalculatorApp(root)
    root.mainloop()
