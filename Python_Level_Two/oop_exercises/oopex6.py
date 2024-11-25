class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def create_acc(self, accNumber, username, balance):
        # Check if account number already exists
        for customer in self.customers:
            if customer["accNumber"] == accNumber:
                print(f"Account number {accNumber} is already in use.\n")
                return  # Exit the method if a duplicate is found

        # If no duplicate found, add new customer to the list
        self.customers.append({"name": username, "accNumber": accNumber, "balance": balance})
        print(f"Account created for {username}. AccNo: {accNumber}, Balance: {balance}\n")

    def deposit(self, accNumber, amount):
        for customer in self.customers:
            if customer["accNumber"] == accNumber:
                customer["balance"] += amount
                print(f"Deposited {amount} to account {accNumber}. New balance: {customer['balance']}\n")
                return
        print(f"Account number {accNumber} not found.\n")

    def withdraw(self, accNumber, withdrawal_amount):
        for customer in self.customers:
            if customer["accNumber"] == accNumber:
                if withdrawal_amount > customer['balance']:
                    print(f"Insufficient funds! Your current balance is {customer['balance']}.\n"
                          f"You cannot withdraw more than your account balance.\n")
                    return
                
                customer['balance'] -= withdrawal_amount
                print(f"{withdrawal_amount} withdrawn from account {accNumber}. "
                      f"New balance: {customer['balance']}\n")
                return
        print(f"Account number {accNumber} not found.\n")

    def check_balance(self, accNumber):
        for customer in self.customers:
            if customer["accNumber"] == accNumber:
                print(f"Hello {customer['name']}!\n"
                      f"Your current balance is: {customer['balance']}\n")
                return
        print(f"Account number {accNumber} not found.\n")


# Example Usage
chase = Bank("Chase Bank")
chase.create_acc(1001, "Robins Thiaine", 0)
chase.deposit(1001, 1000)
chase.withdraw(1001, 5000)  # Attempt to overdraw
chase.withdraw(1001, 500)   # Valid withdrawal
chase.check_balance(1001)
