from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import login, logout



urlpatterns = [
    url(r'', views.user_login),
    url(r'^login/$', views.login, name = 'log_in'),
    url(r'^logout/$', views.logout, name  = 'log_out'),
    #url(r'^home/$', views.home),

]

