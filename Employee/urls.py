from django.urls import path, include
from .views import employees,createemployees,ViewEmployees,EditEmployee,saveemployee,savecontract,access,manageAccess

from django.conf.urls import url

urlpatterns = [
    # path('employees/', employees, name='employees'),
    path('createemployees/', createemployees, name='createemployees'),
    path('viewemployees/', ViewEmployees, name='ViewEmployees'),
    path('saveemployee/', saveemployee, name='saveemployee'),
    path('savecontract/', savecontract, name='savecontract'),
    url(r'^employees/(?P<pk>[0-9]+)/$', employees, name='employees'),
    url(r'^editemployee/(?P<pk>[0-9]+)/$', EditEmployee, name='EditEmployee'),
    url(r'^manageAccess/(?P<pk>[0-9]+)/$', manageAccess, name='manageAccess'),
    path('access/', access, name='access'),
]