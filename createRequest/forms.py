from django import forms
from .models import DocRequestList
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, request

class DocRequestListForm(forms.ModelForm):
    class Meta:
        model = DocRequestList
        fields = ('description', 'document', 'owner', 'version',)

    date = forms.CharField(label="Дата документа", widget=forms.DateInput(attrs={'type': 'date'}))