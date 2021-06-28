from django.urls import re_path
from . import views

app_name = 'users'
urlpatterns = [
    re_path(r'^register/$', views.register, name='register'),
    re_path(r'^login/$', views.login, name='login'),
    re_path(r'^user/(?P<pk>\d+)/profile/$', views.profile, name='profile'),
    re_path(r'^user/(?P<pk>\d+)/profile/update/$', views.profile_update, name='profile_update'),
    re_path(r'^user/(?P<pk>\d+)/pwdchange/$', views.pwd_change, name='pwd_change'),
    re_path(r'^user/(?P<pk>\d+)/upload/$', views.upload_experiment, name='upload'),
    re_path(r'^user/(?P<pk>\d+)/filelist/$', views.file_list, name='filelist'),
    re_path(r'^user/(?P<pk>\d+)/filelist/(?P<fid>\d+)/download/$', views.result, name='download'),
    re_path(r'success/$', views.success_response, name='success'),
    re_path(r'^logout/$', views.logout, name='logout'),
]
