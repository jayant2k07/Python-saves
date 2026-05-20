from utils import transaction
def check_transaction():
    print("\nTransaction History:")
    
    if not transaction:
        print("No transactions yet")
    else:
        for t in transaction:
            print(t)