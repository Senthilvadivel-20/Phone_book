import os

# print(os.getcwd())


import pandas as pd

df=pd.read_csv('.\CSV\Dial_Database.csv')

print(df.columns)



'''
from datetime import date
import pandas as pd
holiday=pd.read_excel('.\CSV\gov_holidays.xlsx')

def day():
    day=date.today().isoweekday()
    if day==1:
        day='Monday'
    elif day==2:
        day='Tuesday'
    elif day==3:
        day='Wednesday'
    elif day==4:
        day='Thursday'
    elif day==5:
        day='Friday'
    elif day==6:
        day='Saturday'
    elif day==7:
        day='sunday'
    return day

day=day()

holiday_list=[]
for i in range(len(holiday)):
    holiday_list.append(holiday['DATE'].iloc[i].date())

def check_holiday():
    if day=='Sunday':
        status='Yes'
    elif date.today() in holiday_list:
        status='Yes'
    else:
        status='NO'
    return status

print(check_holiday())

'''