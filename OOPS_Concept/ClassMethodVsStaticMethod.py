class BankAccount:
    """
    
      Class Method:
          Used for operations that affect the class as a whole, such as modifying class-level data.
          Can access class variables via cls.
      Static Method:
          Used for utility functions that don’t require any information from the class or its instances.
          Cannot access class or instance data unless passed explicitly as arguments.

    """
    # Class variable (shared by all instances)
    bank_name = "ABC Bank"
    interest_rate = 5.0  # Default interest rate for all accounts

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Instance variable
        self.balance = balance  # Instance variable

    # Class Method
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate  # Modify class-level interest rate for all accounts
        print(f"Interest rate changed to {cls.interest_rate}% for all accounts.")

    # Static Method
    @staticmethod
    def validate_account_number(account_number):
        # A utility function that checks if the account number is valid
        if len(account_number) == 10 and account_number.isdigit():
            return True
        return False

    # Instance Method
    def show_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank: {BankAccount.bank_name}")
        print(f"Balance: ${self.balance}")
        print(f"Interest Rate: {BankAccount.interest_rate}%")


# Changing the interest rate for all accounts by Using the Class Method:
BankAccount.set_interest_rate(6.5)

# Creating an instance and showing account details by Using an Instance Method:
account1 = BankAccount('John Doe', 1000)
account1.show_account_details()

# Validating an account number by using the Static Method:
print(BankAccount.validate_account_number('1234567890'))  # Output: True
print(BankAccount.validate_account_number('12345abcd'))    # Output: False
