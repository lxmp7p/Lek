from django import forms
from .models import listRegisterRequest
import datetime

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, label="Логин")
    mail = forms.EmailField(label="Почта")
    fio = forms.CharField(max_length=30, label="ФИО")
    dateb = forms.CharField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
