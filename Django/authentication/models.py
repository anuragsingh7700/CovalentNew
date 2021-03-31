from django.db import models

# Create your models here.

class new_startup(models.Model):
    #details of the registrar
    founder_name = models.CharField(max_length=50)
    founder_pan_id = models.CharField(max_length=20)
    #company details
    registration_no = models.CharField(max_length=20)
    company_name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    team_size = models.IntegerField()
    company_code = models.IntegerField() #this will be used as team-code

class member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    dob = models.DateTimeField()
    job_title = models.CharField(max_length=50) #position in the company
    joining_date = models.CharField(max_length=50)
    joining_code = models.IntegerField()





