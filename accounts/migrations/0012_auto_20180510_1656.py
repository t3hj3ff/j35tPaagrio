# Generated by Django 2.0.2 on 2018-05-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20180428_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='account_bonus',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=255, max_length=255),
        ),
        migrations.AlterField(
            model_name='myprofile',
            name='account_discount',
            field=models.IntegerField(default=0),
        ),
    ]
