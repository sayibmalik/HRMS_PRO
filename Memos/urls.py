from django.urls import path, include
from .views import AllMemos,CreateMemo,editMemo,MyMemos,deleteMemo

from django.conf.urls import url


urlpatterns = [

    path("AllMemos",AllMemos,name="AllMemos"),
    path("MyMemos",MyMemos,name="MyMemos"),
    path("CreateMemo",CreateMemo,name="CreateMemo"),
    path("deleteMemo",deleteMemo,name="deleteMemo"),
    url(r'^editMemo/(?P<pk>[0-9]+)/$', editMemo, name='editMemo'),
]