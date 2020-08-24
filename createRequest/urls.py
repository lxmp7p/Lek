from django.urls import path
from .views import *

urlpatterns = [
    path('', create_request, name='createRequest'),
    path('createRequestMki/', first_create_request_mki, name='firstCreateRequestMki'),
    path('listMki/', get_list_mki, name='listMki'),
]