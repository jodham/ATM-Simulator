import random

amount = 0.0
loggedOn = True

while loggedOn:
    selection = int(input("Select 1 for Deposit, 2 for withdraw or 3 for Exit"))
    if not selection:
        break
    if selection == 1:
        deposit = float(input("How much will you deposit"))
        amount += deposit
        print(f"Deposit in the amount of ${format(deposit, '.2f')} ")
        print(f"Bank account balance ${format(amount, '.2f')} ")
    elif selection == 2:
        withdraw = float(input("How much will you withdraw?"))
        amount -= withdraw
        print(f"Withdraw in the amount of ${format(withdraw, '.2f')}")
        print(f"Bank account balance ${format(amount, '.2f')} ")
    else:
        print("Thanks for choosing our bank")
        loggedOn = False

print("Transaction number:",random.randint(10000, 1000000))
