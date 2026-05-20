from utils import *
def withdraw_money():
    current_balance=get_balance()
    
    w=int(input("enter the amount you want to withdraw:"))
    if w>current_balance:
        print("insufficient balance")
    else:
        current_balance-=w
        set_balance(current_balance)
        transaction.append(f"Withdrawn: {w}")
        print("withdraw is done successfully")
        print("balance left:",current_balance)
