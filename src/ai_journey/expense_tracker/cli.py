import datetime

from ai_journey.expense_tracker.models import Expense
from report import print_report

if __name__ == "__main__":

    e1 = Expense(amount=12.5, category="food", note="lunch")
    e2 = Expense(amount=20.0, category="transportation", note="bus fare")
    e3 = Expense(amount=15.0, category="food", note="dinner")
    # e4 = Expense(amount=-5.0, category="", note="movie tickets")  # This will raise an InvalidExpense exception

    expenses = [e1, e2, e3]
    print("Expenses:" , expenses)

    print(print_report(expenses))