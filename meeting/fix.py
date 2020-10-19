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

logger = logging.getLogger(__name__)

def get_info_reguest(request, idRequest):
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
        return render(request, 'meeting/objectWatch.html', content)