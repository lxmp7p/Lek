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
            requestId = models.DocRequestListMki.objects.get(id=idRequest)
            requestId.status = 'True'
            requestId.save()
            return redirect('../../listRequests/')
        if (move == 'DELETE'):
            descriptionDelete = request.POST.get("descrtiptionDelete")
            usernameDelete = models.DocRequestListMki.objects.get(id=idRequest)
            usernameDeleteMail = userListModel.registeredUsers.objects.get(username=usernameDelete.owner)
            mail = usernameDeleteMail.email
            send_mail('Отказ в проведение исследования', 'Причина отказа: ' + descriptionDelete, 'timurgorashenko@yandex.ru',
                      [mail], fail_silently=False)
            models.DocRequestListMki.objects.filter(id=idRequest).delete()
        return redirect('../../listRequests/')
    else:
        form = forms.DocRequestListMkiForm()
        infoRequest = models.DocRequestListMki.objects.filter(id=idRequest)
        files = ( 'list_members',
                  'accept_research',
                  'protocol_research',
                  'form_inf',
                  'cast_researcher',
                  'contract',
                  'advertising',
                  'write_objects',
                  'another_doc',)
        content = {
                'form': form,
                'username': request.user.username,
                'role_id': request.user.role_id,
                'fio': request.user.fio,
                'infoRequest': infoRequest,
                'idRequest': infoRequest,
                'files': files,
                }
        return render(request, 'infoRequest/infoRequest.html', content)