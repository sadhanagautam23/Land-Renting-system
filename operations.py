from datetime import datetime

def rent(land):
    '''this function is created to trent the land. it takes land
       items and returns bill items'''
    l= list(land.keys())
    bills1 = []
    loop = True
    try:
        name = input("Enter your name")
        phone_num = input("Enter your phone number")
        while loop:
            land_id = input("Enter your desire land: ")
            '''while loop is created to user input unless the valid land id is given'''
            while land_id not in l or land[land_id][-1].lower() != "available":
                if land_id not in l:
                    print("invalid LandId")
                if d[land_id][-1].lower() != "available":
                    print("This land is not available")
                land_id = input("Enter your desire land:")
            print("Valid Land!!")

            
            duration = int(input("Enter the duration for which you want to rent the land(in months)"))
            dayOfRent = datetime.now()

            land[land_id][-1]= "Not Available"  #updating avalibility status to not available  
            selected = land[land_id]
            amount = int((selected[3]))*duration
            info = [name,phone_num,dayOfRent,land_id,selected[0],selected[1],selected[2],selected[3],duration,amount ]
            
            bills1.append(info)#appending each bill items in a single list
            ask = True
            while ask == True:
                more_rent= input("Do you want to rent more land??(y/n)")
                if more_rent.lower()=="y":
                    loop = True
                    ask = False
                elif more_rent.lower() == "n":
                    loop = False
                    ask = False
                else:
                        print("Invalid input!")
        file = open("land.txt","w")
        '''updating values to file after renting'''
        for key,value in land.items():
            file.write(key+","+value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4])
            file.write("\n")
        file.close()
        
    except:
             print("Invalid input!")
         
    
    return bills1

    
def returning(land):
    '''this function is created to return the rented land. it takes land
       items and returns bill items'''    
    l= list(land.keys())#accesing kitta no and storing them as 
    bills2 = []
    fine = 0
    loop = True
    try:
        name = input("Enter your name")
        phone_num = input("Enter your phone number")
        
        while loop == True:
            land_id = input("Enter your desire land: ")
            '''while loop is created to user input unless the valid land id is given'''
            while land_id not in l or land[land_id][-1].lower() == "available":
                if land_id not in l:
                    print("invalid LandId")
                if d[land_id][-1].lower() == "available":
                    print("This land cannot be returned .It was not rented.")
                    
                land_id = input("Enter your desire land:")
            print("Valid Land!!")
        
            
            selected = land[land_id]
        
            duration = int(input("Enter the duration for which rented the land(in months)"))
            returned = int(input("Enter the months for which you took the land"))
            dayOfReturn = datetime.now()#generating today's date
            
            
            '''charging fine if the rented month excedees''' 
            if returned > duration :
                price = float(selected[3])*duration
                fine = 10/100*((returned- duration)*float(selected[3]))
                amount =  price+fine
            else:
                amount =  float(selected[3])*duration
                
            land[land_id][-1]= "Available"  #updating avalibility status to available   
                                
            info = [name,phone_num,dayOfReturn,land_id,selected[0],selected [1],selected[2],selected[3],duration,fine,amount]
            
            bills2.append(info)#appending each bill items in a single list
            ask = True
            while ask == True:
                more_rent= input("Do you want to rent more land??(y/n)")
                if more_rent.lower()=="y":
                    loop = True
                    ask = False
                elif more_rent.lower() == "n":
                    loop = False
                    ask = False
                else:
                    print("Invalid input!")
        file = open("land.txt","w")
        '''updating values to file after returning'''
        for key,value in land.items():
            file.write(key+","+value[0]+","+value[1]+","+value[2]+","+value[3]+","+value[4])
            file.write("\n")
        file.close()                    
                    
    except:
             print("Invalid input!!")
        
    
    return bills2


