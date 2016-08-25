from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.schedule_list, name='schedule_list'),
	url(r'^schedule/(?P<pk>[0-9]+)/$', views.schedule_detail, name='schedule_detail'),
	
]