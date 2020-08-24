from django import forms
from .models import listRegisterRequest
from datetime import datetime

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="Логин")
    mail = forms.EmailField(label="Почта")
    fio = forms.CharField(max_length=30, label="ФИО")
    num = forms.CharField(max_length=30, label="Номер телефона")
    #dateb = forms.CharField(label="", widget=forms.DateInput(attrs={'type': 'date'}))
