from django.shortcuts import render,redirect
from django.contrib.gis.geoip2 import GeoIP2
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from accounts.models import MyProfile
from payment.forms import paygol
from decimal import Decimal
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import MyProfile
from master_account.models import Accounts
from master_account.models import Characters
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.core.exceptions import ValidationError

from paymentwall import *
Paymentwall.set_api_type(Paymentwall.API_VC)
Paymentwall.set_app_key('485bea333b869aac46bbd6c763f8960f')
Paymentwall.set_secret_key('43f3ca58676da6089edb2727aa5eb962')
# Create your views here.

LANGUAGES = (
    ('en', _('English')),
    ('ka_GE', _('Georgian')),
    ('ru', _('Russian')),
)
def get_ip(request):
   xff = request.META.get('HTTP_X_FORWARDED_FOR')
   if xff:
      return xff.split(',')[0]
   return request.META.get('REMOTE_ADDR')


@login_required
def payment_index(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    user = request.user
    if request.user.is_authenticated:
        widget = Widget(
    	user.id, # id of the end-user who's making the payment
    	'p4_1',      # widget code, e.g. p1; can be picked inside of your merchant account
    	[],          # array of products - leave blank for Virtual Currency API
    	{'email': 'admin@paagr.io'} # additional parameters
        )
        return HttpResponseRedirect(widget.get_url())
    else:
        return HttpResponseRedirect("/")

@login_required
def paygol_ok(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    messages.info(request, 'Your Payment was SUCCESSFUL!')
    return HttpResponseRedirect("/cabinet")

@login_required
def paygol_fail(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    messages.info(request, 'Payment FAILED, Please Try Again...')
    return HttpResponseRedirect("/cabinet")

def paygol_ipn(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    secret_key = "14846f31-426a-11e8-b407-128b57940774"
    if secret_key != request.GET.get('key'):
        return HttpResponseRedirect("/cabinet")
    transaction_id = request.GET.get('transaction_id')
    service_id = request.GET.get('service_id')
    shortcode = request.GET.get('shortcode')
    keyword = request.GET.get('keyword')
    message = request.GET.get('message')
    sender = request.GET.get('sender')
    operator = request.GET.get('operator')
    country = request.GET.get('country')
    custom = request.GET.get('custom')
    price = request.GET.get('frmprice')
    currency = request.GET.get('currency')

    balance = MyProfile.objects.get(user_id=custom)
    finalprice = Decimal(price)
    balance.account_balance += finalprice
    balance.save()
    return HttpResponseRedirect("/")


@login_required
def paygol_payment(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    current_user = request.user.username
    qs = MyProfile.objects.get(user=request.user)
    active_user = request.user
    acc_obj = Accounts.objects.values("login","master_account")
    final = acc_obj.filter(login=request.user.id,master_account=active_user.id)
    pg_price = request.POST.get('pg_price')
    pg_custom = request.user.id
    return render(request,'payment/paygol.html',{'pg_price':pg_price,'pg_custom':pg_custom,"qs":qs,"slug":current_user,"final":final})

@login_required
def fillout_payment(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    current_user = request.user.username
    qs = MyProfile.objects.get(user=request.user)
    active_user = request.user
    acc_obj = Accounts.objects.values("login","master_account")
    final = acc_obj.filter(login=request.user.id,master_account=active_user.id)
    form = paygol()
    if form.is_valid():
        pg_price = form.cleaned_data.get("pg_price")
    return render(request,'payment/test.html',{'form':form,"qs":qs,"slug":current_user,"final":final})

def payment_pingback(request):
    ip = get_ip(request)
    g = GeoIP2()
    try:
        country = g.country(ip)
        if country["country_name"] == "Georgia":
            user_language = 'ka_GE'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
        elif country["country_name"] == "Russia" or country["country_name"] == "Ukraine" or country["country_name"] == "Belarus" or country["country_name"] == "Latvia" or country["country_name"] == "Lithuania" or country["country_name"] == "Moldova" or country["country_name"] == "Estonia":
            user_language = 'ru'
            translation.activate(user_language)
            response = HttpResponse()
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    except:
        pass
    test = request.GET.dict()
    test2 = request.GET.get('uid')

    pingback = Pingback(test, request.META['REMOTE_ADDR'])

    if pingback.validate():
        virtual_currency = pingback.get_vc_amount()
        if pingback.is_deliverable():
            # deliver the virtual currency
            print('OK')
        elif pingback.is_cancelable():
            # withdraw the virtual currency
            pass
            print('Fail') # Paymentwall expects response to be OK, otherwise the pingback will be resent
    else:
        print(pingback.get_error_summary())
    return render(request,'payment/pingback.html')
