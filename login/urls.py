from django.urls import path
from .views import *

urlpatterns = [
    path('', login_page),
    path('two_factor/', two_factor, name='two_factor'),
    path('main/', main_page, name='main'),
]