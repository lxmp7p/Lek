from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from listForRegistration.models import registeredUsers as User
from django.template.context_processors import csrf
import hashlib
import listForRegistration
from django.contrib.auth import authenticate
import string
import random
from django.core.mail import send_mail
from listForRegistration import models as registrationModels

def random_code():
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = random.randint(8, 12)
    return ''.join(random.choice(chars) for x in range(size))

def login_page(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('two_factor')
        else:
            return render(request, 'login/login_page.html')
    else:
        return render(request, 'login/login_page.html')

def two_factor(request):
    person = registrationModels.registeredUsers.objects.get(username=request.user.username)
    print(request)
    true_code = person.auth_code
    username = person.username
    password = person.password
    email = person.email
    if request.POST:
        code = request.POST.get('_two_factor_code', '')
        if (code == true_code):
            if (person.is_active=='True'):
                return redirect('main')
            else:
                print("fewfwefwefwefewfew")
                content = {
                    'username': request.user.username,
                    'fio': request.user.fio,
                }
                return redirect('../profile/')
        else:
            return render(request, 'login/two_factor.html')
    else:
        person = registrationModels.registeredUsers.objects.get(username=request.user.username)
        rand_code = random_code()
        person.auth_code = rand_code
        person.save()
        send_mail('Auth', 'Code: ' + rand_code, 'timurgorashenko@yandex.ru',
                  [email], fail_silently=False)
        return render(request, 'login/two_factor.html')

def main_page(request):
    content = {
        'username': request.user.username,
        'fio': request.user.fio,
        'role_id': request.user.role_id,
    }
    return render(request, 'login/main.html', context=content)