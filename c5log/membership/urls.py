from django.conf.urls import patterns, include, url
from membership import views


urlpatterns = patterns('',
	url(r'^login/$', views.LoginView.as_view(), name="login"),
	url(r'^logout/$', views.logout_user, name="logout"),
)