import pandas as pd
import numpy as np
from datetime import datetime
import warnings 
warnings.filterwarnings('ignore')
import joblib
his=pd.read_excel('.\contact\CSV\dial.xlsx')

j=0
for i in his['Time']:
    i=str(i)
    his['S_Time'].iloc[j]='20/12/2001 '+i
    j+=1

his['S_Time']=pd.to_datetime(his['S_Time'])
his['hour']=his['S_Time'].dt.hour
his['minute']=his['S_Time'].dt.minute

his['DOB']=pd.to_datetime(his['DOB'])

to_day=datetime.today()
today=pd.to_datetime(to_day)

his.insert(2,'Age',0)

for i in range(len(his['DOB'])):
    born=his['DOB'].iloc[i]
    age=today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    his.loc[i,'Age']=age

from sklearn.preprocessing import LabelEncoder

status_encoder=LabelEncoder()

gender_encoder=LabelEncoder()
designation_encoder=LabelEncoder()
relationship_encoder=LabelEncoder()
day_encoder=LabelEncoder()
holiday_encoder=LabelEncoder()

his['Status']=status_encoder.fit_transform(his['Status'])

his['Gender']=gender_encoder.fit_transform(his['Gender'])
his['Designation']=designation_encoder.fit_transform(his['Designation'])
his['Relationship']=relationship_encoder.fit_transform(his['Relationship'])
his['Day']=day_encoder.fit_transform(his['Day'])
his['Holiday']=holiday_encoder.fit_transform(his['Holiday'])

x=his[['Gender','Age', 'Designation', 'Relationship','Day', 'Holiday','hour', 'minute']]
y=his['Status']

from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


from sklearn.tree import DecisionTreeClassifier

# Make a decision tree and train
tree = DecisionTreeClassifier(random_state=42)
tree.fit(x_train,y_train)

joblib.dump(tree,'Dial.sav')

'''
gender=gender_encoder.transform([input("Enter Gender : ")])[0]
age=int(input('Enter your Age :'))
designation=designation_encoder.transform([(input('Enter your designation :'))])[0]
relationship=relationship_encoder.transform([input('Enter Relationship :')])[0]
day=day_encoder.transform([input('Enter day :')])[0]
holiday=holiday_encoder.transform([input('Enter is today Holiday :')])
hour=datetime.now().hour
minute=datetime.now().minute

inp=[gender,age,designation,relationship,day,holiday[0],hour,minute]

print("Predicted Result ",tree.predict([inp])[0])
'''

#print("Accuracy :",tree.score(x_test,y_test)*100)
