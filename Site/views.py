from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.views import chklogin
from .models import Billingaddress, Userdetails, Bills, Product, PayHistory, UserMembership, Subscription
from home.models import Employees, Company
import json
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.views import View
import datetime
from datetime import timedelta
from datetime import datetime as dt
import requests
import json
from django.http import HttpResponseRedirect

today = datetime.date.today()

stripe.api_key = settings.STRIPE_SECRET_KEY


# Create your views here.

def index(request):
    if request.method   == "GET":
        request.session["lang"] = "EN"
        l = Product.objects.all()
        context = {"data": l}
        try:
            lang = request.GET["lang"]
        except:
            lang = 'AR'
            return render(request, 'Site/' + lang + '/index.html', context)
    elif request.method == "POST":
            name = request.POST["name"]
            email_from = request.POST["email"]
            subject = request.POST["subject"]
            msg = name + " | " + email_from + " | "  + request.POST["message"]
            et = [settings.EMAIL_HOST_USER, ]
            send_mail(subject,
                    msg,
                    settings.EMAIL_HOST_USER,
                    et,
                    fail_silently=False)

            return redirect('/')




def billing(request):
    return render(request, 'Site/EN/billing.html')


def UserDashboard(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            try:
                u = Userdetails.objects.get(user=uid)
                c = Company.objects.get(user=uid)
            except:
                return redirect('/app/dashboard/')
            context = {"Title": "User Dashboard | HRMS ", "data": u, "data1": c}
            return render(request, 'Site/EN/userdashboard.html', context)
    else:
        return redirect('/app/login')


def BillingAddress(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            b = Billingaddress.objects.filter(user=uid)
            u = Employees.objects.all()
            context = {"Title": "Gareeb | Create Billing Address", "data": b, "employees": u}
            return render(request, 'Site/EN/billingaddress.html', context)
    else:
        return redirect('/app/login')


def bills(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            if user.is_superuser == True:
                b = Bills.objects.all()
                context = {"data": b}
                return render(request, 'Site/EN/bills.html', context)
            else:
                e = Employees.objects.get(user=uid)
                c = Bills.objects.filter(user=e.company)
                context = {"data": c}
                return render(request, 'Site/EN/bills.html', context)
    else:
        return redirect('/app/login')


def Support(request):
    return render(request, 'Site/EN/Support.html')


def CreateBillingAddress(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            context = {"Title": "Gareeb | Create Billing Address", }
            return render(request, 'Site/EN/createbillingaddress.html', context)
        elif request.method == 'POST':
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            Address = request.POST['address']
            Zipcode = request.POST['zipcode']
            City = request.POST['city']
            State = request.POST['state']
            Country = request.POST['country']
            Billingaddress.objects.create(user=user, address=Address, zip_code=Zipcode, City=City, State=State,
                                          Country=Country)
            response = redirect('/Site/EN/billingaddress')
            return response
    else:
        return redirect('/app/login')


def CreateBill(request):
    c = chklogin(request)
    if c:
        if request.method == "GET":
            c = Company.objects.all()
            context = {"data": c}
            return render(request, 'Site/EN/createbill.html', context)
        elif request.method == "POST":
            usr = request.POST["user"]
            c = Company.objects.get(id=usr)
            code = request.POST["code"]
            date = request.POST["date"]
            amount = request.POST["amount"]
            particular = request.POST["particular"]
            try:
                paidstatus = request.POST["paidstatus"]
                if paidstatus == "on":
                    yes = True
                else:
                    yes = False
            except:
                yes = False
            Bills.objects.create(user=c, Code=code, datee=date, Amount=amount, particular=particular, paidStatus=yes)
        response = redirect('/bills')
        return response
    else:
        return redirect('/app/login')


def CreateSupport(request):
    return render(request, 'Site/EN/createsupport.html')


def upgradeplan(request):
    c = chklogin(request)
    if c:
        l = Product.objects.all()

        context = {"Title": "Upgarde Plan ", "data": l}
        return render(request, 'Site/EN/upgradeplan.html', context)
    else:
        return redirect('/app/login')


def mysubscription(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            try:
                u = Userdetails.objects.get(user=uid)
                c = Company.objects.get(user=uid)
                a = UserMembership.objects.get(user=uid)
            except:
                return redirect('/app/dashboard/')
            context = {"Title": "My Subscription", "data": u, "data1": c, "membership": a}
            return render(request, 'Site/EN/mysubscription.html', context)
    else:
        return redirect('/app/login')


def myprofile(request):
    c = chklogin(request)
    if c:
        if request.method == 'GET':
            uid = request.session["userid"]
            try:
                c = Employees.objects.get(user=uid)
            except:
                return redirect('/app/dashboard/')
            context = {"Title": "My Profile", "data1": c}
            return render(request, 'Site/EN/myprofile.html', context)
    else:
        return redirect('/app/login')


def changepassword(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            current = request.POST["cpwd"]
            new_pas = request.POST["npwd"]
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            check = user.check_password(current)
            if check == True:
                user.set_password(new_pas)
                user.save()
        context = {"Title": "Change Password", }
        return render(request, 'Site/EN/changepassword.html', context)
    else:
        return redirect('/app/login')


def payment(request):
    context = {"Title": "Payment"}
    return render(request, "Site/AR/payment.html", context)


def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['key'] = settings.STRIPE_PUBLISHABLE_KEY
    return context


def charge(request):
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount=1,
            currency='SAR',
            description='Payment Gateway',
            source=request.POST['stripToken']
        )
        return render(request, 'Site/AR/payment.html')


class SuccessView(TemplateView):
    template_name = "Site/AR/success.html"


class CancelView(TemplateView):
    template_name = "Site/AR/cancel.html"


def ProductLandingPageView(request):
    c = chklogin(request)
    if c:
        plan = request.GET.get('sub_plan')
        fetch_membership = Product.objects.filter(membership_type=plan).exists()
        if fetch_membership == False:
            return redirect('subscribe')
        product = Product.objects.get(membership_type=plan)
        context = {
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        }
        try:
            uid = request.session["userid"]
            user = User.objects.get(id=uid)
            PayHistory.objects.create(amount=product.price, payment_for=product, user=user, paid="True")
            u = UserMembership.objects.create(user=user, membership=product)
            Subscription.objects.create(user_membership=u,
                                        expires_in=dt.now().date() + timedelta(days=u.membership.duration))

            return render(request, "Site/AR/landing.html", context)
        except:
            return redirect('mysubscription')
    else:
        return redirect('/app/login')


def delMembership(request):
    c = chklogin(request)
    if c:
        if request.method == "POST":
            pk = request.POST["id"]
            c = UserMembership.objects.get(id=pk)
            c.delete()
            return redirect("upgradeplan")
            return redirect("upgradeplan")
    else:
        return redirect('/app/login')


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs["pk"]
        product = Product.objects.get(id=product_id)
        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.membership_type,
                            # 'images': ['https://i.imgur.com/EHyR2nP.png'],
                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "product_id": product.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )

        return JsonResponse({
            'id': checkout_session.id
        })


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        customer_email = session["customer_details"]["email"]
        product_id = session["metadata"]["product_id"]

        product = Product.objects.get(id=product_id)
        send_mail(
            subject="Here is your product",
            message=f"Thanks for your purchase. Here is the product you ordered. The URL is {product.url}",
            recipient_list=[customer_email],
            from_email=[settings.EMAIL_HOST_USER]
        )
    return HttpResponse(status=200)


def handle_not_found(request, exception):
    return render(request, 'Site/AR/not-found.html')


def handle_server_error(request):
    return render(request, 'Site/AR/server-error.html')
