# Prompt the user for their financial details
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected savings after one year with a 5% interest rate
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${projected_annual_savings:.2f}.")

