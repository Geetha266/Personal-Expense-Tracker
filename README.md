# Personal Expense Tracker

A simple command-line Python application to track personal expenses, view spending summaries, and visualize spending by category.

## Features

- Add expenses with date, category, amount, and description
- View all recorded expenses in a formatted table
- View a spending summary grouped by category
- Visualize spending with a bar chart (matplotlib)
- Data persisted locally in a CSV file (no database required)

## Tech Stack

- Python 3
- `csv` (standard library) for data storage
- `matplotlib` for data visualization

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

```bash
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
pip install -r requirements.txt
```

### Usage

```bash
python expense_tracker.py
```

Follow the on-screen menu to add expenses, view records, see summaries, or visualize your spending.

## Example

```
==== Personal Expense Tracker ====
1. Add expense
2. View all expenses
3. View summary by category
4. Visualize spending (bar chart)
5. Exit

Choose an option (1-5): 1
Date (YYYY-MM-DD, or press Enter for today):
Category (e.g. Food, Rent, Transport): Food
Amount: $45.50
Description: Groceries
Added: 2026-09-19 | Food | $45.50 | Groceries
```

## Possible Extensions

- Swap CSV storage for SQLite
- Add a Flask web interface
- Add monthly budget limits with alerts
- Export summaries to PDF

## License

MIT
