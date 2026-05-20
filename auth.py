from utils import pin
def verify_pin():
    attempts=3
    while attempts>0:
        entered_pin=int(input("enter your pin:"))
        if entered_pin==pin:
            print("login successful\n")
            return True
        else:
            attempts-=1
            print(f"Incorrect Pin.....remaining attempts left:{attempts}")
    print("maximum attempts reached!!. Card Blocked")
    return False

    
