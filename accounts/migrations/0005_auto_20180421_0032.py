# Generated by Django 2.0.2 on 2018-04-20 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180421_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='status',
            field=models.CharField(blank=True, choices=[('cleader', 'Clan Leader'), ('pleader', 'Party Leader'), ('splayer', 'Solo Player')], max_length=255, null=True),
        ),
    ]
