from django.urls import path
from .views import *

urlpatterns = [
    path('', create_request, name='createRequest'),
    path('createRequestMki/', create_request_mki, name='createRequestMki'),
]