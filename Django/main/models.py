from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT, SET_NULL
from job.models import Project
from authentication.models import Member, Startup

# Create your models here.
class Bid(models.Model):
    startup = models.ForeignKey(Startup,on_delete=CASCADE)
    project = models.ForeignKey(Project, on_delete=CASCADE)
    q1_ans = models.TextField(max_length=1024,blank=True)
    q2_ans = models.TextField(max_length=1024,blank=True)
    q3_ans = models.TextField(max_length=1024,blank=True)

    def __str__(self):
        return self.startup.company_name if self.startup.company_name else str(self.startup.uid)

class Accept(models.Model):
    startup = models.ForeignKey(Startup,on_delete=RESTRICT)
    contact_person = models.ForeignKey(Member,on_delete=RESTRICT)
    project = models.ForeignKey(Project,on_delete=RESTRICT)
    completed = models.BooleanField(default=False)
    percentage_completion = models.PositiveSmallIntegerField(default=0)
    payment_iters = models.PositiveSmallIntegerField(default=0,verbose_name='Payment Iterations')
    total_paid_amount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.project.project_name +' | '+self.startup.company_name
    
class Update(models.Model):
    accept = models.ForeignKey(Accept,on_delete=RESTRICT)
    updated_by = models.ForeignKey(Member,on_delete=RESTRICT)
    timestamp = models.DateTimeField(auto_now_add=True)
    update_message = models.TextField(max_length=2048)
    update_percentage = models.PositiveSmallIntegerField(default=0)
    approval = models.BooleanField(default=False)
    def __str__(self):
        return self.accept.project.project_name +' | '+ self.accept.startup.company_name 

class Payment(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    tansaction_id = models.CharField(max_length=20,default='')
    amount = models.PositiveIntegerField(default=0)
    accept = models.ForeignKey(Accept,on_delete=CASCADE)
    percent = models.PositiveSmallIntegerField(default=0,verbose_name="Completion Percentage At Payment")