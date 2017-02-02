from django.conf.urls import url
from banking.views import IndexView

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
]