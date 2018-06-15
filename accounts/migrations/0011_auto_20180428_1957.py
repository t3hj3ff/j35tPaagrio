# Generated by Django 2.0.2 on 2018-04-28 15:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20180426_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
    ]
