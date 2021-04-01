from django.contrib import admin

# Register your models here.

from .models import Startup
from .models import Member

admin.site.register(Startup)
admin.site.register(Member)

