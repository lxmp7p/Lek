from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from django.template.context_processors import csrf
import hashlib
from django.contrib.auth import authenticate
from .forms import userInfo
from listForRegistration import models as registrationModels
from createRequest import models as listRequestModels

def get_main_cab(request):
    docRequestListConst = listRequestModels.listRequestResearch.objects.filter(owner=request.user.username)
    content = {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'listRequest': docRequestListConst,
    }
    return render(request, 'profile/main_cab.html', content)

def get_history_requests(request):
    docRequestListConst = listRequestModels.listRequestResearch.objects.filter()
    content = {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'listRequest': docRequestListConst,
    }
    return render(request, 'profile/all_requests.html', content)

def get_profile(request):
    person = registrationModels.registeredUsers.objects.get(username=request.user.username)
    print(person)
    if request.method == 'POST':
        form = userInfo (request.POST)
        if form.is_valid():
            person.dateb = request.POST.get("dateb")
            person.dolzhnost = request.POST.get("dolzhnost")
            person.place_work = request.POST.get("place_work")
            person.password = request.POST.get("password")
            person.set_password(person.password)
            person.is_active = 'True'
            print(request.POST.get("password"))
            person.save()
            #registrationModels.listRegisterRequest.objects.create(**form.cleaned_data)
            return redirect("/")
    form = userInfo()
    content = {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'form': form,
    }
    return render(request, 'profile/profilePage.html', content )