from django.shortcuts import render
from listForRegistration import models
from createRequest import models as requestListMkiModels


# Create your views here.
def create_meeting(request):
    userList = models.registeredUsers.objects.all()
    requestListMki = requestListMkiModels.DocRequestListMki.objects.filter(status='True')
    content = {
        'username': request.user.username,
        'fio': request.user.fio,
        'role_id': request.user.role_id,
        'userList': userList,
        'requestListMki': requestListMki,
    }
    return render(request, 'meeting/createMeeting.html', context=content)