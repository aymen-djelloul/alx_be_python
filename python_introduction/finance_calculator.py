monthly_income = input("Enter your monthly income: ")
total_monthly_expenses = input("Enter your total monthly expenses: ")

Monthly_Savings = int(monthly_income) - int(total_monthly_expenses)

Projected_savings_after_1y =  Monthly_Savings * 12 + ( Monthly_Savings* 0.05 )

print(f"Your monthly savings are : {Monthly_Savings}")
print(f"Projected savings after one year, with interest, is: {int(Projected_savings_after_1y)}")