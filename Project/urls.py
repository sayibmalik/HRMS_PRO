from django.urls import path, include
from .views import CreateProject, delproject, retrieveproject, Editproject

from django.conf.urls import url

urlpatterns = [

    # # path('projects/', Project, name='Project'),
    path('delproject/', delproject, name='delproject'),
    path('CreateProject/', CreateProject, name='CreateProject'),
    path('retrieveproject/', retrieveproject, name='retrieveproject'),
    url(r'^editproject/(?P<pk>[0-9]+)/$',Editproject , name='Editproject'),

]
