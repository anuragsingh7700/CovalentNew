from django.contrib import admin
from .models import job_post, Tags

# Register your models here.

admin.site.register(job_post)
admin.site.register(Tags)
