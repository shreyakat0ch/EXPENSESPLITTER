import csv

class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = float(amount)

class ExpenseSplitter:
    def __init__(self):
        self.expenses = []

    def add_expense(self, name, amount):
        expense = Expense(name, amount)
        self.expenses.append(expense)

    def calculate_shares(self):
        total_expense = sum(expense.amount for expense in self.expenses)
        num_people = len(set(expense.name for expense in self.expenses))
        share_per_person = total_expense / num_people
        return total_expense, share_per_person

    def calculate_balances(self, share_per_person):
        balances = {}
        for expense in self.expenses:
            if expense.name not in balances:
                balances[expense.name] = 0
            balances[expense.name] += expense.amount
        
        for name in balances:
            balances[name] -= share_per_person
        
        return balances

    def print_balances(self, balances):
        for name, balance in balances.items():
            if balance > 0:
                print(f"{name} is owed {balance:.2f}")
            elif balance < 0:
                print(f"{name} owes {-balance:.2f}")
            else:
                print(f"{name} is settled up")

    def save_to_file(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'amount'])
            for expense in self.expenses:
                writer.writerow([expense.name, expense.amount])

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            self.expenses = [Expense(row[0], float(row[1])) for row in reader]

def main():
    splitter = ExpenseSplitter()
    while True:
        print("\nExpense Splitter Menu:")
        print("1. Add Expense")
        print("2. Calculate Balances")
        print("3. Save Expenses to File")
        print("4. Load Expenses from File")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the name: ")
            amount = input("Enter the amount: ")
            splitter.add_expense(name, amount)
        elif choice == '2':
            total_expense, share_per_person = splitter.calculate_shares()
            balances = splitter.calculate_balances(share_per_person)
            splitter.print_balances(balances)
        elif choice == '3':
            filename = input("Enter the filename to save to: ")
            splitter.save_to_file(filename)
        elif choice == '4':
            filename = input("Enter the filename to load from: ")
            splitter.load_from_file(filename)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
