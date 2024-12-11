from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from Site.views import CreateCheckoutSessionView, ProductLandingPageView, stripe_webhook, SuccessView, CancelView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('home.urls')),
    path('meetings/', include('schedule.urls')),
    path('timesheets/', include('timesheets.urls')),
    path('Setting/', include('Setting.urls')),
    path('Project/', include('Project.urls')),
    path('Payroll/', include('Payroll.urls')),
    path('Leaves/', include('Leaves.urls')),
    path('HR/', include('HR.urls')),
    path('Employee/', include('Employee.urls')),
    path('Attendance/', include('Attendance.urls')),
    path('', include('Site.urls')),
    path('SelfServices/', include('SelfServices.urls')),
    path('Decisions/', include('Decisions.urls')),
    path('MuqeemServices/', include('MuqeemServices.urls')),
    path('Recruitment/', include('Recruitment.urls')),
    path('Training/', include('Training.urls')),
    path('Memos/', include('Memos.urls')),
    path('Policies/', include('Policies.urls')),
    path('Support/', include('Support.urls')),
    path('conf/', include('conf.urls')),
    path('webhooks/stripe/', stripe_webhook, name='stripe-webhook'),
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('Product-Landing-Page-View/', ProductLandingPageView, name='landing-page'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')

    # path('accounts/', include('allauth.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "Site.views.handle_not_found"
handler500 = "Site.views.handle_server_error"