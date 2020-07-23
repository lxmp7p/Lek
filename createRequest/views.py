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
# Create your views here.

def create_request_mki(request):
    ArticleFormSet = formset_factory(DocRequestListMkiForm)
    formset = ArticleFormSet()
    print(formset)
    if request.method == 'POST':
        form = DocRequestListMkiForm(request.POST, request.FILES)
        print("Второй запрос", form)
        main_res_usr = request.POST.get('_menu', '')
        print(form.media)
        if form.is_valid():
            form.cleaned_data['owner'] = 'test'
            personal = form.save(commit=False)
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
    return render(request, 'createRequest/createRequestPageMki.html', {
        'form': form,
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
        'main_resercher_list': main_resercher_list,
    })

def create_request(request):
    return render(request, 'createRequest/selectRequestType.html', {
        'username': request.user.username,
        'role_id': request.user.role_id,
        'fio': request.user.fio,
    })