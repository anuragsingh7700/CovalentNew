from django.db import models
from django.db.models.deletion import CASCADE

from authentication.models import Startup,Member


class Tag(models.Model):
    title = models.CharField(max_length=40, verbose_name='Add Tags')

    def __str__(self):
        return self.title


PROJECT_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)


# Create your models here.
class Project(models.Model):
    startup = models.ForeignKey(Startup,on_delete=CASCADE)
    project_name = models.CharField(max_length=250)
    project_description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    deadline = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    ##latest_job_post = job_post.objects.filter(
    ##        status='').order_by('-timestamp')[0:3]
    status = models.CharField(max_length=35, choices=PROJECT_STATUS_CHOICES, default='open')
    cost = models.CharField(max_length=128)
    q1 = models.CharField(max_length=512,default='',verbose_name='Question 1',blank=True)
    q2 = models.CharField(max_length=512,default='',verbose_name='Question 1',blank=True)
    q3 = models.CharField(max_length=512,default='',verbose_name='Question 1',blank=True)

    def __str__(self):
        return self.project_name

class Star(models.Model):
    startup =  models.ForeignKey(Startup, on_delete=CASCADE)
    added_by = models.ForeignKey(Member, on_delete=CASCADE)
    project = models.ForeignKey(Project, on_delete=CASCADE)