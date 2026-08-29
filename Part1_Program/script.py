"""Part 1: Simple INR to USD expense converter."""

expenses_inr = [500, 1250, 799.50, 2100, 350]
INR_PER_USD = 95.5373

print("Expense Conversion (INR -> USD)")
print("-" * 38)

for expense in expenses_inr:
    usd = expense / INR_PER_USD
    print(f"INR {expense:,.2f} -> USD {usd:,.2f}")
