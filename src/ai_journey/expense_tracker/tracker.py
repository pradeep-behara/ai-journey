import datetime

def add_expense(expenses, amount, catogery, *, note="", data=None): 
    expenses.append({"amount": amount, "category": catogery, "note": note, "date": data or default_date})

def total_by_category(expenses):
    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        category_totals[category] = category_totals.get(category, 0) + amount
    return category_totals

def largest(expenses, n=3):
    return sorted(expenses, key=lambda x: x["amount"], reverse=True)[:n] # AI inline suggested this line -- I need to learn indepth about this 

def print_report(expenses):
    totals = total_by_category(expenses)
    print(f"category>:20 count:>20 total:>20")
    for category, total in totals.items():
       print(f"{category:>20} {len([e for e in expenses if e['category'] == category]):>20} {total:>20.2f}")
    print(f"Total expenses: {sum(e['amount'] for e in expenses):>20.2f}")
expenses = {"amount": 12.5, "category": "food", "note": "lunch", "date": "2026-10-12"}

default_date = datetime.date.today().isoformat()

if __name__ == "__main__":
    expenses = []
    add_expense(expenses, 12.5, "food", note="lunch")
    add_expense(expenses, 20.0, "transportation", note="bus fare")
    add_expense(expenses, 15.0, "food", note="dinner")
    add_expense(expenses, 30.0, "entertainment", note="movie tickets")
    
    print_report(expenses)
