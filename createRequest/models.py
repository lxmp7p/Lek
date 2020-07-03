from django.db import models

# Create your models here.
class DocRequestList(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=20, blank=True)
    owner_fio = models.CharField(max_length=20, blank=True)