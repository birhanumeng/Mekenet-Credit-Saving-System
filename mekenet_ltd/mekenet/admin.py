from django.contrib import admin

from . models import CustomerInfo, CustomerLoan, CustomerSaving


# Register your models here.
admin.site.register(CustomerInfo)
admin.site.register(CustomerLoan)
admin.site.register(CustomerSaving)
