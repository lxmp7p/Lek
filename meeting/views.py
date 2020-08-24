from django.shortcuts import render
from listForRegistration import models
from createRequest import models as requestListMkiModels
from .forms import meetingCreate
import re

# Create your views here.
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


        print(researchAcceptList)
        print(userToInvitedList)
        return render(request, 'meeting/createMeeting.html', context=content)
    return render(request, 'meeting/createMeeting.html', context=content)