from django.urls import path
from .views import *

urlpatterns = [
    path('', get_profile, name="personalProfile"),
    path('main_cab/', get_main_cab, name='main_cab')
]