print("Monthly Budget Calculator")

# Ask for total monthly budget
total_budget = float(input("Enter your total monthly budget (LKR): "))

remaining_balance = total_budget

print("\nEnter your expenses one by one.")
print("Type 'done' to finish.\n")

while True:
    expense = input("Enter expense amount (LKR): ")

    if expense.lower() == "done":
        break

    expense = float(expense)

    if expense > remaining_balance:
        print("❌ Expense exceeds remaining balance. Transaction cancelled.")
        continue

    remaining_balance -= expense
    print("Remaining balance:", remaining_balance, "LKR")

# Final summary
print("\n------ Budget Summary ------")
print("Total Budget:", total_budget, "LKR")
print("Remaining Balance:", remaining_balance, "LKR")

if remaining_balance < 500:
    print("⚠ WARNING: Your balance is below 500 LKR!")