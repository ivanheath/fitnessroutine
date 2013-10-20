from django.conf.urls import patterns, url

from routine import views


urlpatterns = patterns('',
    url(r'^main/$', views.main, name='main'),
    url('^main/exercise/', views.addexercise, name='exercise'),
    url(r'^main/routine/', views.routine, name='routine'),
    url(r'^main/addroutine', views.addroutine, name='addroutine'),
    url(r'^routineadded', views.routineadded, name='routineadded'),
    url(r'^main/deleteroutine', views.deleteroutine, name='deleteroutine'),
    url(r'^main/addexercise', views.exerciseadded, name='exerciseadded'),
)
