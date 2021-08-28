from django.db import models
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User
import uuid
import datetime
# Create your models here.


def string_cheker(value):
    regex = re.compile('[@_!"#$%^&*()<>?/\|}{~:]')


    if(regex.search(value) == None):
        return value
    else:
        raise ValidationError("Name should not contain special characters.")

def its_check(value):
    test = User_acc.objects.get(its_id=value)
    if test is None:
        return value
    else:
        raise ValidationError("User with this Its id exists.")

class Temp_user(models.Model):
    
    BLOOD_GROUP = (
        ("A +", "A+"),
        ("B +", "B+"),
        ("A -", "A-"),
        ("B -", "B-"),
        ("BA +", "BA+"),
        ("BA -", "BA-"),
        ("O +", "O+"),
        ("O -", "O-")
    )

    MARATIAL_STATUS = (
        ('married', "Married"),
        ('un-married', "Un Married")
    )

    YEARS= tuple([(x,x) for x in range(2001, int(datetime.datetime.now().date().year) + 1)])

    name = models.CharField(max_length=200, null=True, blank=False, validators=[string_cheker])
    phone_number = models.CharField(max_length=10, null=True, blank=False)
    whatsapp_number = models.CharField(max_length=10, null=True, blank=False)
    its_id = models.CharField(max_length=8, null=True, blank=False, unique=True)
    profession = models.CharField(max_length=200, null=True, blank=False)
    qualification= models.CharField(max_length=100, null=True, blank=False)
    email = models.EmailField(null=True, blank=False, unique=True)
    blood_group = models.CharField(max_length=10, null=True, blank=False, choices=BLOOD_GROUP)
    maritial_status = models.CharField(max_length=20, null=True, blank=False, choices=MARATIAL_STATUS)
    child_in_msb = models.BooleanField(null=True, blank=False)
    year_of_passing = models.CharField(max_length=4, null=True, blank=False, choices=YEARS)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name

class User_acc(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,)    
    name = models.CharField(max_length=200, null=True, validators=[string_cheker])
    phone_number = models.CharField(max_length=10, null=True)
    whatsapp_number = models.CharField(max_length=10, null=True, blank=False)
    its_id = models.CharField(max_length=8, null=True, unique=True)
    profession = models.CharField(max_length=200, null=True)
    qualification= models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True, unique=True)
    blood_group = models.CharField(max_length=10, null=True, blank=False)
    maritial_status = models.CharField(max_length=20, null=True, blank=True)
    child_in_msb = models.BooleanField(null=True, blank=False)
    year_of_passing = models.CharField(max_length=4, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name