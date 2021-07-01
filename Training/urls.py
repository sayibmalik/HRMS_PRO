from django.urls import path, include
from .views import Training, Createtraining,editTraining,trainingDetails

from django.conf.urls import url


urlpatterns = [

    path("Training",Training,name="Training"),
    path("Createraining",Createtraining,name="Createraining"),
    url(r'^editTraining/(?P<pk>[0-9]+)/$', editTraining, name='editTraining'),
    url(r'^trainingDetails/(?P<pk>[0-9]+)/$', trainingDetails, name='trainingDetails'),
]