import pandas as pd
from datetime import datetime,date
from sklearn.preprocessing import LabelEncoder

df=pd.read_excel('.\CSV\saved.xlsx')
da=df[['Name', 'Nick_name', 'Phone_number', 'Gender', 'DOB','Designation','Relation']]

holiday=pd.read_excel('.\CSV\gov_holidays.xlsx')

data=pd.read_csv('.\CSV\Dial_Database.csv')

status_encoder=LabelEncoder()
gender_encoder=LabelEncoder()
designation_encoder=LabelEncoder()
relationship_encoder=LabelEncoder()
day_encoder=LabelEncoder()
holiday_encoder=LabelEncoder()

data['Status']=status_encoder.fit_transform(data['Status'])
data['Gender']=gender_encoder.fit_transform(data['Gender'])
data['Designation']=designation_encoder.fit_transform(data['Designation'])
data['Relationship']=relationship_encoder.fit_transform(data['Relationship'])
data['Day']=day_encoder.fit_transform(data['Day'])
data['Holiday']=holiday_encoder.fit_transform(data['Holiday'])


def DataFrame(c_name,c_nick_name,c_phone_number,c_gender,c_dob,c_designation,c_relation):
    idx=len(df)

    df.loc[idx,'Name']=str(c_name)
    df.loc[idx,'Nick_name']=str(c_nick_name)
    df.loc[idx,'Phone_number']=c_phone_number
    df.loc[idx,'Gender']=str(c_gender)
    df.loc[idx,'DOB']=c_dob
    df.loc[idx,'Designation']=c_designation
    df.loc[idx,'Relation']=str(c_relation)

    da=df[['Name', 'Nick_name', 'Phone_number', 'Gender', 'DOB','Designation','Relation']]
        
    da.to_excel('.\CSV\saved.xlsx')

def all_contact():
    return da

def dob(born):
    born=datetime.fromisoformat(born)
    today=datetime.today()
    age=today.year-born.year-((today.month,today.day)>(born.month,born.day))   #born.month,born.today))
    return age

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
        day='Sunday'
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
        status='No'
    return status


def get_details(inputt):
    try:
        idx=da[da['Name']==inputt].index.values[0]
        statement=True
    except IndexError:
        statement=False
    if statement:
        name=da.loc[idx,'Name']
        nick_name=da.loc[idx,'Nick_name']
        phone_number=da.loc[idx,'Phone_number']
        gender=da.loc[idx,'Gender']
        age=dob(da.loc[idx,'DOB'])
        designation=da.loc[idx,'Designation']
        relation=da.loc[idx,'Relation']
        week_day=day
        holiday=check_holiday()
        hour=datetime.now().hour
        minute=datetime.now().minute
        inp1=gender_encoder.transform([gender])[0]
        inp2=age
        inp3=designation_encoder.transform([designation])[0]
        inp4=relationship_encoder.transform([relation])[0]
        inp5=day_encoder.transform([week_day])[0]
        inp6=holiday_encoder.transform([holiday])[0]
        inp7=hour
        inp8=minute
        inputs=[inp1,inp2,inp3,inp4,inp5,inp6,inp7,inp8]
        details=(name,nick_name,phone_number,gender,age,designation,relation,holiday,hour,minute)


        #name,nick_name,phone_number,gender,age,relation
    else:
         details='Unknown'
         inputs=None
    return details,inputs

def answer(ans):
    answer=status_encoder.inverse_transform([ans])[0]
    return answer
    

