from django.conf.urls import patterns, url
from saisie_absences import views
from saisie_absences.views import AbsencesView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^saisie/$', views.saisie, name='saisie'),
	url(r'^list/tojustify/$', AbsencesView.as_view(toJustify=True), name='list_tojustify'),
	url(r'^list/$', AbsencesView.as_view(), name='list'),
)