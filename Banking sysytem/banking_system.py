# Project= Banking System
# Author= Princy Sharma
# Date=24 August 2026

correctPIN = "1245"
attempt = 0

while attempt < 3:
    user_pin = input("Enter your PIN: ")

    if correctPIN == user_pin:
        print("CORRECT PIN")
        break
    else:
        print("Try again")
        attempt += 1

if attempt == 3:
    print("Too many incorrect attempts. Account blocked.")
else:
    account_balance = 150000

    while True:
        print("\nPress 1 to see your account balance")
        print("Press 2 to deposit money")
        print("Press 3 to withdraw money")
        print("Press 4 to exit")

        user_choice = int(input("Enter your choice: "))

        if user_choice == 1:
            print("Your balance is:", account_balance)

        elif user_choice == 2:
            deposit = int(input("Enter amount to deposit: "))
            account_balance += deposit
            print("Amount deposited successfully!")
            print("Your new balance is:", account_balance)

        elif user_choice == 3:
            withdraw = int(input("Enter amount to withdraw: "))

            if withdraw <= account_balance:
                account_balance -= withdraw
                print("Withdrawal successful!")
                print("Your new balance is:", account_balance)
            else:
                print("Insufficient balance!")

        elif user_choice == 4:
            print("Thanks for visiting!")
            break

        else:
            print("Invalid choice!")