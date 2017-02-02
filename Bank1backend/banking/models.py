from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from PIL import Image
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
	fullName = models.CharField(max_length = 60)
	fatherName = models.CharField(max_length = 60)
	motherName = models.CharField(max_length = 60)
	dob = models.DateField()
	addressProof = models.ImageField(upload_to='addressProof')
	idProof = models.ImageField(upload_to='idProof')
	panNumber = models.IntegerField()
	panCard = models.ImageField(upload_to='panCard')
	accountType = models.CharField(max_length=1, choices=ACCOUNT_CHOICES)
	gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
	email = models.EmailField(max_length=254)
	phoneNumber = models.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])
	startingAmount = models.IntegerField()
	def __str__(self):
		return self.fullName

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


