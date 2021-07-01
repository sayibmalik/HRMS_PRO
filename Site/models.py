from django.db import models
from django.contrib.auth.models import User
from home.models import Employees, Company
from django.utils import timezone
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

import datetime
from datetime import timedelta
from datetime import datetime as dt

today = datetime.date.today()

#### User Payment History
class PayHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    paystack_charge_id = models.CharField(max_length=100, default='', blank=True)
    paystack_access_code = models.CharField(max_length=100, default='', blank=True)
    payment_for = models.ForeignKey('Product', on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    paid = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    MEMBERSHIP_CHOICES = (
        ('Advanced', 'Advanced'),  # Note that they are all capitalize//
        ('Medium', 'Medium'),
        ('Basic', 'Basic'),
    )
    PERIOD_DURATION = (
        ('Days', 'Days'),
        ('Week', 'Week'),
        ('Months', 'Months'),
    )
    price = models.IntegerField(default=0)
    artitle = models.CharField(max_length=5000)
    file = models.FileField(upload_to="product_files/", blank=True, null=True)
    url = models.URLField()
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100, default='Day', choices=PERIOD_DURATION)
    slug = models.SlugField(null=True, blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES, default='Basic', max_length=30)

    def __str__(self):
        return "{}".format(self.membership_type)

    def get_display_price(self):
        return "{0:2f}".format(self.price / 100)


class UserMembership(models.Model):
    user = models.OneToOneField(User, related_name='user_membership', on_delete=models.CASCADE)
    membership = models.ForeignKey(Product, related_name='user_membership', on_delete=models.SET_NULL, null=True)
    reference_code = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.user.username


# @receiver(post_save, sender=UserMembership)
# def create_subscription(sender, instance, *args, **kwargs):
#     if instance:
#         Subscription.objects.create(user_membership=instance,
#                                     expires_in=dt.now().date() + timedelta(days=instance.membership.duration_period))
#

#### User Subscription
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership, related_name='Subscription', on_delete=models.CASCADE,
                                        default=None)
    expires_in = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.username


# @receiver(post_save, sender=Subscription)
# def update_active(sender, instance, *args, **kwargs):
#     if instance.expires_in < today:
#         subscription = Subscription.objects.get(id=instance.id)
#         subscription.delete()
#

class PlanInclusion(models.Model):
    title = models.CharField(max_length=500)
    plan = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user)


class PlanExclusions(models.Model):
    title = models.CharField(max_length=5000)
    plan = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.user)


class Userdetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    whatsapp = models.IntegerField(max_length=500, null=True)
    token = models.CharField(max_length=500, null=True, blank=True)
    Balance = models.IntegerField(max_length=500, null=True)
    plan = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    joiningdate = models.DateField(null=True, blank=True)
    expirydate = models.DateField(null=True, blank=True)
    number = models.BigIntegerField(max_length=15, null=True)

    def __str__(self):
        return "{}".format(self.user)


payment_type = (
    ("1", "DebitCard"),
    ("2", "CreditCard"),
    ("3", "NetBanking"),
)


class Payments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_name = models.CharField(max_length=500, null=True)
    number = models.IntegerField(max_length=500, null=True, blank=True)
    Expiry = models.IntegerField(max_length=500, null=True, blank=True)
    IFSC = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.account_name)


Address_type = (
    ("1", "Current"), ("1", "Permanent"),
)


class Billingaddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=500, null=True, blank=True)
    zip_code = models.IntegerField(max_length=500, null=True, blank=True)
    City = models.CharField(max_length=500, null=True, blank=True)
    State = models.CharField(max_length=500, null=True, blank=True)
    Country = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.user)


class Bills(models.Model):
    user = models.ForeignKey(Company, on_delete=models.CASCADE)
    Code = models.CharField(max_length=500, null=True)
    Amount = models.IntegerField(max_length=500, null=True, blank=True)
    particular = models.CharField(max_length=5000)
    paidStatus = models.BooleanField(default=False)
    datee = models.DateField(default=timezone.now)

    def __str__(self):
        return "{}".format(self.user)


support_type = (
    ("1", "Sales"), ("2", "IT"),
)


class Support(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=500, null=True)
    email = models.CharField(max_length=500, null=True)
    Message = models.CharField(max_length=500, null=True, blank=True)
    number = models.IntegerField(max_length=500, null=True)

    def __str__(self):
        return "{}".format(self.user)
