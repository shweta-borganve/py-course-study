# Project 10: Personal Finance & Investment Tracker

**Difficulty:** ⭐⭐⭐⭐⭐ Hard  
**Real-world Use:** Financial planning, portfolio management, wealth tracking

## Project Overview

Build a comprehensive **Personal Finance & Investment Tracker**:
- Track multiple accounts (bank, investment, savings)
- Monitor investments (stocks, mutual funds, crypto)
- Calculate net worth
- Portfolio analysis and rebalancing
- Goal tracking and progress
- Tax reports
- Financial projections
- Risk analysis

## Features to Implement

1. **Account Management**:
   - Multiple account types: Bank, Investment, Savings, Credit Card
   - Balance tracking
   - Interest/dividend tracking
   - Account reconciliation

2. **Investment Tracking**:
   - Track stocks, mutual funds, crypto, bonds
   - Purchase price and current price
   - Quantity and total value
   - Gain/loss calculation
   - Dividend/interest tracking
   - Valuation history

3. **Portfolio Analysis**:
   - Asset allocation by type
   - Geographic allocation
   - Sector allocation
   - Diversification analysis
   - Rebalancing suggestions

4. **Goals & Targets**:
   - Set financial goals (buy house, retirement, etc.)
   - Track progress toward goals
   - Calculate required monthly savings
   - Timeline and milestones

5. **Performance Analysis**:
   - Return on investment (ROI)
   - Compare with benchmarks
   - Time-weighted returns
   - Year-to-date performance
   - Long-term performance trends

6. **Projections**:
   - Future value calculator
   - Retirement projection
   - Compound interest calculation
   - Investment growth scenarios

7. **Reports & Tax**:
   - Annual report
   - Gain/loss report (capital gains)
   - Dividend report
   - Tax-loss harvesting suggestions
   - Contribution report

8. **Risk Management**:
   - Volatility analysis
   - Risk assessment
   - Insurance needs
   - Emergency fund tracking

## Technologies/Concepts Needed
- Complex data structures
- Financial calculations (compound interest, ROI, etc.)
- Advanced algorithms
- Data visualization concepts
- File I/O
- Date/time operations
- Statistical analysis
- Sorting and filtering
- Real-time data (optional - API integration)

## Step-by-Step Guidance

### Step 1: Design Data Structures
```python
accounts = [
    {
        "id": 1,
        "name": "Checking Account",
        "type": "bank",
        "balance": 5000.00,
        "currency": "USD",
        "bank_name": "Bank of America",
        "interest_rate": 0.01,
        "created_date": "2020-01-01"
    }
]

investments = [
    {
        "id": 1,
        "account_id": 1,
        "symbol": "AAPL",
        "company_name": "Apple Inc",
        "type": "stock",  # stock, mutual_fund, crypto, bond
        "quantity": 10,
        "purchase_price": 120.00,
        "purchase_date": "2023-06-15",
        "current_price": 175.50,
        "current_value": 1755.00,
        "gain_loss": 555.00,
        "gain_loss_percent": 46.25,
        "sector": "Technology",
        "transactions": [
            {
                "date": "2023-06-15",
                "type": "buy",
                "quantity": 10,
                "price": 120.00
            }
        ]
    }
]

goals = [
    {
        "id": 1,
        "name": "Buy a House",
        "target_amount": 300000.00,
        "current_amount": 45000.00,
        "deadline": "2027-12-31",
        "monthly_contribution": 3000.00,
        "priority": "high",
        "created_date": "2024-01-01"
    }
]

transactions = [
    {
        "id": 1,
        "date": "2025-02-09",
        "account_id": 1,
        "type": "deposit",  # deposit, withdrawal, interest, dividend
        "amount": 500.00,
        "description": "Salary",
        "category": "Income"
    }
]
```

### Step 2: Create Core Financial Functions
- `add_investment(account_id, symbol, quantity, purchase_price)`
- `update_investment_price(symbol, current_price)`
- `calculate_portfolio_value()`
- `calculate_net_worth()` - Sum of all assets minus liabilities
- `calculate_roi(investment_id)` - Return on investment
- `calculate_gains_losses()` - Realized and unrealized gains
- `allocate_portfolio()` - Asset allocation percentages
- `rebalance_portfolio()` - Suggestions to rebalance
- `calculate_goal_progress(goal_id)`
- `project_future_value(principal, rate, years)` - Compound interest
- `generate_tax_report(year)`
- `get_performance_metrics()`

### Step 3: Advanced Calculations
```python
def calculate_portfolio_value():
    total = 0
    for account in accounts:
        total += account["balance"]
    
    for investment in investments:
        total += investment["current_value"]
    
    return total

def calculate_roi(investment):
    cost_basis = investment["quantity"] * investment["purchase_price"]
    current_value = investment["current_value"]
    gain = current_value - cost_basis
    roi_percent = (gain / cost_basis) * 100
    return roi_percent

def project_future_value(principal, annual_rate, years):
    # Compound interest: A = P(1 + r)^t
    return principal * (1 + annual_rate) ** years
```

### Step 4: Build Menu System
```
=== Personal Finance Tracker ===
1. Add Account
2. Add Investment
3. View All Accounts
4. View Portfolio
5. View Investments
6. Update Stock Prices
7. Add Expense/Income
8. View Net Worth
9. Goals & Progress
10. Performance Analysis
11. Projections
12. Tax Report
13. Portfolio Rebalancing
14. Analytics & Insights
15. Exit
```

## Example Usage

```
Choose option: 8
=== Net Worth Statement (Feb 9, 2025) ===

ASSETS:
Bank Accounts:
  - Checking: $5,000.00
  - Savings: $25,000.00
  Subtotal: $30,000.00

Investments:
  - Apple (AAPL): 10 shares @ $175.50 = $1,755.00
  - Tesla (TSLA): 5 shares @ $245.00 = $1,225.00
  - Vanguard 500 (VFIAX): 50 units @ $456.00 = $22,800.00
  Subtotal: $25,780.00

Real Estate (estimated):
  - Primary Home: $500,000.00
  Subtotal: $500,000.00

TOTAL ASSETS: $555,780.00

LIABILITIES:
  - Mortgage: $350,000.00
  - Credit Card: $2,500.00
  Subtotal: $352,500.00

NET WORTH: $203,280.00
Net Worth Change (Last Month): +$8,450.00 (↑ 4.3%)

Choose option: 5
=== Investment Portfolio ===

Portfolio Value: $25,780.00
Total Invested: $23,450.00
Unrealized Gain: +$2,330.00 (+9.9%)

Top Performers:
1. Vanguard 500 (VFIAX) - +15.2% gain
2. Apple (AAPL) - +46.25% gain
3. Tesla (TSLA) - -8.5% loss

Asset Allocation:
- Stocks: 15% ($3,980.00)
- Mutual Funds: 85% ($22,800.00)

Sector Breakdown:
- Technology: 45%
- Finance: 25%
- Healthcare: 20%
- Other: 10%

Choose option: 9
=== Financial Goals ===

1. Buy a House
   Target: $300,000.00
   Current: $45,000.00
   Progress: 15% ✓
   Monthly Contribution: $3,000.00
   Deadline: 2027-12-31 (2 years, 11 months)
   Status: On Track ✓

2. Retirement Fund
   Target: $1,000,000.00
   Current: $155,000.00
   Progress: 15.5%
   Required Monthly: $2,450.00 (to reach by age 65)
   Status: Behind schedule ⚠️

Choose option: 11
=== Investment Projections ===

Initial Investment: $25,000.00
Annual Return Rate: 8.0%
Time Period: 20 years

Projected Value: $116,309.40

Growth Timeline:
Year 5: $36,732.00
Year 10: $54,062.00
Year 15: $79,398.00
Year 20: $116,309.40

What-If Scenarios:
- 6% return: $80,406.00
- 8% return: $116,309.40
- 10% return: $168,386.00

Choose option: 12
=== Tax Report (2024) ===

Capital Gains:
- Realized Gains: $5,200.00 (Long-term: $4,800.00, Short-term: $400.00)
- Unrealized Gains: $8,450.00

Dividends Received: $1,250.00

Interest Income:
- Bank Interest: $150.00
- Bond Interest: $300.00
Total Interest: $450.00

Total Taxable Income: $6,900.00
Estimated Tax: $1,035.00 (15% rate)

Tax-Loss Harvesting Opportunities:
- Tesla: -$200.00 loss (can offset gains)
```

## Real-World Enhancement Ideas
1. **Real-time Stock Prices**: API integration (Alpha Vantage, IEX)
2. **Cryptocurrency Tracking**: Track crypto holdings
3. **Budget Integration**: Link with expense tracking
4. **Retirement Calculator**: Advanced retirement planning
5. **Insurance Needs**: Calculate coverage needed
6. **Debt Management**: Track and analyze debt payoff
7. **Recurring Contributions**: Automate regular investing
8. **Dollar-Cost Averaging**: Track regular purchases
9. **Dividend Tracking**: Detailed dividend analysis
10. **Tax Optimization**: Tax-loss harvesting automation
11. **Financial Ratio Analysis**: Debt-to-income, etc.
12. **Alerts**: Rebalancing alerts, goal milestones

## Grading Criteria
- ✅ Can add and manage accounts
- ✅ Investment tracking is accurate
- ✅ Net worth calculation is correct
- ✅ ROI and gains/losses calculated properly
- ✅ Portfolio analysis provides insights
- ✅ Goals track progress accurately
- ✅ Projections use correct formulas
- ✅ Tax reports are comprehensive
- ✅ Data persists between sessions
- ✅ User interface is professional
- ✅ Handles multiple currencies (bonus)
- ✅ Performance is fast with large datasets

## Important Financial Concepts
- **Compound Interest**: Growth + interest on interest
- **Return on Investment (ROI)**: (Gain / Cost) × 100
- **Asset Allocation**: Percentage in each asset type
- **Rebalancing**: Adjusting to target allocation
- **Dollar-Cost Averaging**: Regular investment strategy
- **Diversification**: Spreading risk across assets

## Notes
- Use realistic financial calculations
- Don't provide investment advice
- Always show disclaimers
- Use proper financial formulas
- Handle edge cases (zero division, negative amounts)
