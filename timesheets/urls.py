from django.urls import path, include
from .views import MyTimesheet,ToApprove, Reports
from django.conf.urls import url
urlpatterns = [

    path('timesheet-dashboard/', MyTimesheet, name='MyTimesheet'),
    path('toapprove/', ToApprove, name='ToApprove'),
    path('reports/', Reports, name='Reports')

]