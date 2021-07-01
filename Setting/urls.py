from django.urls import path, include
from .views import Users, CreateUser, Companies, delcompany, Editcompany, CreateCompany, CreateBuilding, CreateFloor, \
    Buildings, Floors, departments, CreateDepartments, Editdepartment, deldepartment, Editbuilding, delbuilding, Editfloor, \
    delfloor, viewcompany,UserEmployees

from django.conf.urls import url

urlpatterns = [
    path('users/', Users, name='Users'),
    path('createuser/', CreateUser, name='Createuser'),
    path('companies/', Companies, name='Companies'),
    path('createcompany/', CreateCompany, name='CreateCompany'),
    path('delcompany/', delcompany, name='delcompany'),
    # path('editcompany/', Editcompany,name='Editcompany'),
    url(r'^editcompany/(?P<pk>[0-9]+)/$',Editcompany , name='Editcompany'),
    path('createbuilding/', CreateBuilding, name='CreateBuilding'),
    path('createfloor/', CreateFloor, name='CreateFloor'),
    path('buildings/', Buildings, name='Buildings'),
    path('floors/', Floors, name='Floors'),
    path('departments/', departments, name='departments'),
    path('createdepartments/', CreateDepartments, name='CreateDepartments'),
    url(r'^editdepartment/(?P<pk>[0-9]+)/$',Editdepartment , name='Editdepartment'),
    path('deldepartment/', deldepartment, name='deldepartment'),
    url(r'^editbuilding/(?P<pk>[0-9]+)/$',Editbuilding , name='Editbuilding'),
    path('delbuilding/', delbuilding, name='delbuilding'),
    url(r'^editfloor/(?P<pk>[0-9]+)/$',Editfloor , name='Editfloor'),
    path('delfloor/', delfloor, name='delfloor'),
    path('viewcompany/', viewcompany, name='viewcompany'),
    url(r'^useremployees/(?P<pk>[0-9]+)/$', UserEmployees, name='useremployees'),

]
