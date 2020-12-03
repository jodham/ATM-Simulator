import random
import time

class account:
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
