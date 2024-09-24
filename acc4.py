class Account:
    # Class variables
    bank_name = "Bank of Maharastra"
    currency = "INR"
    minimum_balance = 3000

    def __init__(self, account_number, holder_name, account_type, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = initial_balance

        if self.balance < Account.minimum_balance:
            raise ValueError(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}")

    # Deposit money
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} {Account.currency}")

    # Withdraw money
    def withdraw(self, amount):
        if self.balance - amount >= Account.minimum_balance:
            self.balance -= amount
            print(f"Withdrew {amount} {Account.currency}")
        else:
            print(f"Cannot withdraw. Minimum balance of {Account.minimum_balance} {Account.currency} required.")

    # Show balance
    def balance_enquiry(self):
        print(f"Current balance: {self.balance} {Account.currency}")

    # Display account details
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance} {Account.currency}")
        print(f"Bank Name: {Account.bank_name}")


# Helper function to check if a string is a valid float
def is_valid_float(value):
    if value.replace('.', '', 1).isdigit():
        return True
    return False


# Main program to interact with the user
def main():
    # Get user input to create an account
    while True:
        acc_number = input("Enter 10-digit account number: ")
        if len(acc_number) == 10 and acc_number.isdigit():
            break
        else:
            print("Invalid account number. Please enter a 10-digit number.")

    while True:
        holder_name = input("Enter account holder name: ")
        if holder_name.isalpha() and len(holder_name) > 0:
            break
        else:
            print("Invalid name. Please enter only alphabetic characters.")

    while True:
        acc_type = input("Enter account type (Savings/Current): ").capitalize()
        if acc_type in ["Savings", "Current"]:
            break
        else:
            print("Invalid account type. Please enter either 'Savings' or 'Current'.")

    # Ensure the initial balance is a numeric value and at least the minimum required amount
    while True:
        initial_balance_input = input(f"Enter initial balance (minimum {Account.minimum_balance} {Account.currency}): ")
        if is_valid_float(initial_balance_input):
            initial_balance = float(initial_balance_input)
            if initial_balance >= Account.minimum_balance:
                break
            else:
                print(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}. Please enter a valid amount.")
        else:
            print("Invalid input. Please enter a valid numeric value.")

    # Create the account
    account = Account(acc_number, holder_name, acc_type, initial_balance)

    # Menu options
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Display Account Details\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "3":
            account.balance_enquiry()
        elif choice == "4":
            account.display_details()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

# Run the main function
main()
