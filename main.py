from expense import Expense

def main():
    expense_file_path="expenses.csv"

    #Get user input for expense
    expense= input_expense()

    #Write their expense to a file
    save_expense(expense, expense_file_path)

    #Read file and sumarize expenses
    read_expense(expense_file_path)
def input_expense():
    categories = ["Food", "Work", "Home", "Luxury", "Misc"]
    expense_name=input(f"Whats the name of this expense: ")
    expense_amount=float(input(f"And how much was it?: "))
    while True:
        for i, category_name in enumerate(categories):
            print(f" {i + 1}. {category_name}")

        value_range = f"[1 - {len(categories)}]"

        try:
            selected_index = int(input(f"Enter a category number {value_range}: ")) - 1 
            if selected_index in range(0, len(categories)):
                selected_category = categories[selected_index]
                new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
                return new_expense
            else:
                print("Invalid number, please try again")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def save_expense(expense, expense_file_path):
    print(f"saving {expense} to {expense_file_path}")
    with open(expense_file_path, "a")as f:
        f.write(f"{expense.name},{expense.category},{expense.amount}\n")

def read_expense(expense_file_path):
    print(f"")
    expenses = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
            print(line_expense)
            expenses.append(line_expense)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("Expenses by category: ")
    for key, amount in amount_by_category.items():
        print(f"  {key}: ${amount:.2f}")


if __name__ == "__main__":
    main()