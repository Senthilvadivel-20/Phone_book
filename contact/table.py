import pandas as pd


df=pd.read_excel('.\CSV\Saved.xlsx')


def contact_table():
    lis=[]
    ln=len(df)
    for i in range(ln):
        temp={
            'name':df['Name'][i],
            'nick_name':df['Nick_name'][i],
            'phone_number':df['Phone_number'][i],
            'gender':df['Gender'][i],
            'dob':df['DOB'][i],
            'designation':df['Designation'][i],
            'relation':df['Relation'][i]
        }
        lis.append(temp)


    return lis


