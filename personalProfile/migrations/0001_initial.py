# Generated by Django 3.0.7 on 2020-08-15 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='listRequestResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('owner', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=12)),
                ('date_created', models.CharField(max_length=30)),
            ],
        ),
    ]
