from django.contrib import admin
from .models import AccountRequest, CreditCardRequest, Account
# Register your models here.

admin.site.register(AccountRequest)
admin.site.register(CreditCardRequest)
admin.site.register(Account)