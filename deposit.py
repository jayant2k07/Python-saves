from utils import *
def deposit_money():
    current_balance=get_balance()
    
    amount=int(input("enter the amount you want to deposit:"))
    current_balance += amount
    set_balance(current_balance)
    transaction.append(f"Deposited: {amount}")
    print("Amount added successfully.....")
    print("new balance is:",current_balance)

