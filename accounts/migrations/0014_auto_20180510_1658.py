# Generated by Django 2.0.2 on 2018-05-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20180510_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='account_bonus',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=65, max_length=65),
        ),
    ]
