from django import forms
from .models import DocRequestListMki
from django.shortcuts import render, redirect
from django.contrib import auth
from django.http import HttpResponse, request

class DocRequestListMkiForm(forms.ModelForm):
    class Meta:
        model = DocRequestListMki
        fields = ('description', 'document', 'owner', 'status',
                  'description','document',
                  'owner','owner_fio','status','main_researcher',
                  'list_members','ver_bio','accept_research',
                  'accept_research_version','accept_research_date',
                  'protocol_research','protocol_research_version',
                  'protocol_research_date','form_inf','form_inf_version',
                  'form_inf_date','cast_researcher','cast_researcher_version',
                  'cast_researcher_date','advertising','write_objects',
                  'name_another_doc','another_doc','another_doc_version',
                  'another_doc_date', 'contract', 'contract_date',
                  )

