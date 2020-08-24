"""Lek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.contrib.auth import views
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


from login.views import *
from registration.views import *
from listForRegistration.views import *
from personalProfile.views import *
from infoRequest.views import *

urlpatterns = [
    path('', include('login.urls')),
    path('registration/', include('registration.urls')),
    path('admin/', admin.site.urls),
    path('listForRegistration/', include('listForRegistration.urls')),
    path('createRequest/', include('createRequest.urls')),
    path('listRequests/', include('listRequests.urls')),
    path('logout/', views.LogoutView.as_view(next_page='/'), name='logout'),
    path('profile/', include('personalProfile.urls'), name='profile'),
    path('meeting/', include('meeting.urls'), name='meeting'),
    path('infoRequest/<int:idRequest>/', include("infoRequest.urls")),
    path('profile/watch_requests/<int:idRequest>/', include("infoRequest.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
