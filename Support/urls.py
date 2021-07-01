from django.urls import path, include
from .views import supportTickets,createSupport,ticketDetails
from django.conf.urls import url


urlpatterns = [

    path("supportTickets",supportTickets,name="supportTickets"),
    path("createSupport",createSupport,name="createSupport"),
    url(r'^ticketDetails/(?P<pk>[0-9]+)/$', ticketDetails, name='ticketDetails'),
]