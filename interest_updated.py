"""
Description: learning loops and logic in python
Author: Tanvir Singh Bhullar
Date: 02/10/2023
Usage: just learning new stuff
"""

import pprint
# Define an empty dictionary to store account balances
account_balances = {}

# Open and process the input file
with open('account_balances.txt', 'r') as file:
    for line in file:
        account_number, balance = line.strip().split('|')
        account_balances[account_number] = float(balance)

        # Display the account balances
pprint.pprint(account_balances)
for account_number, balance in account_balances.items():
    if balance > 0:
        if balance < 1000:
            interest_rate = 0.01  # 1%
        elif 1000 <= balance < 5000:
            interest_rate = 0.025  # 2.5%
        else:
            interest_rate = 0.05  # 5%
        new_balance = balance + ((balance * interest_rate) / 12)
    else:
        interest_rate = 0.1  # 10%
        new_balance = balance + ((balance * interest_rate) / 12)
    account_balances[account_number] = new_balance

    # Display updated balances
pprint.pprint(account_balances)
import csv
from datetime import datetime
# Define the filename
current_date = datetime.now().strftime("%Y-%m-%d")
initials = "TSB"  # Replace with your initials
filename = f"{current_date}-{initials}.csv"
# Open and write to the CSV file
with open(filename, 'w', newline='') as csv_file:
    fieldnames = ["Account", "Balance"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for account_number, balance in account_balances.items():
        writer.writerow({"Account": account_number, "Balance": balance})
# Verify data in the CSV file
# Check for blank rows manually

# Open and read the CSV file
with open(filename, 'r') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row)

# Verify the correct (updated) data displays

    





































