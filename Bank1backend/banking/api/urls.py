from django.conf.urls import url
from django.contrib import admin

from .views import (
	AccountRequestCreateAPIView,
	CreditCardRequestCreateAPIView,
	AccountRequestListAPIView,
	CreditCardRequestListAPIView,
	)

urlpatterns = [
	url(r'^AccountRequest/post/$', AccountRequestCreateAPIView.as_view(), name='createAccountRequest'),
	url(r'^CreditCardRequest/post/$', CreditCardRequestCreateAPIView.as_view(), name='createCreditCardRequest'),
	url(r'^AccountRequest/get/$', AccountRequestListAPIView.as_view(), name='createAccountRequest'),
	url(r'^CreditCardRequest/get/$', CreditCardRequestListAPIView.as_view(), name='createCreditCardRequest'),
]