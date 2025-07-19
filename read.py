

def read_land():
    try:
        '''this function is created to read data present in land.txt file.it doesnot take any parameter and returs dictionary with the land info'''
        land = {}
        file = open("land.txt","r")
        lines = file.readlines()
        file.close()
        for line in lines:
            dic_list= line.replace("\n","").split(",")#converting each line info in a dictionary
            keys = dic_list[0]#storing kitta no in keys
            values = []
            for i in range(1,len(dic_list)):
                values.append(dic_list[i])

            land[keys] = values

        return land
    except:
        print("Error occured")
        
