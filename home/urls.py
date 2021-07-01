from django.urls import path, include
from .views import index, Blocks, Carousels, Forms, Pricing, calendar, CreateMeeting, Meetings, Industry, \
    CreateIndustry, Countries, FedStates, \
    CountryGroup, Banks, CreateBank, BankAccounts, CreateBankAccounts, Dashboard, DiscussInbox, DiscussGeneral, \
    GeneralPublicChannels, Badges, \
    createBadges, CreateChallenges, RegularizationCategory, CreateRegularizationCategory, Expenses, CreateExpenses, \
    MyReports, CreateReport, \
    ExpensesReportsToPay, CreateExpensesReportsToPay, AllExpenses, ExpensesReport, ExpensesProducts, \
    CreateExpensesProducts, ViewExpensesProducts, \
    Login, Signup, logout, Changelang, FreeSignUp, forgetpasscode,reset_password

from django.conf.urls import url

urlpatterns = [
    path('login/', Login, name='login'),
    path('logout/', logout, name='logout'),
    path('dashboard/', index, name='index'),
    path('signup/', Signup, name='signup'),
    path('blocks/', Blocks, name='Blocks'),
    path('carousels/', Carousels, name='Carousels'),
    path('forms/', Forms, name='Forms'),
    path('pricing/', Pricing, name='Pricing'),
    path('calendar/', calendar, name='calendar'),
    path('createmeeting/', CreateMeeting, name='CreateMeeting'),
    path('meetings/', Meetings, name='Meetings'),
    path('industry/', Industry, name='Industry'),
    path('createindustry/', CreateIndustry, name='CreateIndustry'),
    path('countries/', Countries, name='Countries'),
    path('fedstates/', FedStates, name='FedStates'),
    path('countrygroup/', CountryGroup, name='CountryGroup'),
    path('banks/', Banks, name='Banks'),
    path('createbank/', CreateBank, name='CreateBank'),
    path('bankaccounts/', BankAccounts, name='BankAccounts'),
    path('createbankaccounts/', CreateBankAccounts, name='CreateBankAccounts'),
    path('dashboard/', Dashboard, name='Dashboard'),
    path('discussinbox/', DiscussInbox, name='DiscussInbox'),
    path('discussgeneral/', DiscussGeneral, name='DiscussGeneral'),
    path('generalpublicchannels/', GeneralPublicChannels, name='GeneralPublicChannels'),
    path('badges/', Badges, name='Badges'),
    path('createbadges/', createBadges, name='createBadges'),
    path('createchallenges/', CreateChallenges, name='CreateChallenges'),
    path('regularizationcategory/', RegularizationCategory, name='RegularizationCategory'),
    path('createregularizationcategory/', CreateRegularizationCategory, name='CreateRegularizationCategory'),
    path('expenses/', Expenses, name='Expenses'),
    path('createexpenses/', CreateExpenses, name='CreateExpenses'),
    path('myreports/', MyReports, name='MyReports'),
    path('createreport/', CreateReport, name='CreateReport'),
    path('expensesreportstopay/', ExpensesReportsToPay, name='ExpensesReportsToPay'),
    path('createexpensesreportstopay/', CreateExpensesReportsToPay, name='CreateExpensesReportsToPay'),
    path('allexpenses/', AllExpenses, name='AllExpenses'),
    path('expensesreport/', ExpensesReport, name='ExpensesReport'),
    path('expensesproducts/', ExpensesProducts, name='ExpensesProducts'),
    path('createexpensesproducts/', CreateExpensesProducts, name='CreateExpensesProducts'),
    path('viewexpensesproducts/', ViewExpensesProducts, name='ViewExpensesProducts'),
    path('Changelang/', Changelang, name='Changelang'),
    path('FreeSignUp/', FreeSignUp, name='FreeSignUp'),
    path('forgetpasscode/', forgetpasscode, name='forgetpasscode'),
    path("reset_password", reset_password, name="reset_password"),


]
