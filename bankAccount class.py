# Bank account class

balance = 0
account_number = int(input("Enter the account number: "))

class bankAccount:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number
    def Balance(self):
        print("Balance is", self.balance)
    def deposit(self):
        self.balance += dep_amount
        print("The amount is deposited")
    def withdraw(self):
        self.balance -= withdraw_amount
        print("The amount is withdrawn")

obj = bankAccount(balance, account_number)

while True:
    print("1. Show balance\n2. Deposit amount\n3. Withdraw amount\n4. Exit\n")
    option = int(input("Enter the option(1/2/3): "))
    print()

    if option == 1:
        obj.Balance()
    elif option == 2:
        dep_amount = int(input("Enter amount to deposit: "))
        obj.deposit()
    elif option == 3:
        withdraw_amount = int(input("Enter the amount to withdraw: "))
        obj.withdraw()
    else:
        break