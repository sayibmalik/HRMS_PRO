from django.urls import path, include
from .views import ViewPolicies,CreatePolicies,managePolicies,editPolicies,deletePolicies

from django.conf.urls import url


urlpatterns = [

    path("ViewPolicies",ViewPolicies,name="ViewPolicies"),
    path("managePolicies",managePolicies,name="managePolicies"),
    path("CreatePolicies",CreatePolicies,name="CreatePolicies"),
    path("deletePolicies",deletePolicies,name="deletePolicies"),
    url(r'^editPolicies/(?P<pk>[0-9]+)/$', editPolicies, name='editPolicies'),
]