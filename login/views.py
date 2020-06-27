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


def login_page(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password, )
        if user is not None:
            auth.login(request, user)
            return redirect('listForRegistration/')
        else:
            return render(request, 'login/login_page.html')
    else:
        return render(request, 'login/login_page.html')