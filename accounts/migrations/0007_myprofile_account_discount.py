# Generated by Django 2.0.2 on 2018-04-20 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20180421_0044'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='account_discount',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=3),
        ),
    ]
