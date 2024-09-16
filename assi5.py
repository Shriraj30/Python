class Account:
    # Class variables
    currency = "USD"
    min_balance = 3000
    bank_name = "ABC Bank"

    def __init__(self, account_number, holder_name, balance, account_type):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.account_type = account_type
        
        # Check if the initial balance is at least the minimum balance
        if self.balance < Account.min_balance:
            print(f"Initial deposit must be at least {Account.min_balance} {Account.currency}. Account creation failed.")
            self.balance = 0  # Set balance to 0 if not valid
        else:
            print(f"Account created successfully with balance: {self.balance} {Account.currency}")
    
    # Member function to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} {Account.currency}. New balance: {self.balance} {Account.currency}")
        else:
            print("Invalid deposit amount!")
    
    # Member function to withdraw money
    def withdraw(self, amount):
        if amount > 0 and self.balance - amount >= Account.min_balance:
            self.balance -= amount
            print(f"Withdrew {amount} {Account.currency}. New balance: {self.balance} {Account.currency}")
        else:
            print(f"Withdrawal denied! Minimum balance of {Account.min_balance} {Account.currency} must be maintained.")

    # Member function for balance inquiry
    def balance_enquiry(self):
        print(f"Your current balance is {self.balance} {Account.currency}")

    # Member function to display all details
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance} {Account.currency}")
        print(f"Bank Name: {Account.bank_name}")

# Accepting input from the user to create an account dynamically
account_number = input("Enter Account Number: ")
holder_name = input("Enter Account Holder Name: ")
balance = float(input(f"Enter Initial Balance (minimum {Account.min_balance} {Account.currency}): "))
account_type = input("Enter Account Type (e.g., Savings, Checking): ")

# Creating the account
acc = Account(account_number, holder_name, balance, account_type)

# Display account details
acc.display_details()

# Accepting input for deposit and withdrawal
deposit_amount = float(input("Enter amount to deposit: "))
acc.deposit(deposit_amount)

withdraw_amount = float(input("Enter amount to withdraw: "))
acc.withdraw(withdraw_amount)

# Balance enquiry
acc.balance_enquiry()
