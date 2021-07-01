from django.urls import path, include
from .views import exitreentryvisas,finalexitvisas,passportservices,renewiqama,operationslog,issue,\
    cancel,reprintexitreentryvisy,updatepassportinfo,updatepassportexpirydate

from django.conf.urls import url


urlpatterns = [
    path('ExitReentryVisas/',exitreentryvisas,name='exitreentryvisas'),
    path('FinalExitVisas/',finalexitvisas,name='finalexitvisas'),
    path('PassportServices/',passportservices,name='passportservices'),
    path('RenewIqama/',renewiqama,name='renewiqama'),
    path('OperationsLog/',operationslog,name='operationslog'),
    path('Issue/',issue,name='issue'),
    path('Cancel/',cancel,name='cancel'),
    path('ReprintExitReentryVisa/',reprintexitreentryvisy,name='reprintexitreentryvisy'),
    path('UpdatePassportInfo/',updatepassportinfo,name='updatepassportinfo'),
    path('UpdatePassportExpiryDate/',updatepassportexpirydate,name='updatepassportexpirydate'),
]