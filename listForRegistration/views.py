from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import re
import random
from .models import registeredUsers
from registration import models
from .forms import RegisterForm
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from listForRegistration.models import registeredUsers as User
from django.template.context_processors import csrf
import hashlib
from django.contrib.auth import authenticate
from datetime import date

def random_password():
    length = 8
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    return passwd

def listForRegistrationPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(r'cccc!!!!!!', request.body)
        action_re = re.findall(r'ACCEPT|DELETE', str(request.body)) #Получение имени нажатой кнопки через регулярку
        role = re.findall(r'kommission|secretar', str(request.body)) #Получение роли через регулярку
        i = re.findall(r'(ACCEPT|DELETE)+(......*=)', str(request.body))  # Получение id записи через регулярку
        object = 0
        print(i)
        for a in i:
            object = a[1]
        object = object[1:-4]
        object = int(object)
        action = ''
        for i in action_re:
            action = i
        for i in role:
            role = i
        print(request.body)
        req = ''
        # В object хранится значение id нажатой кнопки типа int
        # В action хранится значение нажатой кнопки типа str (ACCEPT/DELETE)
        if action=="ACCEPT":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object:
                    req = list(i)
                    print(req)
                    password = random_password()
                    user = User.objects.create_user(username=req[1],
                                                    email=req[2],
                                                    fio=req[3],
                                                    dateb=req[4],
                                                    password=password,
                                                    role=role,
                                                    username_field=req[1],
                                                    is_superuser='None',
                                                    last_login='None',
                                                    first_name='None',
                                                    last_name='None',
                                                    is_staff='False',
                                                    is_active='True',
                                                    date_joined=date.today(),
                                                    )
                    print(password)
                    user.save()
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку

        elif action=="DELETE":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object:
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку
    else:
        form = RegisterForm()
    listRequest = models.listRegisterRequest.objects.all()
    print(request.user.username)
    return render(request, 'listForRegistration/listForRegistrationPage.html', {'username': request.user.username, 'fio': request.user.fio, 'listRequest': listRequest})


