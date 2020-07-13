from django import forms
from listForRegistration import models
import datetime

class userInfo(forms.Form):
    dateb = forms.CharField(label="Дата рождения", widget=forms.DateInput(attrs={'type': 'date'}))
    dolzhnost = forms.CharField(max_length=30, label="Должность")
    place_work = forms.CharField(max_length=30, label="Место работы")
    password = forms.CharField(max_length=100, label="Новый пароль")
