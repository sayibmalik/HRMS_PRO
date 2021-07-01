from django.urls import path, include
from .views import calendar
from django.conf.urls import url
urlpatterns = [

    path('calendar', calendar, name='calendar'),


]
