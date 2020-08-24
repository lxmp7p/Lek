from django.urls import path
from .views import *

urlpatterns = [
    path('', get_profile, name="personalProfile"),
    path('main_cab/', get_main_cab, name='main_cab'),
    path('historyRequests/', get_history_requests, name='historyRequests'),
    path('watch_requests/', watch_requests, name='watchRequests'),
]