from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
	url(r'^$', TemplateView.as_view(template_name="app/index.html"), name='index'),
	url(r'^banking/', include("banking.urls")),
	url(r'^admin/', admin.site.urls),
	url(r'^api/banking/', include("banking.api.urls")),
]