# Generated by Django 3.0.7 on 2020-06-29 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_listregisterrequest_first_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listregisterrequest',
            name='role',
        ),
    ]
