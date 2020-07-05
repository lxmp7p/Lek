from django.shortcuts import render
from django.http import HttpResponse, response, request
# Create your views here.
from createRequest import models
from createRequest import forms
import re
from django.shortcuts import redirect

def get_info_reguest(request, idRequest):
    if request.method == 'POST':
        i_accept = re.findall(r'ACCEPT', str(request.body))  # Получение id записи через регулярку
        i_delete = re.findall(r'DELETE', str(request.body))  # Получение id записи через регулярку
        move = None
        if (i_accept):
            for i in i_accept:
                move = i
        else:
            for i in i_delete:
                move = i
        if (move == 'ACCEPT'):
            pass
        if (move == 'DELETE'):
            models.DocRequestList.objects.filter(id=idRequest).delete()
        print(request.body, move)
        return redirect('../../listRequests/')
    else:
        form = forms.DocRequestListForm()
        infoRequest = models.DocRequestList.objects.filter(id=idRequest)
        content = {
                'form': form,
                'username': request.user.username,
                'role_id': request.user.role_id,
                'fio': request.user.fio,
                'infoRequest': infoRequest,
                'idRequest': infoRequest,
                }
        return render(request, 'infoRequest/infoRequest.html', content)