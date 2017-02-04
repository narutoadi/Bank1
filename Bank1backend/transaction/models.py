from __future__ import unicode_literals

from django.db import models
from banking.models import Account
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.contrib.auth.models import User

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.
class TransactionHistory(models.Model):
	debitedFrom = models.ForeignKey(Account, null=False, related_name='debitedFrom')
	amount = models.IntegerField()
	creditedTo = models.ForeignKey(Account, null=False, related_name='creditedTo')
	
