from django import forms
from .models import DocRequestList
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, request

class DocRequestListForm(forms.ModelForm):
    class Meta:
        model = DocRequestList
        fields = ('description', 'document', 'owner', 'status',
                  'zagolovok','num_zagolovok','date_zagolovok',
                  'podpis','num_podpis','date_podpis',
                  'test','num_test','date_test',
                  )