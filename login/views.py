from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
# Create your views here.
from django.template.context_processors import csrf
import hashlib


def login_page(request):
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('listForRegistration/', {'username': username})
        else:
            return render(request, 'login/login_page.html')
    else:
        return render(request, 'login/login_page.html')