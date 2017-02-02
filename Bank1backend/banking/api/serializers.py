from rest_framework.serializers import ModelSerializer
from banking.models import AccountRequest, CreditCardRequest

class AccountRequestSerializer(ModelSerializer):
	class Meta:
		model = AccountRequest
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
			'accountType',
			'startingAmount',
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

