from django.urls import path
from .views import *
from .fix import *

urlpatterns = [
    path('', create_meeting, name="createMeeting"),
    path('openMeeting/', open_meeting, name="openMeeting"),
]
