from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
# Create your views here.
from .models import DocRequestList as File
from django.template.context_processors import csrf
import hashlib
import listForRegistration
from django.contrib.auth import authenticate
from .forms import DocRequestListForm
from django.forms.formsets import formset_factory
# Create your views here.

def create_request(request):
    ArticleFormSet = formset_factory(DocRequestListForm)
    formset = ArticleFormSet()
    for form in formset:
        print(form.as_table())
    if request.method == 'POST':
        form = DocRequestListForm(request.POST, request.FILES)
        print("Форма:",form.is_valid())
        if form.is_valid():
            form.cleaned_data['owner'] = 'test'
            print(form.cleaned_data)
            personal = form.save(commit=False)
            personal.owner = request.user.username
            personal.owner_fio = request.user.fio
            personal.save()
            return redirect('../../createRequest/')
    else:
        form = DocRequestListForm()
    return render(request, 'createRequest/createRequestPage.html', {
        'form': form,
        'username': request.user.username,
        'fio': request.user.fio,
    })
    print(request.user.username)