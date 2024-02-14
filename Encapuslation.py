class BankAccount:
    def __init__(self, name, balance):
        self.__name = name  # Private attribute for account holder name
        self.__balance = balance  # Private attribute for account balance

    # Getter method to access balance
    def get_balance(self):
        return self.__balance

    # Setter method to deposit money (with validation)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to display account information
    def show_details(self):
        print(f"Account Holder: {self.__name}")
        print(f"Balance: ${self.__balance}")

# Create an account object
account = BankAccount("John Doe", 500.00)

# Trying to directly access private attribute throws an error
# print(account.__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Use public methods to access and modify balance
account.deposit(100.00)
account.show_details()  # Output: Account Holder: John Doe, Balance: $600.00

