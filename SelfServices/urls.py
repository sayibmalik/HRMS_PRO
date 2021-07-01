from django.urls import path, include
from .views import requestsalaryletter,requestleaves,requestexcuse,requestoutofoffice,requestovertime,\
    requestbusinesstrip,requesttravelticketfordependants,requestlone,requestgrievance,requesttraingcourse,\
    pendingrequests,myrequests,employeerequests

from django.conf.urls import url


urlpatterns = [
    path('requestsalaryletter/', requestsalaryletter, name='requestsalaryletter'),
    path('requestleaves/', requestleaves, name='requestleaves'),
    path('requestexcuse/', requestexcuse, name='requestexcuse'),
    path('requestoutofoffice/', requestoutofoffice, name='requestoutofoffice'),
    path('requestovertime/', requestovertime, name='requestovertime'),
    path('requestbusinesstrip/', requestbusinesstrip, name='requestbusinesstrip'),
    path('requesttravelticketfordependants/', requesttravelticketfordependants, name='requesttravelticketfordependants'),
    path('requestlone/', requestlone, name='requestlone'),
    path('requestgrievance/', requestgrievance, name='requestgrievance'),
    path('requesttraingcourse/', requesttraingcourse, name='requesttraingcourse'),
    path('pendingrequests/', pendingrequests, name='pendingrequests'),
    path('myrequests/', myrequests, name='myrequests'),
    path('employeerequests/', employeerequests, name='employeerequests'),
]