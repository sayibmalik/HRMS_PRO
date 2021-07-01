from django.urls import path, include
from .views import Recruitment,Applyjob,deljob,editrecruitment

from django.conf.urls import url

urlpatterns = [

    path('recruitment/', Recruitment, name='Recruitment'),
    path('deljob/', deljob, name='deljob'),
    url(r'^applyjob/(?P<pk>[0-9]+)/$',Applyjob , name='Applyjob'),
    url(r'^editrecruitment/(?P<pk>[0-9]+)/$',editrecruitment , name='editrecruitment'),

]
