from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.login, name='login'),
    url(r'^main/$', views.logincheck, name='main'),
    url(r'^newuser/$', views.newuser, name='newuser'),
    url(r'^newuser/useradded', views.useradded, name='useradded'),
)
