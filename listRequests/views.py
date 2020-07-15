from django.shortcuts import render
from django.http import HttpResponse, request
from createRequest import models

# Create your views here.

def getListRequests(request):
    listRequests = models.DocRequestListMki.objects.all()
    return render(request, 'listRequests/listRequestsPage.html', {'username': request.user.username, 'fio': request.user.fio, 'role_id': request.user.role_id, 'listRequest': listRequests, })
