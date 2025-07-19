import datetime

def unique_num():
    '''this function is created to generate unigue number'''
    year = str(datetime.datetime.now().year)#year is accesed
    month = str(datetime.datetime.now().month)
    day = str(datetime.datetime.now().day)
    hour = year = str(datetime.datetime.now().hour)
    minute = str(datetime.datetime.now().minute)
    second = year = str(datetime.datetime.now().second)

    unique = year+month+day+hour+minute+second#unique number
    
    return unique
