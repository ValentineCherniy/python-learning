print("Welcome to the Daily Expense Tracker!")
print("\nMenu:")
print("1. Add a new expense")
print("2. View all expenses")
print("3. Calculate total and average expense")
print("4. Clear all expenses")
print("5. Exit")
expenses_list = []
while True:
    menu_point = input()
    if menu_point == "1":
        expense = float(input())
        expenses_list.append(expense)
        #print(expenses_list)
        print("Expense added successfully!")
    elif menu_point == "2":
        if len(expenses_list) == 0:
            print("No expenses recorded yet.")
        else:
            print("Your expenses:")
            for i in range(0, len(expenses_list)):
                print (f"{i+1}. {expenses_list[i]}")
    elif menu_point == "3":
        if len(expenses_list) == 0:
            print("No expenses recorded yet.")
        else:
            total_expense = 0
            for i in range(0, len(expenses_list)):
                total_expense += expenses_list[i]
                average_expense = total_expense / len(expenses_list)
            print (f"Total expense: {total_expense}" )
            print(f"Average expense: {average_expense}")
    elif menu_point == "4":
        expenses_list = []
        print("All expenses cleared.")
    elif menu_point == "5":
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break