# Generated by Django 2.0.2 on 2018-04-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180421_0153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='favourite_snack',
            field=models.CharField(max_length=255, verbose_name='Interests'),
        ),
    ]