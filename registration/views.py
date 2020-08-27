from django.shortcuts import render, redirect
from datetime import datetime

# Create your views here.
from django.template.context_processors import csrf
from .forms import RegisterForm

from .models import  listRegisterRequest

now = datetime.now()

def registration_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            listRegisterRequest.objects.create(**form.cleaned_data)
            form = listRegisterRequest(request.POST)
            username = request.POST.get('username', '')
            person = listRegisterRequest.objects.get(username=username)
            person.date_created = now.strftime("%d-%m-%Y %H:%M")
            person.save()
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_page.html', {'form': form, 'datetime': datetime.now()})
