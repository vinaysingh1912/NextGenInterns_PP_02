class BankAccount:
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposit Successful. New balance is ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please try again.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal Successful. New balance is ${self.balance:.2f}")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please try again.")
        else:
            print("Insufficient funds. Please deposit more money.")

    def check_balance(self):
        print(f"Account balance is ${self.balance:.2f}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder):
        if account_number not in self.accounts:
            self.accounts[account_number] = BankAccount(account_number, account_holder)
            print("Account created successfully.")
        else:
            print("Account number already exists. Please try again.")

    def get_account(self, account_number):
        return self.accounts.get(account_number)


def main():
    bank = Bank()

    while True:
        print("\n1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder's name: ")
            bank.create_account(account_number, account_holder)
        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            account = bank.get_account(account_number)
            if account:
                account.deposit(amount)
            else:
                print("Account not found. Please create an account first.")
        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            account = bank.get_account(account_number)
            if account:
                account.withdraw(amount)
            else:
                print("Account not found. Please create an account first.")
        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found. Please create an account first.")
        elif choice == "5":
            print("Thank You for using the bank.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
