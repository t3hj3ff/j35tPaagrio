# Generated by Django 2.0.2 on 2018-04-20 09:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20180420_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_ka',
            field=models.TextField(default=django.utils.timezone.now, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='text_ru',
            field=models.TextField(default=django.utils.timezone.now, max_length=1024),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_ka',
            field=models.CharField(default=django.utils.timezone.now, max_length=65),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(default=django.utils.timezone.now, max_length=65),
            preserve_default=False,
        ),
    ]
