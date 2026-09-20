"""
Personal Expense Tracker
-------------------------
A simple command-line app to log, view, and visualize personal expenses.

Features:
- Add expenses (date, category, amount, description)
- View all expenses
- View summary by category
- Visualize spending with a bar chart
- Data persisted to a CSV file

Author: Your Name
"""

import csv
import os
from datetime import datetime
from collections import defaultdict

import matplotlib.pyplot as plt

DATA_FILE = "expenses.csv"
FIELDNAMES = ["date", "category", "amount", "description"]


def init_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, mode="w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
            writer.writeheader()


def add_expense(date, category, amount, description):
    """Append a new expense record to the CSV file."""
    with open(DATA_FILE, mode="a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writerow({
            "date": date,
            "category": category,
            "amount": amount,
            "description": description
        })
    print(f"Added: {date} | {category} | ${amount:.2f} | {description}")


def load_expenses():
    """Read all expenses from the CSV file into a list of dicts."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, mode="r", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


def view_expenses():
    """Print all expenses in a readable table format."""
    expenses = load_expenses()
    if not expenses:
        print("No expenses recorded yet.")
        return

    print(f"\n{'Date':<12}{'Category':<15}{'Amount':<10}{'Description'}")
    print("-" * 55)
    for e in expenses:
        print(f"{e['date']:<12}{e['category']:<15}${float(e['amount']):<9.2f}{e['description']}")
    print()


def summarize_by_category():
    """Return a dict of total spending per category."""
    expenses = load_expenses()
    totals = defaultdict(float)
    for e in expenses:
        totals[e["category"]] += float(e["amount"])
    return totals


def print_summary():
    """Print total spending per category and overall total."""
    totals = summarize_by_category()
    if not totals:
        print("No expenses to summarize.")
        return

    print("\nSpending Summary by Category")
    print("-" * 35)
    for category, total in sorted(totals.items(), key=lambda x: -x[1]):
        print(f"{category:<20}${total:.2f}")
    print("-" * 35)
    print(f"{'TOTAL':<20}${sum(totals.values()):.2f}\n")


def visualize_spending():
    """Show a bar chart of spending by category."""
    totals = summarize_by_category()
    if not totals:
        print("No data to visualize.")
        return

    categories = list(totals.keys())
    amounts = list(totals.values())

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color="steelblue")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount ($)")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()


def get_valid_date():
    while True:
        date_str = input("Date (YYYY-MM-DD, or press Enter for today): ").strip()
        if not date_str:
            return datetime.now().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")


def get_valid_amount():
    while True:
        amount_str = input("Amount: $").strip()
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Amount must be positive.")
                continue
            return amount
        except ValueError:
            print("Invalid amount. Please enter a number.")


def main_menu():
    init_file()

    menu = """
==== Personal Expense Tracker ====
1. Add expense
2. View all expenses
3. View summary by category
4. Visualize spending (bar chart)
5. Exit
"""
    while True:
        print(menu)
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            date = get_valid_date()
            category = input("Category (e.g. Food, Rent, Transport): ").strip() or "Uncategorized"
            amount = get_valid_amount()
            description = input("Description: ").strip()
            add_expense(date, category, amount, description)

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            print_summary()

        elif choice == "4":
            visualize_spending()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-5.")


if __name__ == "__main__":
    main_menu()
