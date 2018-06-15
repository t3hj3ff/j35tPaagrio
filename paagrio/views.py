from django.shortcuts import redirect,render
from django.contrib.gis.geoip2 import GeoIP2
from django.conf import settings
from django.http import HttpResponse
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from news.models import News
from .forms import SubmitIssueForm
from ratelimit.decorators import ratelimit

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


@ratelimit(key='ip', rate='25/m', block=True)
def index(request):
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
    qs = News.objects.all().order_by('-timestamp')[0:3]
    return render(request, "index.html", {
    "news":qs

    })

def news_detail(request,slug):
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
    qs = News.objects.filter(slug=slug)
    return render(request,"news_detail.html",{"qs":qs})

#bottom two needs to loop characters to display top pk/pvp limit 50 or [0:50]
def statistics_pvp(request):
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
    return render(request,"statistics_pvp.html")

def statistics_pk(request):
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
    return render(request,"statistics_pk.html")
