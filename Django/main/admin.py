from django.contrib import admin
from .models import Bid,Accept,Update,Payment
# Register your models here.
class BidAdmin(admin.ModelAdmin):
    list_display = ('startup','project')

class AcceptAdmin(admin.ModelAdmin):
    list_display = ('project','startup')

class UpdateAdmin(admin.ModelAdmin):
    list_display = ('accept','update_message','updated_by','timestamp')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('accept','amount','percent','timestamp')

admin.site.register(Bid,BidAdmin)
admin.site.register(Accept,AcceptAdmin)
admin.site.register(Update,UpdateAdmin)
admin.site.register(Payment,PaymentAdmin)