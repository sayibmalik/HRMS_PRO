from django.contrib import admin
from .models import Product,PlanInclusion,PlanExclusions,Userdetails,Payments,Billingaddress,Bills,Support,UserMembership,PayHistory,Subscription
# Register your models here.

admin.site.register(Product)
admin.site.register(PlanInclusion)
admin.site.register(PlanExclusions)
admin.site.register(Userdetails)
admin.site.register(Payments)
admin.site.register(Billingaddress)
admin.site.register(Bills)
admin.site.register(Support)
admin.site.register(PayHistory)
admin.site.register(UserMembership)
admin.site.register(Subscription)