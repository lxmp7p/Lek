from django.db import models

# Create your models here.
class listRegisterRequest(models.Model):
    username = models.CharField(max_length=20)
    mail = models.EmailField()
    fio = models.CharField(max_length=30)
    dateb = models.CharField(max_length=12)
    is_superuser = models.CharField(max_length=2)
    last_login = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)


