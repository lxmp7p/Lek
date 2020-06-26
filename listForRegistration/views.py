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
        id_re = re.findall(r'id=(..&*)', str(request.body)) #Получение id записи через регулярку
        action_re = re.findall(r'ACCEPT|DELETE', str(request.body)) #Получение имени нажатой кнопки через регулярку
        object = 0
        action = ''
        for i in id_re:
            object = i
        for i in action_re:
            action = i
        object = int(object[0:-1])
        req = ''
        # В object хранится значение id нажатой кнопки типа int
        # В action хранится значение нажатой кнопки типа str (ACCEPT/DELETE)
        if action=="ACCEPT":
            for i in models.listRegisterRequest.objects.values_list(): # Пробегаем по таблице с заявками
                if i[0] == object:
                    req = list(i)
                    req.append(random_password())
                    registeredUsers.objects.create(username=req[1], #Добавляем пользователя в бд
                                                   mail=req[2],
                                                   fio=req[3],
                                                   dateb=req[4],
                                                   password=req[5],
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


