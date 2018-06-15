"""paagrio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path,include
from .views import index,news_detail,statistics_pvp,statistics_pk
from payment.views import payment_index,payment_pingback,paygol_payment,fillout_payment,paygol_ipn,paygol_ok,paygol_fail
from master_account.views import cabinet,characters_detail,characters_manage
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('ოეე/', admin.site.urls),
    path('accounts/', include('userena.urls')),
    path('',index,name='index'),
    path('cabinet/',cabinet,name='cabinet'),
    re_path('cabinet/manage/(?P<slug>[\w-]+)/$',characters_detail,name="characters_detail"),
    re_path('cabinet/characters/(?P<slug1>[\w-]+)/(?P<slug2>[\w-]+)/$',characters_manage,name="characters_manage"),
    path('favicon.ico',RedirectView.as_view(url='/static_my_proj/assets/img/favicon.png')),
    re_path('news/(?P<slug>[\w-]+)/$',news_detail,name='news_detail'),
    path('payment/',payment_index,name="payment_index"),
    path('donate/choose/',paygol_payment,name="paygol_payment"),
    path('ok/',paygol_ok,name="paygol_ok"),
    path('fail/',paygol_fail,name="paygol_fail"),
    re_path(r'paygol/ipn',paygol_ipn,name="paygol_ipn"),
    path('donate/',fillout_payment,name="fillout_payment"),
    path('statistics/pvp',statistics_pvp,name="statistics"),
    path('statistics/pk',statistics_pk,name="statistics_pk"),
    re_path(r'pingback',payment_pingback,name="payment_pingback"),
    re_path(r'^messages/', include('userena.contrib.umessages.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
