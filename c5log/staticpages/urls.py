from django.conf.urls import patterns, include, url
from staticpages import views


urlpatterns = patterns('',
	url(r'^about/$', views.AboutView.as_view(), name="about"),
	url(r'^bot/$', views.BotView.as_view(), name="bot")
)