import datetime
import random

def main():
    x="The Hotel"
    print("Welcome to ",x,"!")
    print("1.Check In")
    print("2.Eat")
    print("3.Check Out")
    option=int(input())
    while option:
        if option>=1 and option<=3:
            if option==1:
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
                    room_cost=0
                if room_type==1:
                    room_cost=65
                elif room_type==2:
                    room_cost=105
                else:
                    room_Cost=35
                print("The cost of 7 days is: ",room_cost*7,"\n")
                print("Thank you!Enjoy your stay!")
                check_in=datetime.date()
                check_out=check_in+timedelta(days=7)
                c_id=random.randint(101,200)
                print("Your Customer ID is: ",c_id)
            elif option==2:
                price+=food()
            else:
                print("You have ",check_out-check_in,"days to check out.Are you sure you want to check out?Y/N.")
                to_check_out=input()
                if to_check_out=="Y":
                    check_out=datetime.date()
                    room_cost*=(check_out-check_in+1)
                    print("The room cost is:",price)
                    print("The food bill is:", food_bill)
                    print("Thank you for choosing ,",x,"!")
                    exit()
        
    
   
def entrees_menu():
    print("1.Chicken Alfredo : $20")
    print("2.Cuban Chicken Sandwich : $18")
    print("3.Chicken Nuggets with Fries : $19")
    print("4.Beef Burger : $24")
    print("5.Lasagna : $20")
    print("6.Chicken Wrap : $22")
    print("7.Steak : $35")
    print("8.Caesar Salad : $17")
    print("9.Mozzarella Sticks : $18")
    print("10.Hotel Special : $25")

def drinks_menu():
    print("11.Cold Drinks : $1.50")
    print("12.Orange Juice : $2")
    print("13.Mixed Fruit Juice : $2.5")
    print("14.Water Bottle : $1")
    print("15.Coffee : $2")
    print("16.Hot Chocolate : $2.5")
    print("17.Tea : $2.7")
    

def food():
    print("Welcome to ",x,"'s Restaurant!What would you like?")
    entrees_menu()
    drinks_menu()
    food_cost={1:20,2:18,3:19,4:24,5:20,6:22,7:35,8:17,9:18,10:25,11:1.5,12:2,13:2.5,14:1,15:2,16:2.5,17:2.7}
    to_order=input("Are you ready to order?Y/N")
    food_bill=0
    while to_order=="Y":
        see_menu=input("Would you like to see the menus again?Y/N")
        if see_menu=="Y":
            entrees_menu()
            drinks_menu()
        else:
            menu_number=int(input("Enter the item number:"))
            if menu_number not in food_cost:
                print("Invalid Number")
            else:
                food_bill+=food_cost[menu_number]
                price+=food_cost[menu_number]
     to_order=input("Would you like to keep ordering?Y/N")
     print("Your food bill is: $",food_bill)
     return food_bill
        
                    
                          
    
        
    
    
    


    
