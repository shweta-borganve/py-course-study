# Project 2: Personal Expense Tracker

**Difficulty:** ⭐⭐⭐ Medium  
**Real-world Use:** Manage personal finances and spending

## Project Overview

Build an **Expense Tracker** application where users can:
- Record daily expenses with categories
- Track spending by category
- Generate reports (daily, weekly, monthly)
- Set spending budgets and get alerts
- Visualize spending patterns
- Export reports to CSV

## Features to Implement

1. **Record Expense**:
   - Date, description, amount, category
   - Categories: Food, Transport, Entertainment, Utilities, Shopping, Other

2. **View Expenses**:
   - All expenses
   - By date range (today, this week, this month)
   - By category
   - Sorted by amount or date

3. **Budget Management**:
   - Set monthly budget per category
   - Show warning if spending exceeds 80% of budget
   - Show exceeded categories

4. **Reports**:
   - Total spending per category
   - Daily average spending
   - Highest spending day
   - Most expensive category
   - Month-over-month comparison

5. **Statistics & Analytics**:
   - Total monthly spending
   - Average transaction amount
   - Spending trends

6. **Data Persistence**:
   - Save to CSV or JSON
   - Load on startup

## Technologies/Concepts Needed
- File I/O (CSV, JSON)
- Data structures (lists, dictionaries)
- Date/time operations
- Mathematical calculations
- Data analysis and filtering
- String formatting for reports

## Step-by-Step Guidance

### Step 1: Design Data Structure
```python
expenses = [
    {
        "date": "2025-02-09",
        "description": "Lunch at cafe",
        "amount": 8.50,
        "category": "Food"
    }
]

budget = {
    "Food": 300,
    "Transport": 150,
    "Entertainment": 100
}
```

### Step 2: Create Core Functions
- `add_expense(date, description, amount, category)`
- `get_expenses_by_date(start_date, end_date)`
- `get_expenses_by_category(category)`
- `get_category_spending()`
- `check_budget_alerts()`
- `generate_monthly_report()`
- `save_expenses()`
- `load_expenses()`

### Step 3: Build Menu System
```
=== Expense Tracker ===
1. Add Expense
2. View Expenses
3. View by Category
4. Set Budget
5. View Budget Alerts
6. Generate Report
7. Export to CSV
8. Statistics
9. Exit
```

### Step 4: Implement Date Filtering
- Use `datetime` module
- Support queries like "last 7 days", "this month"

## Example Usage

```
Choose option: 1
Enter date (YYYY-MM-DD): 2025-02-09
Enter description: Lunch
Enter amount: 12.50
Choose category: 
1. Food
2. Transport
3. Entertainment
4. Utilities
5. Shopping
6. Other
Choice: 1
✓ Expense recorded!

Choose option: 6
=== Monthly Report (February 2025) ===
Total Spending: $847.50

Spending by Category:
- Food: $350.00 (41.3%)
- Transport: $180.00 (21.2%)
- Entertainment: $150.00 (17.7%)
- Shopping: $100.00 (11.8%)
- Utilities: $67.50 (8.0%)

Highest Spending Day: 2025-02-05 ($75.00)
Average Daily Spending: $28.25

Budget Status:
✓ Food: $350 / $300 (OVER BUDGET by $50!)
✓ Transport: $180 / $200 (90% used)
✓ Entertainment: $150 / $150 (At limit)
```

## Real-World Enhancement Ideas
1. **Monthly Budgets**: Set different budgets for different months
2. **Recurring Expenses**: Automatic monthly bills
3. **Savings Goal**: Track money saved
4. **Expense Categories**: More detailed subcategories
5. **Receipt Storage**: Attach photo/notes to transactions
6. **Tax Calculator**: Calculate tax on purchases
7. **Graphical Reports**: Create charts/graphs
8. **Multi-user**: Different users with separate budgets
9. **Notifications**: Email alerts for budget overages
10. **Currency Support**: Handle multiple currencies

## Grading Criteria
- ✅ Can add and view expenses
- ✅ Categorization works correctly
- ✅ Budget alerts are accurate
- ✅ Reports are detailed and useful
- ✅ Data persists between sessions
- ✅ Date filtering works properly
- ✅ Mathematical calculations are correct
- ✅ User interface is clear and friendly
