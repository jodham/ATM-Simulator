import random

amount = 0.0
loggedOn = True
withdrawalAmount = 23
sendingCharges = 15

while loggedOn:
    selection = int(input("Select 1 for Deposit, 2 for withdraw ,3 for send money or 4 for Exit"))
    if not selection:
        break
    if selection == 1:
        deposit = float(input("How much will you deposit"))
        amount += deposit
        print(f"Deposit in the amount of ${format(deposit, '.2f')} ")
        print(f"Bank account balance ${format(amount, '.2f')} ")
    elif selection == 2:
        withdraw = float(input("How much will you withdraw?"))
        if amount >= withdraw + withdrawalAmount:
            amount -= withdraw + withdrawalAmount
            print(f"\nWithdraw in the amount of ${format(amount, '.2f')}")
            print(f"Bank account balance ${format(amount, '.2f')}")
        else:
            print("\nUnsuccessful!!!\nUnable to withdraw", withdraw,
                  "\nInsufficient funds\nYou haveto cater for transaction charges too\nYour balance is", amount)
    elif selection == 3:
        phoneNumber = int(input("Enter receivers number"))
        sendMoney = int(input("Enter amount to send"))
        print(f"\nsend money in the amount of ${format(sendMoney, '.2f')}")
        if phoneNumber == 10 and amount >= sendMoney + sendingCharges:
            amount -= sendMoney + sendingCharges
            print(f"\nYour Balance is ${format(amount, '.2f')}")
        elif amount < sendMoney + sendingCharges:
            print(f"insufficient balance\nYour balance is ${format(amount, '.2f')}")
        #else:
           #print("invalid number.......try again")
    else:
        loggedOn = False
        print("\nTransaction id :", random.randint(10000, 1000000))
        print("Thanks for choosing our bank see u soon")







