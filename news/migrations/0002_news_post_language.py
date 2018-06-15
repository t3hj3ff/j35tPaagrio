# Generated by Django 2.0.2 on 2018-04-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='post_language',
            field=models.CharField(blank=True, choices=[('ka', 'Georgian'), ('en', 'English'), ('ru', 'Russian')], max_length=255, null=True),
        ),
    ]