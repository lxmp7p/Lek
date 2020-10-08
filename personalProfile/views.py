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
from meeting import models
import re

def get_main_cab(request):
    docRequestListConst = listRequestModels.listRequestResearch.objects.filter(owner=request.user.username)
    userlistMeetings = models.listMeetings.objects.all()
    meetings_invited = []
    for object in userlistMeetings:
        if request.user.username in object.users_invited:
            meetings_invited.append(object)
            print(object.accepted_meetings_description)

           # print(re.sub("\D", "", i))
    content = {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'listRequest': docRequestListConst,
        'meetingInvited': meetings_invited,
    }
    return render(request, 'profile/main_cab.html', content)

def watch_requests(request):
    listRequests = listRequestModels.DocRequestListMki.objects.filter(secretar_accept=True)
    return render(request, 'profile/viewRequestPredsetatel.html',
                  {'username': request.user.username, 'fio': request.user.fio, 'role_id': request.user.role_id,
                   'listRequest': listRequests, })



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