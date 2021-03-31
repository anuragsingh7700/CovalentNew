from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.

class new_startup(models.Model):
    #details of the registrar
    #founder_name = models.CharField(max_length=50)
    #founder_pan_id = models.CharField(max_length=20)
    #company details
    registration_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    contact_no = models.CharField(max_length=12) #validation should be added in forms
    company_email = models.EmailField(max_length=254)
    industry = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    team_size = models.IntegerField()
    company_code = models.PositiveIntegerField(validators=[MinValueValidator(10000)], primary_key=True) #this will be used as team-code

class member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    dob = models.DateField()
    job_title = models.CharField(max_length=50) #position in the company
    joining_date = models.CharField(max_length=50)
    joining_code = models.ForeignKey(new_startup, on_delete=models.CASCADE)





