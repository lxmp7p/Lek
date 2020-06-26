from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import re
import random
from .models import registeredUsers
from registration import models
from .forms import RegisterForm

def random_password():
    length = 8
    passwd = list('1234567890abcdABCD!@#$%^&*()-=_?')
    random.shuffle(passwd)
    passwd = ''.join([random.choice(passwd) for x in range(length)])
    return passwd

def listForRegistrationPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
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
                    req.append(random_password())
                    registeredUsers.objects.create(username=req[1], #Добавляем пользователя в бд
                                                   mail=req[2],
                                                   fio=req[3],
                                                   dateb=req[4],
                                                   password=req[5],
                                                   role=role,
                                                   )
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку

        elif action=="DELETE":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object:
                    models.listRegisterRequest.objects.filter(id=i[0]).delete() #Удаляем заявку
    else:
        form = RegisterForm()
    listRequest = models.listRegisterRequest.objects.all()
    return render(request, 'listForRegistration/listForRegistrationPage.html', {'username': request.user.username, 'listRequest': listRequest})


