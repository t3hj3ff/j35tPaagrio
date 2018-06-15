from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile


pMANAGE_STATUS = [
    ('Clan Leader','Clan Leader'),
    ('Party Leader','Party Leader'),
    ('Solo Player','Solo Player'),
]

class MyProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('User'),
                                related_name='my_profile',on_delete=models.CASCADE)
    favourite_snack = models.CharField(_('Interests'),
                                       max_length=255)
    status = models.CharField(max_length=255,null=True,blank=True,choices=pMANAGE_STATUS)
    account_balance = models.IntegerField(default=0)
    account_discount = models.IntegerField(default=0)
    account_bonus = models.DecimalField(default=0,decimal_places=4,max_digits=64)
