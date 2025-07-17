import datetime
import random

def main():
    x="The Hotel"
    print("Welcome to ",x,"!")
    res=input("Do you have a reservation?Y/N")
    res="N"
    n=int(input("How many people?"))
    print("Would you like a:\n")
    print("1.Standard")
    print("2.Deluxe")
    print("3.Suite")
    room_type=int(input())
    price=0
    while not room_type.isdigit():
        print("Try again.\n")
        print("Would you like a:\n")
        print("1.Standard")
        print("2.Deluxe")
        print("3.Suite")
        room_type=int(input())
    if root_type==1:
        price+=65
    elif room_type==2:
        price+=105
    else:
        price+=35
    print("The cost of 7 days is: ",price,"\n")
    print("Thank you!Enjoy your stay!")
    check_in=datetime.date()
    check_out=check_in+timedelta(days=7)
    c_id=random.randint(101,200)
    print("Your Customer ID is: ",c_id)
    to_eat=input("Would you like to eat something?Y/N")
    if to_eat=="Y":
        price+=food()

def entrees_menu():
    print("1.Chicken Alfredo : $20")
    print("2.Cuban Chicken Sandwich : $18")
    print("3.Chicken Nuggets with Fries : $19")
    print("4.Beef Burger : $24")
    print("5.Lasagna : $20")
    print("6.Chicken Wrap : $22")
    print("7.Chicken Alfredo : $20")
    print("8.Chicken Alfredo : $20")
    print("9.Chicken Alfredo : $20")
    print("10.Chicken Alfredo : $20")
    

def food():
    print("Welcome to ",x,"'s Restaurant!What would you like?")
    
    
    


    
