from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

admin.site.register(User)
admin.site.register(Customer)
admin.site.register(Employeer)
admin.site.register(TypeOfInsurance)
admin.site.register(Dogovor)
#admin.site.register(ApplicationForPayment)
@admin.register(ApplicationForPayment)
class PageApplicationForPayment(admin.ModelAdmin):
    list_display = ("dogovor","doctor_opinion","customer_request","approved")
admin.site.register(Payment)
admin.site.register(Admin)
# Register your models here.
