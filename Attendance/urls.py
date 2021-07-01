from django.urls import path, include
from .views import Cards,People,Myattendance,ManageAttendance

from django.conf.urls import url

urlpatterns = [
    path('cards/', Cards, name='Cards'),
    path('people/', People, name='People'),
    path('myattendance/', Myattendance, name='Myattendance'),
    path('ManageAttendance/', ManageAttendance, name='ManageAttendance'),
]
