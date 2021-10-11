from django.contrib import admin
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# Register your models here.

from .models import AdminUser, Rating, SiteUser, Startup, PaymentMethod, Rating
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('user_id','first_name','job_title', 'startup')

admin.site.register(Member, MemberAdmin)

# class StartUpAdmin(UserAdmin):
#     list_display = ('company_name', 'date_of_creation', 'team_size')
#     list_filter = ('company_name', 'date_of_creation', 'team_size')
#     # fieldsets = (
#     #     (None,{'fields': ('email', 'password')}),
#     #     ('Permissions',{'fields': ('is_staff','is_active')})
#     # )
#     # add_fieldsets = (
#     #     (None,{
#     #         'fields' : ('email', 'password1', 'password2', 'is_staff', 'is_active')
#     #     }),
#     # )
#     search_fields = ['company_name','email','company_code','contact_no']
#     ordering = ['email']
#     filter_horizontal = ('groups', 'user_permissions',)
# admin.site.unregister(User)
# admin.site.register(Startup, StartUpAdmin)



# admin.site.unregister(SiteUser)
admin.site.register(SiteUser)
admin.site.register(Startup)
admin.site.register(AdminUser)
# admin.site.register(Member)
admin.site.register(PaymentMethod)
admin.site.register(Rating)