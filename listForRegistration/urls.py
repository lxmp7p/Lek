from django.urls import path
from .views import *

urlpatterns = [
    path('', listForRegistrationPage, name='listForRegistration'),
]