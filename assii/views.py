from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from .models import stu
import time
a=[]
# Create your views here.
def index(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def log(request):
    if request.method=='POST':
        username=request.POST['username']
        passw=request.POST['pass']
        x=auth.authenticate(username=username,password=passw)
        if x is None:
            return HttpResponse('404 not found')
    return render(request, 'log.html')
def home(request):
    try:
     if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        emai = request.POST['emai']
        passs = request.POST['pass']
        age = request.POST['age']
        uid = request.POST['uid']
        image = request.FILES['image']
        if(len(uid)==0):
         t = time.localtime()
         current_time = time.strftime("%M%S", t)
         a=uid
         uii=str(a[:2])
         d = uii + str(current_time)
        else:
            d=uid
        myuser=User.objects.create_user(d,emai,passs)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
     st = stu(s_userid=d, s_age=age, image=image)
     st.save()
     return render(request, 'home.html')
    except Exception as e:
        return HttpResponse('Unique Id already used')
