expenses = []
while True :
    expense = input("Enter your expenses(or type done if you are finished)")
    if expense.lower() == "done" :
        break
    else :
        try:
            expense = float(expense)
            expenses.append(expense)
        except ValueError:
            print("Please enter a valid number:")
print("Your total expenses are:", sum(expenses))
for i in range(len(expenses)):
    print(f"Expense {i+1}: {expenses[i]}")
print("Number of expenses:", len(expenses))


            
