from django.shortcuts import render, redirect
from listForRegistration import models
from createRequest import models as requestListMkiModels
from .forms import meetingCreate
from .models import listMeetings
from listForRegistration import models as listForRegistration
from django.core.mail import send_mail
import re

# Create your views here.

def send_message_users(userList,researchs):
    researchs_description = []
    for i in researchs:
        description = requestListMkiModels.DocRequestListMki.objects.get(id=i)
        researchs_description.append(description.description)

    for username in userList:
        user = listForRegistration.registeredUsers.objects.get(username=username)
        send_mail('Добавление в исследование', 'Вы были добавлены в список участников для обсуждения таких тем как: ' + str(researchs_description), 'timurgorashenko@yandex.ru',
                  [user.email], fail_silently=False)


def create_meeting(request):
    userList = models.registeredUsers.objects.all()
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
        print(str(request.POST.get("s")))
        userToInvited = re.findall(r'userLists=[a-zA-Z]*', str(request.body))   #Получаем список выбранных юзеров
        for i in userToInvited:
            userToInvitedList.append(i[10:])

        researchForAccept = re.findall(r'reserchs=[\d]*', str(request.body))   #Получаем список выбранных исследований
        for i in researchForAccept:
            researchAcceptList.append(i[9:])


        form = meetingCreate(request.POST)
        if form.is_valid():
            date = request.POST.get("date")
            time = request.POST.get("date")
            meeting = listMeetings()
            meeting.time = time
            meeting.date = date
            meeting.accepted_meetings = researchAcceptList
            meeting.users_invited = userToInvitedList
            meeting.save()
            send_message_users(userToInvitedList,researchAcceptList)
            return redirect('main')


        return render(request, 'meeting/createMeeting.html', context=content)
    return render(request, 'meeting/createMeeting.html', context=content)