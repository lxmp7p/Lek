from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import csrf
from .forms import RegisterForm

from .models import  listRegisterRequest

def registration_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            listRegisterRequest.objects.create(**form.cleaned_data)
            return redirect("/")
    else:
        form = RegisterForm()
    return render(request, 'registration/registration_page.html', {'form': form})
