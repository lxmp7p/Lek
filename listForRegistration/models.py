from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class registeredUsers(AbstractUser):
    username_field= models.CharField(max_length=20)
    is_superuser = models.CharField(max_length=2)
    last_login = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    fio = models.CharField(max_length=30)
    dateb = models.CharField(max_length=12)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_staff = models.CharField(max_length=20)
    is_active = models.CharField(max_length=20)
    date_joined = models.CharField(max_length=20)

class Role(models.Model):
    role = models.CharField(max_length=30, db_index=True, verbose_name='Наименование роли ')






