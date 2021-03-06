# Generated by Django 3.2.6 on 2021-08-13 11:38

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_alter_temp_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_user',
            name='father_name',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[register.models.string_cheker]),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='qualification',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='temp_user',
            name='profession',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
