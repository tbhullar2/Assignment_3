"""
Description: learning loops and logic in python
Author: Tanvir Singh Bhullar
Date: 27/09/2023
Usage: just learning new stuff
"""

list= ["D" , "W" , "Q"]
import random

random_number=random.randint(-1000, 10000)
bank_balance=float(random_number)
print(bank_balance)

print("*", 40)
original_string = "PIXELL RIVER FINANCIAL"
width = 40
centered_string = original_string.center(width)
 
print(centered_string)

original_string = "ATM Simulator"
centered_string = original_string.center(width)
print(centered_string)

original_string = "User bank balance is: $"
centered_string = original_string.center(width)
print( f"User bank balance is: ${bank_balance:,.2f}") 

original_string = "Deposit: D"
centered_string = original_string.center(width)
print(centered_string) 

original_string = "Withdraw: W"
centered_string = original_string.center(width)
print(centered_string) 

original_string = "To Quit: Q"
centered_string = original_string.center(width)
print(centered_string) 

print("**********************************************")
list = ["D" , "W" , "Q"]
user_selection = input ("list:").upper()
deposit_amount = float(input("Enter transaction amount: $"))
bank_balance += deposit_amount
print(f"User bank balance is $){bank_balance:,.2f}".center(width))

import os
from time import sleep
sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')