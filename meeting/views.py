from django.shortcuts import render, redirect
from createRequest import models as requestListMkiModels
from .forms import meetingCreate
from .models import listMeetings
from listForRegistration import models as listForRegistration
from django.core.mail import send_mail
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, response, request
# Create your views here.
from createRequest import models
from createRequest import forms
import re
from django.shortcuts import redirect
from listForRegistration import models as userListModel
from django.core.mail import send_mail
from createRequest import models as listRequestResearchModels
import logging

import re


now = datetime.now()

# Create your views here.

def get_description(researchs):
    researchs_description = []
    for i in researchs:
        description = requestListMkiModels.DocRequestListMki.objects.get(id=i)
        researchs_description.append(description.description)
    return researchs_description


def send_message_users(userList,researchs):
    researchs_description = get_description(researchs)
    for username in userList:
        user = listForRegistration.registeredUsers.objects.get(username=username)
        send_mail('Добавление в исследование', 'Вы были добавлены в список участников для обсуждения таких тем как: ' + str(researchs_description), 'timurgorashenko@yandex.ru',
                  [user.email], fail_silently=False)

def open_meeting(request):
    meetingAccepted = listMeetings.objects.all()
    tmp = []
    meetingList = None
    #meetingList = None
    for object in meetingAccepted:
        if (request.user.username in object.users_invited):
            if (object.date == now.strftime("%Y-%m-%d")):
                meetingList = object
    '''
    tmp = []
    for object in meetingList:
        tmp.append(object.accepted_meetings)
    meetindTheme = tmp
    print(meetindTheme)
    '''
    tmp = []
    num = ''
    if not meetingList:
        message = "На сегодня не назначено совещаний!"
        context = {'username': request.user.username, 'fio': request.user.fio, 'role_id': request.user.role_id, 'error': message, }
        return render(request, 'meeting/openMeeting.html', context=context)
    meetingName = meetingList.accepted_meetings_description
    for id in meetingList.accepted_meetings:
        if id != ',':
             num += id
        else:
            tmp.append(num)
            num = ''
    meetingIdList = tmp
    tmp = []
    meetings = []
    for id in meetingIdList:
        meetings.append(requestListMkiModels.DocRequestListMki.objects.get(id=id))
    context = {'username': request.user.username, 'fio': request.user.fio, 'role_id': request.user.role_id, 'meetings':meetings}
    return render(request, 'meeting/openMeeting.html', context=context)

def create_meeting(request):
    userList = userListModel.registeredUsers.objects.all()
    requestListMki = requestListMkiModels.DocRequestListMki.objects.filter(status='True')
    form = meetingCreate()
    content = {
        'username': request.user.username,
        'fio': request.user.fio,
        'role_id': request.user.role_id,
        'userList': userList,
        'requestListMki': requestListMki,
        'form': form,
    }
    if request.method == 'POST':
        userToInvitedList = []
        researchAcceptList = []
        researchAcceptListFix = ''
        print(str(request.POST.get("s")))
        userToInvited = re.findall(r'userLists=[a-zA-Z]*', str(request.body))   #Получаем список выбранных юзеров
        for i in userToInvited:
            userToInvitedList.append(i[10:])


        researchForAccept = re.findall(r'reserchs=[\d]*', str(request.body))   #Получаем список выбранных исследований
        for i in researchForAccept:
            researchAcceptList.append(i[9:])
            researchAcceptListFix += str(i[9:]) + ','

        descriptionsList = get_description(researchAcceptList)
        form = meetingCreate(request.POST)
        if form.is_valid():
            date = request.POST.get("date")
            time = request.POST.get("time")
            meeting = listMeetings()
            meeting.time = time
            meeting.date = date
            meeting.accepted_meetings = researchAcceptListFix
            meeting.accepted_meetings_description = descriptionsList
            meeting.users_invited = userToInvitedList
            meeting.save()
            send_message_users(userToInvitedList,researchAcceptList)
            return redirect('main')


        return render(request, 'meeting/createMeeting.html', context=content)
    return render(request, 'meeting/createMeeting.html', context=content)

