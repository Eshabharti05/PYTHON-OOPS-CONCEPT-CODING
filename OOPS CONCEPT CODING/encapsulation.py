class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Insufficient balance or invalid withdrawal amount.")

    def __get_balance(self):
        return self.__balance


# Create an account
account = BankAccount(1000)

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)

# Get the current balance
print("Current balance:", account._BankAccount__get_balance())
