# Generated by Django 3.0.6 on 2020-08-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0007_auto_20200713_1936'),
    ]

    operations = [
        migrations.AddField(
            model_name='listregisterrequest',
            name='date_created',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
