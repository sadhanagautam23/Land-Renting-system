

def rent_write(bills1,unique):
    '''This function is created to write bill
       in a unique file.it takes bills1 and unique number contaning bill items as parameter '''
    try:
        filename = unique+"_"+bills1[0][0]+".txt"
        grand_total = 0
        for each in bills1:
            grand_total = grand_total + float(each[-1])
        file = open(filename,"w")
        file.write("\t"+"\t"+"\t"+"\t"+"Techo Property Nepal"+"\n")
        file.write("\t"+"\t"+"\t"+"Sanepa, Lalitpur | Phone no: 97294956"+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Rented Land are:"+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Name of the customer:"+"\t"+bills1[0][0]+"\n")
        file.write("Contact Number:"+"\t"+bills1[0][1]+"\n")
        file.write("Date and time of purchase:"+"\t"+str(bills1[0][2])+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Purchase Detail are:"+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Item ID"+"\t"+"\t"+"City"+"\t"+"\t"+"Direction"+"\t"+"Anna"+"\t"+"Price per month"+"\t"+"\t"+"Month"+"\t"+"Total"+"\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        for value in bills1:
            file.write(str(value[3])+"\t"+"\t"+str(value[4])+"\t"+str(value[5])+"\t"+"\t"+str(value[6])+"\t"+"\t"+"Rs."+str(value[7])+"\t"+"\t"+str(value[8])+"\t"+"Rs."+str(value[9]))
            file.write("\n")
        file.write("------------------------------------------------------------------------------------------------------------------------------"+("\n"))                
        file.write("Grand Total:"+"Rs."+str(grand_total)+"\n")
        file.write("\n")
        file.close()
        
    except:
        print(Error)

def returning_write(bills2,unique):
    '''This function is created to write bill
       in a unique file.It takes bills2 contaning bill and unique number items as parameter '''
    try:
        filename = unique+"_"+bills2[0][0]+".txt"
        grand_total = 0
        for each in bills2:
            grand_total = grand_total + float(each[-1])
        file = open(filename,"w")
        file.write("\t"+"\t"+"\t"+"\t"+"Techo Property Nepal"+"\n")
        file.write("\t"+"\t"+"\t"+"Sanepa, Lalitpur | Phone no: 97294956"+"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Returned Land are:"+"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Name of the customer:"+"\t"+bills2[0][0]+"\n")
        file.write("Contact Number:"+"\t"+bills2[0][1]+"\n")
        file.write("Date and time of return:"+str(bills2[0][2])+"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Purchase Detail are:"+"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        file.write("Item ID"+"\t"+"\t"+"City"+"\t"+"\t"+"Direction"+"\t"+"Anna"+"\t"+"Price per month"+"\t"+"\t"+"Month"+"\t"+"\t"+"fine"+"\t"+"\t"+"Total"+"\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        for value in bills2:
            file.write(str(value[3])+"\t"+"\t"+str(value[4])+"\t"+"\t"+str(value[5])+"\t"+"\t"+str(value[6])+"\t"+"\t"+str(value[7])+"\t"+"\t"+str(value[8])+"\t"+"\t"+"Rs."+str(value[9])+"\t"
                       +"\t"+"Rs."+str(value[10]))
            file.write("\n")
        file.write("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))                
        file.write("Grand Total:"+"Rs."+str(grand_total)+"\n")
        file.write("\n")
        file.close()
    except:
        print(error)

def rent_bill(bills1):
    '''This function is created to print bill
       in the output window.It takes bills1 contaning bill items as parameter '''
    try:
        grand_total = 0
        for each in bills1:
            grand_total = grand_total + float(each[-1])
       
        print("\t"+"\t"+"\t"+"\t"+"Techo Property Nepal"+"\n")
        print("\t"+"\t"+"\t"+"Sanepa, Lalitpur | Phone no: 97294956"+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Rented Land are:"+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Name of the customer:"+"\t"+bills1[0][0]+"\n")
        print("Contact Number:"+"\t"+bills1[0][1]+"\n")
        print("Date and time of purchase:"+"\t"+str(bills1[0][2])+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Purchase Detail are:"+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Item ID"+"\t"+"\t"+"City"+"\t"+"\t"+"Direction"+"\t"+"Anna"+"\t"+"Price per month"+"\t"+"\t"+"Month"+"\t"+"\t"+"Total"+"\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        for value in bills1:
            print(str(value[3])+"\t"+"\t"+str(value[4])+"\t"+str(value[5])+"\t"+"\t"+str(value[6])+"\t"+"\t"+"Rs."+str(value[7])+"\t"
                  +str(value[8])+"\t"+"\t"+"Rs."+str(value[9]))
            print("\n")
        print("------------------------------------------------------------------------------------------------------------------------------"+("\n"))                
        print("Grand Total:"+"Rs."+str(grand_total)+"\n")
        print("\n")
    except:
        print("Error")
      

def renturning_bill(bills2):
    '''This function is created to print bill
       in the output window.It takes bills2 contaning bill items as parameter '''
    try:
        grand_total = 0
        for each in bills2:
            grand_total = grand_total + float(each[-1])
        print("\t"+"\t"+"\t"+"\t"+"Techo Property Nepal"+"\n")
        print("\t"+"\t"+"\t"+"Sanepa, Lalitpur | Phone no: 97294956"+"\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Returned Land are:"+"\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Name of the customer:"+"\t"+bills2[0][0]+"\n")
        print("Contact Number:"+"\t"+bills2[0][1]+"\n")
        print("Date and time of return:"+str(bills2[0][2])+"\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Purchase Detail are:"+"\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        print("Item ID"+"\t"+"\t"+"City"+"\t"+"\t"+"Direction"+"\t"+"Anna"+"\t"+"Price per month"+"\t"+"\t"+"Month"+"\t"+"\t"+"fine"+"\t"+"\t"+"Total"+"\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))
        for value in bills2:
            print(str(value[3])+"\t"+"\t"+str(value[4])+"\t"+"\t"+str(value[5])+"\t"+"\t"+str(value[6])+"\t"+"\t"+str(value[7])+"\t"+"\t"+str(value[8])+"\t"+"Rs."+str(value[9])+"\t"
                       +"\t"+"Rs."+str(value[10]))
            print("\n")
        print("---------------------------------------------------------------------------------------------------------------------------------"+("\n"))                
        print("Grand Total:"+"Rs."+str(grand_total)+"\n")
        print("\n")
    except:
        print("Error")

def available_items(d):
    '''this function is created to print land information in outout screen.it takes d as parameterwhich stores land info'''
    print("Item ID"+"\t"+"\t"+"City"+"\t"+"\t"+"Direction"+"\t"+"Anna"+"\t"+"\t"+"Price per month"+"\t"+"\t"+"Avalilable status"+"\n")
    for key,value in d.items():
        print(key+"\t"+"\t"+value[0]+"\t"+value[1]+"\t"+"\t"+value[2]+"\t"+"\t"+value[3]+"\t"+"\t"+"\t"+value[4])
            
    
