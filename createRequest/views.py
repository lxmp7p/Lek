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
# Create your views here.

def create_request_mki(request):
    ArticleFormSet = formset_factory(DocRequestListMkiForm)
    formset = ArticleFormSet()
    print(formset)
    if request.method == 'POST':
        form = DocRequestListMkiForm(request.POST, request.FILES)
        form.owner = 'test'
        print(form.media)
        if form.is_valid():
            form.cleaned_data['owner'] = 'test'
            personal = form.save(commit=False)
            personal.owner = request.user.username
            personal.owner_fio = request.user.fio
            personal.save()
            return redirect('../../createRequest/')
        else:
            print("ошибки формы \n", form.errors)
    else:
        form = DocRequestListMkiForm()
    return render(request, 'createRequest/createRequestPageMki.html', {
        'form': form,
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