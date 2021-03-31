from django.contrib import admin

# Register your models here.

from .models import new_startup
from .models import member

admin.site.register(new_startup)
admin.site.register(member)

