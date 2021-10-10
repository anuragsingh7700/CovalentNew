from django.contrib import admin
from .models import Project, Tag
from django.contrib.auth.models import Group

# Register your models here.

#admin.site.register(Project)
admin.site.register(Tag)


class JobsAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'project_description', 'deadline', 'status')


admin.site.register(Project, JobsAdmin)
admin.site.unregister(Group)