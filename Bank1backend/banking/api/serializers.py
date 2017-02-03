from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.core.validators import RegexValidator
from banking.models import AccountRequest, CreditCardRequest
from drf_extra_fields.fields import Base64ImageField

class AccountRequestSerializer(serializers.Serializer):
	ACCOUNT_CHOICES = (
		('S', 'Saving'),
		('C', 'Current'),
	)
	GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
	fullName = serializers.CharField(required=True);
	fatherName = serializers.CharField(required=True);
	motherName = serializers.CharField(required=True);
	dob = serializers.DateField(required=True);
	gender = serializers.ChoiceField(choices=GENDER_CHOICES,required=True);
	email = serializers.EmailField(required=True);
	phoneNumber = serializers.CharField(max_length=16,validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format '+9999999'. Upto 15 digits are allowed.")])
	panNumber = serializers.CharField(max_length=10, required=True);
	accountType = serializers.ChoiceField(choices=ACCOUNT_CHOICES,required=True);
	startingAmount = serializers.IntegerField(required=True);
	addressProof = Base64ImageField(required=True);
	idProof = Base64ImageField(required=True);
	panCard = Base64ImageField(required=True);
	def create(self, validated_data):
		print (validated_data)
		return AccountRequest.objects.create(**validated_data)
	
class FormStatusSerializer(ModelSerializer):
	class Meta:
		model = AccountRequest
		fields = [
			'formNumber',
			'formStatus',
			'panNumber',
		]

class CreditCardRequestSerializer(ModelSerializer):
	class Meta:
		model = CreditCardRequest
		fields = [
			'fullName',
			'fatherName',
			'motherName',
			'dob',
			'gender',
			'email',
			'phoneNumber',
			'panNumber',
			'addressProof',
			'idProof',
			'panCard',
			'incomeProof',
			'cardType',
		]

