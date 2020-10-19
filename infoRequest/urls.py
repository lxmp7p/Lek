from django.urls import path
from .views import *

urlpatterns = [
    path('', get_info_reguest, name='infoRequest'),
    path('infoRequestFix/', get_info_reguest_fix, name='infoRequestFix'),
]