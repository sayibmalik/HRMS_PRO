from django.urls import path, include
from .views import Appraisals, announcements, createAnnouncements, createAppraisals, approveAnnouncements, \
    answerAppraisal, ViewAppraisal, \
    EmployeeTransfer, EmployeesSettings, Contracts, createContracts, Recruitment, Contactss, CreateContacts, \
    ContactTag, CreateContactTags, ContactTitles, delannouncement, Editannouncements, ViewContact, ContractTemplate, \
    document, \
    Createdocuments, Editdocuments, Notes, Createnotes, Editnotes, assets, Createassets, Editassets, delnotes, \
    delassets, deldocument, delcontact, editContract

from django.conf.urls import url

urlpatterns = [
    path('appraisals/', Appraisals, name='Appraisals'),
    path('announcements/', announcements, name='announcements'),
    path('createannouncements/', createAnnouncements, name='createAnnouncements'),
    path('delannouncement/', delannouncement, name='delannouncement'),
    url(r'^editannouncement/(?P<pk>[0-9]+)/$', Editannouncements, name='editannouncements'),
    path('createappraisals/', createAppraisals, name='createAppraisals'),
    path('approveannouncements/', approveAnnouncements, name='approveAnnouncements'),
    path('answerappraisal/', answerAppraisal, name='answerAppraisal'),
    path('contacts/', Contactss, name='Contacts'),
    path('createcontacts/', CreateContacts, name='CreateContacts'),
    url(r'^viewcontact/(?P<pk>[0-9]+)/$', ViewContact, name='ViewContact'),
    path('contacttags/', ContactTag, name='ContactTag'),
    path('createcontacttags/', CreateContactTags, name='CreateContactTags'),
    path('contacttitles/', ContactTitles, name='ContactTitles'),
    path('viewappraisal/', ViewAppraisal, name='ViewAppraisal'),
    path('contracts/', Contracts, name='Contracts'),
    path('createcontracts/', createContracts, name='createContracts'),
    path('employeetransfer/', EmployeeTransfer, name='EmployeeTransfer'),
    path('recruitment/', Recruitment, name='Recruitment'),
    path('employeessettings/', EmployeesSettings, name='EmployeesSettings'),
    url(r'^contracttemplate/(?P<pk>[0-9]+)/$', ContractTemplate, name='ContractTemplate'),
    path('documents/', document, name='documents'),
    path('createdocuments/', Createdocuments, name='Createdocuments'),
    url(r'^editdoc/(?P<pk>[0-9]+)/$', Editdocuments, name='Editdoc'),
    path('notes/', Notes, name='Notes'),
    path('createnotes/', Createnotes, name='Createnotes'),
    url(r'^editnote/(?P<pk>[0-9]+)/$', Editnotes, name='Editnotes'),
    path('assets/', assets, name='Assets'),
    path('createassets/', Createassets, name='Createassets'),
    url(r'^editasset/(?P<pk>[0-9]+)/$', Editassets, name='Editasset'),
    path('delnotes/', delnotes, name='delnotes'),
    path('delassets/', delassets, name='delassets'),
    path('deldoc/', deldocument, name='deldoc'),
    path('delcontact/', delcontact, name='delcontact'),
    url(r'^editContract/(?P<pk>[0-9]+)/$', editContract, name='editContract'),
]
