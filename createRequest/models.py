from django.db import models

# Create your models here.
class DocRequestList(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/',  blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.CharField(max_length=20, blank=True)
    owner_fio = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=10, blank=True, null=True)

    zagolovok = models.FileField(upload_to='zagolovok/',  blank=True, null=True)
    num_zagolovok = models.CharField(max_length=30, blank=True, null=True)
    date_zagolovok = models.CharField(max_length=30, blank=True, null=True)

    podpis = models.FileField(upload_to='podpis/',max_length=30, blank=True, null=True)
    num_podpis = models.CharField(max_length=30, blank=True, null=True)
    date_podpis = models.CharField(max_length=30, blank=True, null=True)

    test = models.FileField(max_length=30, blank=True, null=True)
    num_test = models.CharField(max_length=30, blank=True, null=True)
    date_test = models.CharField(max_length=30, blank=True, null=True)