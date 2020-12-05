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
        if amount >= withdraw:
            amount -= withdraw
            print(f"\nWithdraw in the amount of ${format(amount, '.2f')}")
            print(f"Bank account balance ${format(amount, '.2f')}")
        else:
            print("\nThis transaction cannot be completed")
            print("your balance",+amount, "is less than requested amount")
    else:
        loggedOn = False
        print("\nTransaction id :", random.randint(10000, 1000000))



