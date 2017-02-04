from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

# This code is triggered whenever a new user has been created and saved to the database

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
# Create your models here.

class AccountRequest(models.Model):
	ACCOUNT_CHOICES = (
		('S', 'Saving'),
		('C', 'Current'),
	)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	FORM_STATUS_CHOICES = (
		('RP', 'Request pending'),
		('VF', 'Verified but found false'),
		('VT', 'Verified and found true'),
		('AC', 'Account created'),
	)
	formNumber = models.AutoField(primary_key = True)
	fullName = models.CharField(max_length = 60)
	fatherName = models.CharField(max_length = 60)
	motherName = models.CharField(max_length = 60)
	dob = models.DateField()
	addressProof = models.ImageField(upload_to='addressProof')
	idProof = models.ImageField(upload_to='idProof')
	panNumber = models.CharField(max_length=10, unique=True)
	panCard = models.ImageField(upload_to='panCard')
	accountType = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	email = models.EmailField(max_length=254)
	phoneNumber = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])
	startingAmount = models.IntegerField()
	formStatus = models.CharField(max_length=2,choices=FORM_STATUS_CHOICES, default='RP')
	
	def __str__(self):
		return self.panNumber

class CreditCardRequest(models.Model):
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	CREDIT_CARD_CHOICES = (
		('B', 'Bronz'),
		('S', 'Silver'),
		('G', 'Gold'),
    )
	fullName = models.CharField(max_length = 60)
	fatherName = models.CharField(max_length = 60)
	motherName = models.CharField(max_length = 60)
	dob = models.DateField()
	gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
	idProof = models.ImageField(upload_to='idProof')
	addressProof = models.ImageField(upload_to='addressProof')
	panNumber = models.IntegerField()
	panCard = models.ImageField(upload_to='panCard')
	incomeProof = models.ImageField(upload_to='incomeProof')
	email = models.EmailField(max_length=254)
	phoneNumber = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])
	cardType = models.CharField(max_length=1, choices=CREDIT_CARD_CHOICES)
	def __str__(self):
		return self.fullName

class BankDetails(models.Model):
	rowNumber = models.IntegerField(unique=True)
	accountNumberStarting = models.IntegerField()
	debitCardStarting = models.IntegerField()
	creditCardStarting = models.IntegerField()
	accountRequestCount = models.IntegerField()
	creditCardRequestCount = models.IntegerField()
	accountsCount = models.IntegerField()
	creditCardCount = models.IntegerField()

class DebitCard(models.Model):
	debitCardNumber = models.CharField(max_length=16,unique=True)
	validFromMonth = models.IntegerField()
	validFromYear = models.IntegerField()
	validThruMonth = models.IntegerField()
	validThruYear = models.IntegerField()
	lottNo = models.IntegerField()
	cvv = models.CharField(max_length=3)
	pin = models.CharField(max_length=4) #use salt and hash for this field
	def __str__(self):
		return self.debitCardNumber

class Account(models.Model):
	accountNumber = models.CharField(max_length=11,primary_key=True)
	formNumber = models.OneToOneField(AccountRequest)
	debitCardNumber = models.OneToOneField(DebitCard)
	amount = models.IntegerField()

