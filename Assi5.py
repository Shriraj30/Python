Finish subscribing to Google One … 90% of storage used. Get 30 GB for Drive, Gmail, and Google Photos. ₹59.00 ₹15.00/month for 3 months.
class Account:
    bank_name = "Bank of Maharashtra"
    currency = "INR"
    minimum_balance = 3000

    def __init__(self, account_number, holder_name, account_type, initial_balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.account_type = account_type
        self.balance = initial_balance

        if self.balance < Account.minimum_balance:
            raise ValueError(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount): 
        if amount <= 0:
            return False
        if self.balance - amount >= Account.minimum_balance:
            self.balance -= amount
            return True
        return False

    def balance_enquiry(self):
        return self.balance

    def display_details(self):
        return {
            "Account Number": self.account_number,
            "Holder Name": self.holder_name,
            "Account Type": self.account_type,
            "Balance": f"{self.balance:.2f} {Account.currency}",
            "Bank Name": Account.bank_name
        }


def is_valid_float(value):
    return value.replace('.', '', 1).isdigit() and len(value) > 0


def main():
    while True:
        acc_number = input("Enter 10-digit account number: ")
        if len(acc_number) == 10 and acc_number.isdigit():
            break
        else:
            print("Invalid account number. Please enter a 10-digit number.")

    while True:
        holder_name = input("Enter account holder name: ")
        if all(x.isalpha() or x.isspace() for x in holder_name) and len(holder_name) > 0:
            break
        else:
            print("Invalid name. Please enter only alphabetic characters and spaces.")

    while True:
        acc_type = input("Enter account type (Savings/Current): ").capitalize()
        if acc_type in ["Savings", "Current"]:
            break
        else:
            print("Invalid account type. Please enter either 'Savings' or 'Current'.")

    while True:
        initial_balance_input = input(f"Enter initial balance (minimum {Account.minimum_balance} {Account.currency}): ")
        if is_valid_float(initial_balance_input):
            initial_balance = float(initial_balance_input)
            if initial_balance >= Account.minimum_balance:
                break
            else:
                print(f"Initial balance must be at least {Account.minimum_balance} {Account.currency}.")
        else:
            print("Invalid input. Please enter a valid numeric value.")

    account = Account(acc_number, holder_name, acc_type, initial_balance)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Balance Enquiry\n4. Display Account Details\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            amount = input("Enter amount to deposit: ")
            if is_valid_float(amount):
                if account.deposit(float(amount)):
                    print("Deposit successful.")
                else:
                    print("Deposit amount must be positive.")
            else:
                print("nvalid amount. Please enter a valid numeric value.")
        elif choice == "2":
            amount = input("Enter amount to withdraw: ")
            if is_valid_float(amount):
                if account.withdraw(float(amount)):
                    print("Withdrawal successful.")
                else:
                    print("Cannot withdraw. Minimum balance required.")
            else:
                print("Invalid amount. Please enter a valid numeric value.")
        elif choice == "3":
            balance = account.balance_enquiry()
            print(f"Current balance: {balance:.2f} {Account.currency}")
        elif choice == "4":
            details = account.display_details()
            for key, value in details.items():
                print(f"{key}: {value}")
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

main()
