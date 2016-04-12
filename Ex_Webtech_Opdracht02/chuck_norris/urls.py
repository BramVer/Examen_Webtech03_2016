from django.conf.urls import url
from . import views

app_name = 'chuck_norris'
urlpatterns = [
		#example: /chuck_norris/
	url(r'^$', views.IndexView.as_view(), name='index'),
]