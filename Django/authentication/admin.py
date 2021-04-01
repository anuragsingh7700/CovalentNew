from django.contrib import admin

# Register your models here.

from .models import Startup
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'job_title', 'joining_code')

admin.site.register(Member, MemberAdmin)

class StartUpAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'date_of_creation', 'team_size', 'company_code')

admin.site.register(Startup, StartUpAdmin)
