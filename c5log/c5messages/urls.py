from django.conf.urls import patterns, include, url
from c5messages import views


urlpatterns = patterns('',
	url(r'^$', views.HomeView.as_view(), name="home"),
	url(r'^archives/(?P<log_date>\d{1,2}\-\d{1,2}\-\d{4})/$', views.ArchiveView.as_view(), name="archives"),
	url(r'^archives/$', views.ArchiveView.as_view(), name="archives"),
	url(r'^search/page(?P<page>[0-9]+)$', views.SearchView.as_view(), name="search"),
	url(r'^search/$', views.SearchView.as_view(), name="search"),
	url(r'^stats/$', views.StatsView.as_view(), name="stats"),
)