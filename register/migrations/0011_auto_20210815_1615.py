# Generated by Django 3.2.6 on 2021-08-15 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20210815_1602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp_user',
            name='its_id',
        ),
        migrations.RemoveField(
            model_name='user_acc',
            name='its_id',
        ),
    ]
