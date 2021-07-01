from django.urls import path
from .views import index ,billing, UserDashboard,BillingAddress,bills,Support,CreateBillingAddress,CreateBill,\
    CreateSupport,upgradeplan,mysubscription,myprofile,changepassword,payment,charge,delMembership

urlpatterns = [
    path('', index, name='site'),
    path('billing/', billing, name='billing'),
    path('userdashboard/', UserDashboard, name='UserDashboard'),
    path('billingaddress/', BillingAddress, name='BillingAddress'),
    path('bills/', bills, name='Bills'),
    path('Support/', Support, name='Support'),
    path('createbillingaddress/', CreateBillingAddress, name='CreateBillingAddress'),
    path('createbill/', CreateBill, name='CreateBill'),
    path('createsupport/', CreateSupport, name='CreateSupport'),
    path('upgradeplan/', upgradeplan, name='upgradeplan'),
    path('mysubscription/', mysubscription, name='mysubscription'),
    path('myprofile/', myprofile, name='myprofile'),
    path('changepassword/', changepassword, name='changepassword'),
    path("payment/", payment, name="payment"),
    path("charge/", charge, name="charge"),
    path("delMembership/", delMembership, name="delMembership"),

]
