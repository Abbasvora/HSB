# Generated by Django 3.2.6 on 2021-08-13 11:27

from django.db import migrations, models
import register.models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='temp_user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, validators=[register.models.string_cheker]),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='profession',
            field=models.CharField(blank=True, choices=[('engineer', 'Engineer'), ('doctor', 'Doctor'), ('businessman', 'Businessman'), ('ca', 'Charted Accountant'), ('freelancer', 'Freenlancer')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='temp_user',
            name='last_studied_class',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='temp_user',
            name='year_of_passing',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]