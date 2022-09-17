from django.shortcuts import *
from django.http import *
import time
import requests
import json
from datetime import date

# from app.models import User
from django.contrib.auth.models import User


def index(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        username = request.POST.get('UserName')
        p1 = request.POST.get('p1')
        p2 = request.POST.get('p2')

        myuser = User.objects.create_user(username=username, email=email, password=p1)
        myuser.first_name=name
        myuser.last_name=""
        myuser.save()
        subject="WELCOME !!!"
        message="Wellcome to this email webapp project created by @shreyas, here you can send and receive text emails to other users. This is a system generated Email."
        today=date.today()
        responce = requests.post('https://shreyas001.herokuapp.com/api/emaildb/', data={
                             'sender': "SYSTEM", 'receiver': username, 'subject': subject, 'message': message, 'date': today})
        # message.success("Account Created Successfully")
        return redirect('/')
        # if(p1==p2):
        #     user=User(name=name, user_name=username, email=email, password=p1)
        #     user.save()
        #     return redirect('/email/login')
    else:
        return render(request, 'index.html')
