# Generated by Django 3.0.7 on 2020-06-27 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_auto_20200627_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='listregisterrequest',
            name='first_name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
