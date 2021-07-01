from django.urls import path, include
from .views import endofserviceforemployee,suspendemployeesalary,transferemployeedecision,\
    pendingdecision,mydecisions,alldecision

from django.conf.urls import url


urlpatterns = [
    path('EndofserviceforEmployee/',endofserviceforemployee,name='EndofserviceforEmployee'),
    path('SuspendEmployeeSalary/',suspendemployeesalary,name='suspendemployeesalary'),
    path('TransferEmployeeDecision/',transferemployeedecision,name='transferemployeedecision'),
    path('PendingDecision/',pendingdecision,name='pendingdecision'),
    path('MyDecisions/',mydecisions,name='mydecisions'),
    path('AllDecision/',alldecision,name='alldecision'),
]