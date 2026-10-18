from dataclasses import dataclass
import datetime

# def add_expense(expenses, amount, catogery, *, note="", data=None): 

class InvalidExpense(Exception):
    pass

@dataclass
class Expense:
    amount: float
    category: str
    note: str = ""
    date: datetime.date = datetime.date.today()

    def __post_init__(self):
        if self.amount < 0:
            raise InvalidExpense("Amount must be non-negative.")
        if self.category == "":
            raise InvalidExpense("Category must be provided.")