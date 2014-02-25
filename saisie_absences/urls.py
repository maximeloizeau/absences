from django.conf.urls import patterns, url
from saisie_absences import views
from saisie_absences.views import AbsencesView

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^saisie/$', views.saisie, name='saisie'),
	url(r'^list/tojustify/$', AbsencesView.as_view(toJustify=True), name='list_tojustify'),
	url(r'^list/department/$', AbsencesView.as_view(department=True), name='list_selfdepartment'),
	url(r'^list/department/([A-Za-z0-9]+)$', AbsencesView.as_view(department=True), name='list_department'),
	url(r'^list/year/$', AbsencesView.as_view(year=True), name='list_selfyear'),
	url(r'^list/year/([A-Za-z0-9]+)$', AbsencesView.as_view(year=True), name='list_year'),
	url(r'^list/$', AbsencesView.as_view(), name='list'),
	url(r'^justificatif/$', views.justificatif, name='justificatif'),
	url(r'^api/absences/list/([0-9]*)$', views.api_absences_list, name='api_absences_list'),
)