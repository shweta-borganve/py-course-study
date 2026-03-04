"""
Expense Tracker Application

A console-based expense tracking system that allows users to:
- Add and view expenses
- Set monthly budgets
- Check budget alerts
- Generate monthly reports
- Save and load data from CSV

Author: Your Name
Year: 2026
"""

import csv
from collections import defaultdict
from datetime import datetime

FILE_NAME = "expenses.csv"
CATEGORIES = (
    "Food",
    "Transport",
    "Entertainment",
    "Utilities",
    "Shopping",
    "Other",
)


class ExpenseTracker:
    """Main class for managing expenses and budgets."""

    def __init__(self):
        """Initialize expenses and budgets."""
        self.expenses = []
        self.budgets = {}
        self.load_expenses()

    def load_expenses(self):
        """Load expenses from CSV file."""
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["amount"] = float(row["amount"])
                    self.expenses.append(row)
        except FileNotFoundError:
            pass

    def save_expenses(self):
        """Save expenses to CSV file."""
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            fieldnames = ["date", "description", "amount", "category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def validate_date(self, date_text):
        """Validate date format YYYY-MM-DD."""
        try:
            datetime.strptime(date_text, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def add_expense(self):
        """Add a new expense."""
        date = input("Enter date (YYYY-MM-DD): ")

        if not self.validate_date(date):
            print("Invalid date format.")
            return

        description = input("Enter description: ")

        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                raise ValueError
        except ValueError:
            print("Invalid amount.")
            return

        print("Choose category:")
        for index, category in enumerate(CATEGORIES, start=1):
            print(f"{index}. {category}")

        try:
            choice = int(input("Choice: "))
            category = CATEGORIES[choice - 1]
        except (ValueError, IndexError):
            print("Invalid category choice.")
            return

        self.expenses.append(
            {
                "date": date,
                "description": description,
                "amount": amount,
                "category": category,
            }
        )

        print("✓ Expense added successfully!")

    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return

        for expense in self.expenses:
            print(
                f"{expense['date']} | "
                f"{expense['description']} | "
                f"${expense['amount']:.2f} | "
                f"{expense['category']}"
            )

    def set_budget(self):
        """Set monthly budget for each category."""
        print("Set Monthly Budget:")
        for category in CATEGORIES:
            try:
                amount = float(input(f"Budget for {category}: "))
                if amount < 0:
                    raise ValueError
                self.budgets[category] = amount
            except ValueError:
                print("Invalid input. Budget skipped.")

        print("✓ Budgets updated!")

    def check_budget(self):
        """Check budget usage and warnings."""
        spending = defaultdict(float)

        for expense in self.expenses:
            spending[expense["category"]] += expense["amount"]

        print("=== Budget Status ===")
        for category, budget in self.budgets.items():
            spent = spending[category]

            if budget == 0:
                print(f"{category}: No budget set.")
                continue

            percent = (spent / budget) * 100

            if percent >= 100:
                print(f"{category}: OVER BUDGET! (${spent:.2f}/{budget:.2f})")
            elif percent >= 80:
                print(f"{category}: Warning! {percent:.1f}% used")
            else:
                print(f"{category}: OK ({percent:.1f}% used)")

    def monthly_report(self):
        """Generate report for a specific month."""
        month = input("Enter month (YYYY-MM): ")

        total = 0
        category_total = defaultdict(float)
        daily_total = defaultdict(float)

        for expense in self.expenses:
            if expense["date"].startswith(month):
                total += expense["amount"]
                category_total[expense["category"]] += expense["amount"]
                daily_total[expense["date"]] += expense["amount"]

        print(f"\n=== Report for {month} ===")
        print(f"Total Spending: ${total:.2f}")

        print("\nSpending by Category:")
        for category, amount in category_total.items():
            print(f"{category}: ${amount:.2f}")

        if daily_total:
            highest_day = max(daily_total, key=daily_total.get)
            print(
                f"\nHighest Spending Day: {highest_day} "
                f"(${daily_total[highest_day]:.2f})"
            )

            average = total / len(daily_total)
            print(f"Average Daily Spending: ${average:.2f}")
        else:
            print("No data for this month.")

    def run(self):
        """Run the main menu loop."""
        while True:
            print("\n=== Expense Tracker ===")
            print("1. Add Expense")
            print("2. View Expenses")
            print("3. Set Budget")
            print("4. Check Budget")
            print("5. Monthly Report")
            print("6. Save & Exit")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_expense()
            elif choice == "2":
                self.view_expenses()
            elif choice == "3":
                self.set_budget()
            elif choice == "4":
                self.check_budget()
            elif choice == "5":
                self.monthly_report()
            elif choice == "6":
                self.save_expenses()
                print("Data saved. Goodbye!")
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
