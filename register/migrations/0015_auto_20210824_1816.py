# Generated by Django 3.2.6 on 2021-08-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0014_user_acc_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='temp_user',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='temp_user',
            name='last_studied_class',
        ),
        migrations.RemoveField(
            model_name='temp_user',
            name='year_of_passing',
        ),
        migrations.RemoveField(
            model_name='user_acc',
            name='father_name',
        ),
        migrations.RemoveField(
            model_name='user_acc',
            name='last_studied_class',
        ),
        migrations.RemoveField(
            model_name='user_acc',
            name='year_of_passing',
        ),
        migrations.AddField(
            model_name='temp_user',
            name='blood_group',
            field=models.CharField(choices=[('A +', 'A+'), ('B +', 'B+'), ('A -', 'A-'), ('B -', 'B-'), ('BA +', 'BA+'), ('BA -', 'BA-'), ('O +', 'O+'), ('O -', 'O-')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='child_in_msb',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='maritial_status',
            field=models.CharField(blank=True, choices=[('married', 'Married'), ('un-married', 'Un Married')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='temp_user',
            name='whatsapp_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user_acc',
            name='blood_group',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='user_acc',
            name='child_in_msb',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='user_acc',
            name='maritial_status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='user_acc',
            name='whatsapp_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
