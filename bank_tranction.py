"""
Description: learning loops and logic in python
Author: Tanvir Singh Bhullar
Date: 27/09/2023
Usage: just learning new stuff
"""

import random
import os
from time import sleep

variables={"D", "W", "Q"}

bank_balance=random.randint(-1000, 100000)
user_balance= float(bank_balance)

while True:
    width= 40
    fills="*"

    print(fills * width)
    print("PIXELL RIVER FINSNCIAL".center(width))
    print("ATM SIMULATOR" .center(width))
    print(f"your current balance is: ${user_balance:,.2f}")
    print(f"Deposit: {variables[1]}".center(width))
    print(f"Withdraw: {variables[2]}".center(width))
    print(f"to Quit: {variables[3]}".center(width))
    print(fills * width, "/n")

    option=input("enter your selection:").upper()
    if option=="Q":
        print("Thank you for using this ATM. Have a great day!")
        break
    elif option=="D":
        deposit_amount=float(input("enter amount of transaction: $"))
        if deposit_amount<0:
            print(fills * width)
            print("Please enter a positive amount in it.")
            print(fills * width)
        else:
            user_balance+=deposit_amount
            print(fills * width)
            print(f"Your current balance is:${user_balance:,.2f}".center(width))
            print(fills * width)
    elif option=="W":
       


