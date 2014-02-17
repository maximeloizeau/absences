from django.conf.urls import patterns, url
from saisie_absences import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^saisie/$', views.saisie, name='saisie'),
)