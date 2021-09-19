from django.shortcuts import render
import joblib
from . import Save_in_DataFrame
# from django.shortcuts import HttpResponse
from contact.sim_details import number
from contact import table

from django.contrib import messages



def home(request):
    return render(request,'home.html')

def save(request):
    return render(request,'save.html')

def done(request):
    c_name=request.GET['name']
    c_nick_name=request.GET['nick_name']
    c_phone_number=request.GET['phone_number']
    c_gender=request.GET['gender']
    c_dob=request.GET['dob']
    c_designation=request.GET['designation']
    c_relation=request.GET['relation']


    Save_in_DataFrame.DataFrame(c_name,c_nick_name,c_phone_number,c_gender,c_dob,c_designation,c_relation)
    
    message=messages.success(request, f"{c_name} Contact Created.....!")

    return render(request,'save.html',locals())

def all(request):
    lis=table.contact_table()
    return render(request,'table.html',locals())

def call(request):
    details,inputs=Save_in_DataFrame.get_details(request.GET['number'])
    if details=='Unknown':
        Message="You're calling to unknown person"
    else:
        #gender,age,designation,relationship,day,holiday,hour,minute
        name,nick_name,phone_number,gender,age,designation,relation,holiday,hour,minute=details
        tree=joblib.load('.\CSV\Dial.pkl')
        land_mark,sim,time_zone=number(str(phone_number))
        ans=tree.predict([inputs])
        answer=Save_in_DataFrame.answer(ans)
        if answer=='Yes':
            Message='This Person may take this call'
        else:
            Message='This Person may not take this call'
    return render(request,'calling.html',locals())


    
    