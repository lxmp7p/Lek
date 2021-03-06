# Generated by Django 3.0.7 on 2020-06-27 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listForRegistration', '0002_auto_20200627_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeredusers',
            name='role',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='date_joined',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='first_name',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='is_active',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='is_staff',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='is_superuser',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='last_login',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='registeredusers',
            name='last_name',
            field=models.CharField(max_length=2),
        ),
    ]
