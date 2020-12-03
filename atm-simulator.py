import random
import time

class Account:
    def __init__(self,id, checkingBalance= 0, savingBalance= 0, annualInterestRateSavings= 3.4):
        self.id = id
        self.checkingBalance = checkingBalance
        self.savingsBalance = savingBalance
        self.annualInterestRateSavings = annualInterestRateSavings
        def getId(self):
            return self.id
        def checkingAccountBalance(self):
            return self.checkingBalance
        def withdrawCheckingAmount(self, amount):
            self.checkingBalance -= amount
        def depositCheckingAmount(elf, amount):
            self.checkingBalance += amount
        def transferCheckingAmount(self, amount):
            self.checkingBalance += amount
            self.savingsBalance -= amount
        def savingsAccountBalance(self):
            return self.savingsBalance
        def withdrawSavingsAccount(self, amount):
            self.savingsBalance -= amount
        def depositSavingsAccount(self, amount):
            self.savingsBalance += amount
        def transferSavingsAccount(self, amount):
            self.savingsBalance += amount
            self.checkingBalance -= amount
        def savingsAccountMonthlyInterest(self):
            return self.savingsBalance * self.savingsAccountMonthlyInterest()
        def savingsAccountAnnualInterestRate(self):
            return self.annualInterestRateSavings
        def savingsAccountMonthlyInterestRate(self):
            return self.annualInterestRateSavings /12
def main():
    #creating accounts
    accounts = []
    for i in range(1000, 9999):
        account = Account(i, 0)
        accounts.append(account)

        while True:
            #reading id from user
            print("welcome to wanjas bank.")
            id = int( input("\nEnter 4 digit account pin: "))

            #loop till id is valid
            while id < 1000 or id > 9999:
                id = int(input("\nInvald Id..Re-Enter: "))
                #iterating over the interface
            while True:

                print("\nHow can we help you today?")
                print("""\n - View checking balance\t\t2 \n3 - Deposit checking \t\t\t4 - transfer Checking \n5 - View 
                Savings Balance \t\t6 - Withdraw Savings \n7 - Deposit Savings \t\t\t8 - Transfer Savings \9n - Exit """)


