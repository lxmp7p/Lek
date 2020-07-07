from django import forms
from listForRegistration import models
import datetime

class userInfo(forms.Form):
    num = forms.CharField(max_length=30, label="Номер телефона")
    dolzhnost = forms.CharField(max_length=30, label="Должность")
    place_work = forms.CharField(max_length=30, label="Место работы")
    password = forms.CharField(max_length=100, label="Новый пароль")
