from banking.models import (
	AccountRequest, 
	CreditCardRequest,
	DebitCard,
	Account,
	)
from banking.api.serializers import (
	AccountRequestSerializer,
	CreditCardRequestSerializer,
	FormStatusSerializer,
	DebitCardSerializer,
	)
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly,
	)

class AccountRequestCreateAPIView(generics.CreateAPIView):
	queryset = AccountRequest.objects.all()
	serializer_class = AccountRequestSerializer
	permission_classes = [AllowAny]

class CreditCardRequestCreateAPIView(generics.CreateAPIView):
	queryset = CreditCardRequest.objects.all()
	serializer_class = CreditCardRequestSerializer
	permission_classes = [AllowAny]

class FormStatusAPIView(generics.RetrieveAPIView):
	queryset = AccountRequest.objects.all()
	serializer_class = FormStatusSerializer
	permission_classes = [AllowAny]
	lookup_field = 'panNumber'

class AccountRequestListAPIView(generics.ListAPIView):
	queryset = AccountRequest.objects.all()
	serializer_class = AccountRequestSerializer
	## customize permissions so that only bank employee can see 

class CreditCardRequestListAPIView(generics.ListAPIView):
	queryset = CreditCardRequest.objects.all()
	serializer_class = CreditCardRequestSerializer
	## customize permissions so that only bank employee can see 

@api_view(['GET'])
def isTransactionPossible(request):
	response = Response()
	if request.method == 'GET':
		card = DebitCard.objects.filter(debitCardNumber = request.dcNum, validThruMonth = request.vtm,	validThruYear = request.vty, cvv = request.cvv)
		if card.count() == 0:
			response['cardFound'] = False
			response['transactionPossible'] = False
			return response
		else:
			response['cardFound'] = True
			id = card[0:1].get().id
			acc = Account.objects.filter(debitCardNumber = id)
			if acc.count() == 0:
				response['accountFound'] = False
				response['transactionPossible'] = False
				return response
			else:
				response['accountFound'] = True
				bal = acc[0:1].get.amount
				if bal >= request.amount:
					response['transactionPossible'] = True
					response['accountNumber'] = acc[0:1].get.accountNumber
					return response
				else:
					response['transactionPossible'] = False
					return response


