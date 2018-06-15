# Generated by Django 2.0.2 on 2018-04-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('login', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('last_access', models.IntegerField()),
                ('access_level', models.IntegerField()),
                ('last_ip', models.CharField(blank=True, max_length=15, null=True)),
                ('last_server', models.IntegerField()),
                ('bonus', models.IntegerField()),
                ('bonus_expire', models.IntegerField()),
                ('ban_expire', models.IntegerField()),
                ('allow_ip', models.CharField(max_length=255)),
                ('allow_hwid', models.CharField(max_length=255)),
                ('points', models.IntegerField()),
                ('acc_switch_times', models.IntegerField()),
                ('first_acc_switch_time', models.BigIntegerField()),
                ('master_account', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'accounts',
                'managed': True,
            },
        ),
    ]
