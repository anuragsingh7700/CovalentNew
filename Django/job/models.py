from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=40, verbose_name='Add Tags')

    def __str__(self):
        return self.title


PROJECT_STATUS_CHOICES = (
    ('open', 'Open'),
    ('closed', 'Closed'),
)


# Create your models here.
class job_post(models.Model):
    project_name = models.CharField(max_length=250)
    project_description = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    duration = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    ##latest_job_post = job_post.objects.filter(
    ##        status='').order_by('-timestamp')[0:3]
    status = models.CharField(max_length=35, choices=PROJECT_STATUS_CHOICES, default='open')
