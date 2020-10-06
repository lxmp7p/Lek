from django.db import models

# Create your models here.

class listMeetings(models.Model):
    accepted_meetings = models.CharField(max_length=200, blank=False, null=False)
    users_invited = models.CharField(max_length=200, blank=False, null=False)
    date = models.CharField(max_length=30, blank=False, null=False)
    time = models.CharField(max_length=50, blank=False, null=False)