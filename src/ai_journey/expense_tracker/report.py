from collections.abc import Iterator
from typing import Iterable

from ai_journey.expense_tracker.models import Expense

def timed(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result
    return wrapper

def by_category(expenses: Iterable[Expense], category: str) -> Iterator[Expense]:
    """Filter expenses by category."""
    return (expense for expense in expenses if expense.category == category)

@timed
def print_report(expenses):
    totals = by_category(expenses, category="food")
    print(f"category>:20 count:>20 total:>20")
    for category, total in totals.items():
       print(f"{category:>20} {len([e for e in expenses if e['category'] == category]):>20} {total:>20.2f}")
    print(f"Total expenses: {sum(e['amount'] for e in expenses):>20.2f}")