class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited {amount}")
            print(f"Deposited {amount} into Account {self.account_number}. New balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transactions.append(f"Withdrew {amount}")
            print(f"Withdrew {amount} from Account {self.account_number}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} balance: {self.balance}")

    def display_transactions(self):
        print(f"Transactions for Account {self.account_number}:")
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account {account_number} created successfully.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print("Account not found.")
            return None



bank = Bank()


bank.create_account("12345", 1000)
bank.create_account("67890", 500)


account1 = bank.get_account("12345")
if account1:
    account1.deposit(500)
    account1.withdraw(200)

account2 = bank.get_account("67890")
if account2:
    account2.deposit(1000)

account1.display_balance()
account1.display_transactions()

account2.display_balance()
account2.display_transactions()
