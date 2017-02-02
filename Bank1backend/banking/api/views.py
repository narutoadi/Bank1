from banking.models import (
	AccountRequest, 
	CreditCardRequest
	)
from banking.api.serializers import (
	AccountRequestSerializer,
	CreditCardRequestSerializer,
	)
from rest_framework import generics
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

class AccountRequestListAPIView(generics.ListAPIView):
	queryset = AccountRequest.objects.all()
	serializer_class = AccountRequestSerializer
	## customize permissions so that only bank employee can see 

class CreditCardRequestListAPIView(generics.ListAPIView):
	queryset = CreditCardRequest.objects.all()
	serializer_class = CreditCardRequestSerializer
	## customize permissions so that only bank employee can see 