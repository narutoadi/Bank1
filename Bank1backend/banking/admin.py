from django.contrib import admin
from .models import AccountRequest, CreditCardRequest
# Register your models here.

admin.site.register(AccountRequest)
admin.site.register(CreditCardRequest)