class BankAccount:
    def __init__(self,
                 account_holder,intial_balance=0.0):
        self.account_holder =account_holder
        self.balance =initial_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print(f"deposited ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")
            def withdraw(self, amount):
                if amount <= 0:
                    print("withdrawal amount must be positive.")
                elif amount > self.balance:
                    print("insufficient funds! current balance: ${self.balance:.2f}")
                else:
                    self.balance -= amount
                    print(f"withdraew ${amount:.2f}")

            def display_account_info(self):
                print(f"account holder:{self.account_holder} | Current Balance: ${self.balance:.2f}")
#    required driver script
print("---testing Account 1(Alice) ---")
account1 =BankAccount("Alice",100.00)
account1.deposit(50.00)
account1.withdraw(30.00)
account1.withdraw(200.00)
account1.display_account_info()

print("\n--- Testing Account 2(Martin)---")
account2 = BankAccount("Martin")
account2.deposit(-10.00)
account2.deposit(75.00)
account2.display_account_info()