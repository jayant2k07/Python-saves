from utils import *
from display import display_balance
from withdraw import withdraw_money
from deposit import deposit_money
from statement import check_transaction
from auth import verify_pin

def display():
    print("-"*50)
    print("MENU")
    print("-"*50)
    
    print("1.check balance")
    print("2.deposit")
    print("3.withdraw")
    print("4.check transactions")
    print("5.exit")
    print("*"*50)

    while True:
        
        choice=int(input("enter your choice:"))

        if choice==1:
            display_balance()
        elif choice==2:
            deposit_money()
        elif choice==3:
            withdraw_money()
        elif choice==4:
            check_transaction()
        elif choice==5:
            print("Thank You")
            break
        else:
            print("invalid choice")
            break

if verify_pin():
    display()    

