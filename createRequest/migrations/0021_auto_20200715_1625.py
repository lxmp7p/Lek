# Generated by Django 3.0.7 on 2020-07-15 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('createRequest', '0020_auto_20200715_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='docrequestlistmki',
            name='contract',
            field=models.FileField(blank=True, null=True, upload_to='contract/'),
        ),
        migrations.AddField(
            model_name='docrequestlistmki',
            name='contract_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
