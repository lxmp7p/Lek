from django.db import models

# Create your models here.
class listRegisterRequest(models.Model):
    username = models.CharField(max_length=20)
    mail = models.EmailField()
    fio = models.CharField(max_length=30)
    dateb = models.CharField(max_length=12)


