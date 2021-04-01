from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from random import choice
import string

# Create your models here.

class Startup(models.Model):
    #details of the registrar
    #founder_name = models.CharField(max_length=50)
    #founder_pan_id = models.CharField(max_length=20)
    #company details
    registration_no = models.CharField(max_length=20,primary_key=True)
    company_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=10) #validation should be added in forms
    company_email = models.EmailField(max_length=254)
    date_of_creation = models.DateField(default=timezone.now)
    industry = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    team_size = models.IntegerField()
    company_code = models.CharField(default = ''.join((choice(string.ascii_uppercase) for x in range(7))), unique=True,max_length=7) #this will be used as team-code


class Member(models.Model):
    # profile_picture = models.ImageField(upload_to="employee_pic/", null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    job_title = models.CharField(max_length=50) #position in the company
    joining_date = models.CharField(max_length=50, default=timezone.now)
    joining_code = models.ForeignKey(Startup, on_delete=models.CASCADE)





