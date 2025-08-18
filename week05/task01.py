
class BankAccount:
    def __init__(self, account_number, owner_name, balance=0.0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited {amount} successfully. New balance: {self.balance}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"✅ Withdrawn {amount} successfully. New balance: {self.balance}")
            else:
                print("❌ Insufficient funds.")
        else:
            print("❌ Withdrawal amount must be positive.")

    def transfer(self, target_account, amount):
        """Transfer money to another BankAccount."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                target_account.balance += amount
                print(f"✅ Transferred {amount} to {target_account.owner_name}. New balance: {self.balance}")
            else:
                print("❌ Insufficient funds for transfer.")
        else:
            print("❌ Transfer amount must be positive.")

    def display_info(self):
        """Display account details."""
        print(f"🏦 Account Number: {self.account_number}")
        print(f"👤 Owner Name: {self.owner_name}")
        print(f"💰 Balance: {self.balance}")


# Example Usage
acc1 = BankAccount("001", "Ahsaan", 5000)
acc2 = BankAccount("002", "Ali", 2000)

acc1.deposit(1500)
acc1.withdraw(1000)
acc1.transfer(acc2, 2000)

acc1.display_info()
acc2.display_info()
