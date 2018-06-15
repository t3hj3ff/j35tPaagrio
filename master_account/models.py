from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
import whirlpool
import base64
import hashlib

User = get_user_model

class Accounts(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=256, blank=True, null=True)
    lastactive = models.PositiveIntegerField(default=0)
    access_level = models.IntegerField(default=0)
    lastip = models.CharField(db_column='lastIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastserver = models.IntegerField(db_column='lastServer', blank=True, null=True, default=1)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=45,default="null@null")
    pay_stat = models.IntegerField(default=1)
    bonus = models.FloatField(default=0)
    bonus_expire = models.IntegerField(default=0)
    banexpires = models.IntegerField(db_column='banExpires',default=0)  # Field name made lowercase.
    allowips = models.CharField(db_column='AllowIPs', max_length=256,default="*")  # Field name made lowercase.
    points = models.IntegerField(default=0)
    lock_expire = models.IntegerField(default=0)
    activated = models.PositiveIntegerField(default=1)
    last_hwid = models.CharField(max_length=50, blank=True, null=True)
    master_account = models.BigIntegerField(blank=True, null=True)


    def set_password(self, password):
        self.password = make_password(password,None,'unsalted_md5')

    def whirlpool_hash(self,password):
        data = self.password
        encoded_password = data.encode('utf-8')
        wp = base64.b64encode(hashlib.sha1(encoded_password).digest()).decode('utf-8')
        self.password = wp

    def __str__(self):
        return self.login

    class Meta:
        managed = True
        db_table = 'accounts'

    def get_absolute_url(self):
        return reverse("characters_detail", kwargs={'slug':self.login})


class Characters(models.Model):
    account_name = models.CharField(max_length=45)
    obj_id = models.IntegerField(db_column='obj_Id', primary_key=True)  # Field name made lowercase.
    char_name = models.CharField(unique=True, max_length=35)
    face = models.PositiveIntegerField(blank=True, null=True)
    hairstyle = models.PositiveIntegerField(db_column='hairStyle', blank=True, null=True)  # Field name made lowercase.
    haircolor = models.PositiveIntegerField(db_column='hairColor', blank=True, null=True)  # Field name made lowercase.
    sex = models.IntegerField(blank=True, null=True)
    heading = models.IntegerField(blank=True, null=True)
    x = models.IntegerField(blank=True, null=True)
    y = models.IntegerField(blank=True, null=True)
    z = models.IntegerField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    pvpkills = models.IntegerField(blank=True, null=True)
    pkkills = models.IntegerField(blank=True, null=True)
    clanid = models.IntegerField(blank=True, null=True)
    createtime = models.PositiveIntegerField()
    deletetime = models.PositiveIntegerField()
    title = models.CharField(max_length=16, blank=True, null=True)
    rec_have = models.PositiveIntegerField()
    rec_left = models.PositiveIntegerField()
    rec_timeleft = models.IntegerField()
    accesslevel = models.IntegerField(blank=True, null=True)
    online = models.IntegerField(blank=True, null=True)
    onlinetime = models.PositiveIntegerField()
    lastaccess = models.PositiveIntegerField(db_column='lastAccess')  # Field name made lowercase.
    leaveclan = models.PositiveIntegerField()
    deleteclan = models.PositiveIntegerField()
    nochannel = models.IntegerField()
    pledge_type = models.SmallIntegerField()
    pledge_rank = models.PositiveIntegerField()
    lvl_joined_academy = models.PositiveIntegerField()
    apprentice = models.PositiveIntegerField()
    key_bindings = models.CharField(max_length=8192, blank=True, null=True)
    pcbangpoints = models.IntegerField(db_column='pcBangPoints')  # Field name made lowercase.
    vitality = models.PositiveSmallIntegerField()
    fame = models.IntegerField()
    bookmarks = models.PositiveIntegerField()
    hunt_bonus = models.SmallIntegerField(blank=True, null=True)
    hunt_timeleft = models.SmallIntegerField(blank=True, null=True)
    bot = models.IntegerField(blank=True, null=True)
    last_hwid = models.CharField(max_length=50, blank=True, null=True)
    fraction = models.SmallIntegerField()

    class Meta:
        managed = True
        db_table = 'characters'

    def __str__(self):
        return self.char_name

    def get_absolute_url(self):
        return reverse("characters_manage", kwargs={'slug2':self.obj_id,"slug1":self.account_name})
