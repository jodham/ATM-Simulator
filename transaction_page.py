import random

amount = 0.0
loggedOn = True
withdrawalAmount = 23
sendingCharges = 15
separator = '=='

while loggedOn:
    selection = int(input("Select 1 for Deposit, 2 for withdraw ,3 for send money or 4 for Exit"))
    if not selection:
        break
    if selection == 1:
        deposit = float(input("How much will you deposit :"))
        amount += deposit
        print(f"Deposit in the amount of ${format(deposit, '.2f')}")
        print(f"Bank account balance ${format(amount, '.2f')} ")
        print(separator *30)
    elif selection == 2:
        withdraw = float(input("How much will you withdraw? :"))
        if amount >= withdraw + withdrawalAmount:
            amount -= withdraw + withdrawalAmount
            print(f"\nWithdraw in the amount of ${format(amount, '.2f')}\nwithdrawal charges ${format(withdrawalAmount ,'.2f')}")
            print(f"Bank account balance ${format(amount, '.2f')}")
            print(separator *30)
        else:
            print("\nUnsuccessful!!!\nUnable to withdraw", withdraw,
                  "\nInsufficient funds\nYou haveto cater for transaction charges too\nYour balance is", amount)
            print(separator *30)
    elif selection == 3:
        phoneNumber = str(input("Enter receivers number :"))
        sendMoney = int(input("Enter amount to send"))
        if (len(phoneNumber) ==10 ) and (amount >= sendMoney + sendingCharges):
            amount -= sendMoney + sendingCharges
            print(f"\nsend money in the amount of ${format(sendMoney, '.2f')} to", phoneNumber,)
            print(f"\nYour Balance is ${format(amount, '.2f')}\ntransaction cost ${format(sendingCharges, '.2f')}")
            print(separator *30)
        elif len(phoneNumber) != 10:
            print("incorrect phone number")
            print(separator *30)
        else:
            print(f"insufficient balance\nyour balance is ${format(amount, '.2f')}")
            print(separator *30)

    else:
        loggedOn = False
        print("\nTransaction id :", random.randint(10000, 1000000))
        print("Thanks for choosing our bank see u soon")
        print(separator *30)







