# Generated by Django 3.0.7 on 2020-07-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createRequest', '0011_auto_20200704_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docrequestlist',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]