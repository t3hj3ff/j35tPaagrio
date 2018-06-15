from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from .forms import ChildUser,ChildUserPasswordChange,TransferFunds
from master_account.models import Accounts
from django.contrib.auth.decorators import login_required
from accounts.models import MyProfile
from master_account.models import Accounts
from master_account.models import Characters
from django.http import HttpResponseRedirect,HttpResponseForbidden
from django.contrib import messages
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.geoip2 import GeoIP2
from django.core.exceptions import ValidationError
import whirlpool

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
def cabinet(request):
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
    current_user = request.user
    form = ChildUser(request.POST or None)
    if request.method == "POST":
        form = ChildUser(request.POST or None)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.password = form.cleaned_data['password']
            instance.password_confirm = form.cleaned_data['password_confirm']
            instance.whirlpool_hash(instance.password)
            instance.master_account = current_user.id
            instance.save()
            messages.info(request, 'Your Account has been created successfully!')
            return HttpResponseRedirect("/cabinet")


    qs = MyProfile.objects.get(user=request.user)
    child_accounts = Accounts.objects.filter(master_account=current_user.id)

    return render(request,"cabinet.html",{"form":form,"qs":qs,"child_accounts":child_accounts})

@login_required
def characters_detail(request,slug):
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
    current_user = slug
    active_user = request.user
    instance = Accounts.objects.get(login=slug)
    form = ChildUserPasswordChange(request.POST or None)
    if request.method == "POST":
        form = ChildUserPasswordChange(data=request.POST,instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.password = form.cleaned_data['password']
            instance.whirlpool_hash(instance.password)
            instance.save()
            messages.info(request, 'Your Password has been changed!')
            return HttpResponseRedirect("/cabinet")
    acc_obj = Accounts.objects.values("login","master_account")
    final = acc_obj.filter(login=slug,master_account=active_user.id)
    if not final:
        return HttpResponseRedirect("/cabinet")
    qs = MyProfile.objects.get(user=request.user)
    child_characters = Characters.objects.filter(account_name=slug)
    child_accounts = Accounts.objects.filter(master_account=active_user.id)
    return render(request,'change.html',{"qs":qs,"form":form,"child_accounts":child_accounts,"slug":current_user,"final":final,"characters":child_characters})

@login_required
def characters_manage(request,slug1,slug2):
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
    current_user = slug1
    qs = MyProfile.objects.get(user=request.user)
    active_user = request.user
    acc_obj = Accounts.objects.values("login","master_account")
    final = acc_obj.filter(login=slug1,master_account=active_user.id)
    if not final:
        return HttpResponseRedirect("/cabinet")
    gamoyeneba = MyProfile.objects.get(user=request.user)
    form = TransferFunds(request.POST or None)
    if form.is_valid():
        from django.db import connection
        amount = form.cleaned_data.get("amount")
        if amount > gamoyeneba.account_balance:
            messages.error(request, "ERROR!: Not Enough pCredits available!")
        else:
            character_name = slug2
            cursor = connection.cursor()
            check_query1 = cursor.execute("SELECT owner_id FROM items WHERE item_id = %s AND owner_id = %s AND loc = %s", (4037,character_name,'INVENTORY'))
            if check_query1 > 0:
                cursor.execute("UPDATE items SET count = count + %s WHERE item_id = %s AND owner_id = %s AND loc = %s", (amount,4037,character_name,'INVENTORY'))
            else:
                sql = cursor.execute("SELECT object_id FROM items ORDER BY object_id DESC LIMIT 1")
                result = cursor.fetchone()[0]
                cursor.execute(
                        'INSERT INTO items (owner_id, object_id, item_id, name, count, enchant_level, loc)'
                        'VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (character_name, result+1, 4037, 'Coin of Luck',amount, 0, 'INVENTORY'),
                    )
            gamoyeneba.account_balance -= amount
            gamoyeneba.save()
            messages.success(request, "SUCCESS!: pCredits have been successfully transfered to your character")
            return HttpResponseRedirect("/cabinet")
    return render(request,'char_manage.html',{"qs":qs,"slug":current_user,"final":final,"form":form})
