from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse

from django.contrib.auth.models import User
# Create your views here.
from .models import DocRequestListMki as File
from django.template.context_processors import csrf
import hashlib
import listForRegistration
from django.contrib.auth import authenticate
from .forms import DocRequestListMkiForm
from django.forms.formsets import formset_factory
from datetime import datetime
from listForRegistration import models as UserList
from .models import listRequestResearch
# Create your views here.


def addAllRequestToList(description,owner,date_created):
    listRequestResearch.objects.create(description=description,
                                       owner=owner,
                                       date_created=date_created,
                                       status='Ожидание решения комиссии')
def first_create_request_mki(request):
    ArticleFormSet = formset_factory(DocRequestListMkiForm)
    formset = ArticleFormSet()
    print(formset)
    if request.method == 'POST':
        form = DocRequestListMkiForm(request.POST, request.FILES)
        main_res_usr = request.POST.get('_menu', '')
        print(form.media)
        if form.is_valid():
            # Убрал это ! form.cleaned_data['owner'] = 'test'
            personal = form.save(commit=False)
            description = 'Сделать получение названия исследования'
            addAllRequestToList(description,
                                request.user.username,
                                datetime.now(),
                                )

            personal.status = 'False'
            personal.secretar_accept = 'False'
            personal.owner = request.user.username
            personal.date_created = datetime.now()
            personal.owner_fio = request.user.fio
            personal.main_researcher = main_res_usr
            personal.save()
            return redirect('../../createRequest/')
        else:
            print("ошибки формы \n", form.errors)
    form = DocRequestListMkiForm()
    main_resercher_list = UserList.registeredUsers.objects.filter(role_id=6)
    print(main_resercher_list)
    return render(request, 'createRequest/Mki/createRequestPageMki.html', {
        'form': form,
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'main_resercher_list': main_resercher_list,
    })

def get_list_mki(request):
    return render(request, 'createRequest/Mki/listMki.html', {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
    })

def create_request(request):
    return render(request, 'createRequest/selectRequestType.html', {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
    })