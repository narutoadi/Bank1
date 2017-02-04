from django.conf.urls import url
from django.contrib import admin

from .views import (
	AccountRequestCreateAPIView,
	CreditCardRequestCreateAPIView,
	AccountRequestListAPIView,
	CreditCardRequestListAPIView,
	FormStatusAPIView,
	)
from . import views

urlpatterns = [
	url(r'^AccountRequest/post/$', AccountRequestCreateAPIView.as_view(), name='createAccountRequest'),
	url(r'^FormStatus/get/(?P<panNumber>[\w]+)/$',FormStatusAPIView.as_view(), name='getFormStatus' ),
	url(r'^CreditCardRequest/post/$', CreditCardRequestCreateAPIView.as_view(), name='createCreditCardRequest'),
	url(r'^AccountRequest/get/$', AccountRequestListAPIView.as_view(), name='createAccountRequest'),
	url(r'^CreditCardRequest/get/$', CreditCardRequestListAPIView.as_view(), name='createCreditCardRequest'),
	url(r'^isPossible/(?P<dcNum>[\w]+)/(?P<vtm>[\d]+)/(?P<vty>[\d]+)/(?P<cvv>[\w]+)/$', views.isTransactionPossible, name='isPossible'),
]