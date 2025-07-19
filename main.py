from operations import rent,returning
from read import read_land
from write import rent_write,returning_write,rent_bill,renturning_bill,available_items
from unique_bill import unique_num
d = read_land()
main_loop = True
while main_loop == True:
    available_items(d)#this function is called to display info of land
    print("1. rent")
    print("2. return")
    print("3. exit")
    try:
        user_input = int(input("Enter your choice:"))#user input
        
        if user_input==1:
            bills1 = rent(d)#calling rent function and store returned value to bills1
            rent_write(bills1,unique_num())
            rent_bill(bills1)
        elif user_input == 2:
            bills2 = returning(d)#calling return function and store returned value to bills1
            returning_write(bills2,unique_num())
            renturning_bill(bills2)
        elif user_input == 3:
            print("Thank you using our system!!")
            main_loop = False #setting main loop to false
        else:
            print("Your input is invalid !!")

    except Exception as e:
          print("invalid input",e)
