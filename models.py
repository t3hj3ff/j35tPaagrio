# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Accounts(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    password = models.CharField(max_length=256, blank=True, null=True)
    lastactive = models.PositiveIntegerField()
    access_level = models.IntegerField()
    lastip = models.CharField(db_column='lastIP', max_length=15, blank=True, null=True)  # Field name made lowercase.
    lastserver = models.IntegerField(db_column='lastServer', blank=True, null=True)  # Field name made lowercase.
    comments = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=45)
    pay_stat = models.IntegerField()
    bonus = models.FloatField()
    bonus_expire = models.IntegerField()
    banexpires = models.IntegerField(db_column='banExpires')  # Field name made lowercase.
    allowips = models.CharField(db_column='AllowIPs', max_length=256)  # Field name made lowercase.
    points = models.IntegerField()
    lock_expire = models.IntegerField()
    activated = models.PositiveIntegerField()
    last_hwid = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'accounts'


class AccountsMyprofile(models.Model):
    mugshot = models.CharField(max_length=100)
    privacy = models.CharField(max_length=15)
    favourite_snack = models.CharField(max_length=255)
    user = models.ForeignKey('AuthUser', models.DO_NOTHING, unique=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    account_balance = models.IntegerField()
    account_discount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'accounts_myprofile'


class AiParams(models.Model):
    npc_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    param = models.CharField(max_length=25)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ai_params'
        unique_together = (('npc_id', 'param'),)


class AllyData(models.Model):
    ally_id = models.IntegerField(primary_key=True)
    ally_name = models.CharField(max_length=45, blank=True, null=True)
    leader_id = models.IntegerField()
    expelled_member = models.PositiveIntegerField()
    crest = models.CharField(max_length=192, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ally_data'


class Auction(models.Model):
    id = models.PositiveIntegerField()
    sellerid = models.IntegerField(db_column='sellerId')  # Field name made lowercase.
    sellername = models.CharField(db_column='sellerName', max_length=50)  # Field name made lowercase.
    sellerclanname = models.CharField(db_column='sellerClanName', max_length=50)  # Field name made lowercase.
    itemname = models.CharField(db_column='itemName', max_length=40)  # Field name made lowercase.
    startingbid = models.BigIntegerField(db_column='startingBid')  # Field name made lowercase.
    currentbid = models.BigIntegerField(db_column='currentBid')  # Field name made lowercase.
    enddate = models.DecimalField(db_column='endDate', max_digits=20, decimal_places=0)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auction'


class AuctionBid(models.Model):
    id = models.IntegerField()
    auctionid = models.IntegerField(db_column='auctionId', primary_key=True)  # Field name made lowercase.
    bidderid = models.IntegerField(db_column='bidderId')  # Field name made lowercase.
    biddername = models.CharField(db_column='bidderName', max_length=50)  # Field name made lowercase.
    clan_name = models.CharField(max_length=50)
    maxbid = models.BigIntegerField(db_column='maxBid')  # Field name made lowercase.
    time_bid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'auction_bid'
        unique_together = (('auctionid', 'bidderid'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AutoChat(models.Model):
    groupid = models.IntegerField(db_column='groupId', primary_key=True)  # Field name made lowercase.
    npcid = models.IntegerField(db_column='npcId')  # Field name made lowercase.
    chatdelay = models.IntegerField(db_column='chatDelay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_chat'
        unique_together = (('groupid', 'npcid'),)


class AutoChatText(models.Model):
    groupid = models.IntegerField(db_column='groupId', primary_key=True)  # Field name made lowercase.
    chattext = models.CharField(db_column='chatText', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'auto_chat_text'
        unique_together = (('groupid', 'chattext'),)


class BanHwid(models.Model):
    hwid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ban_hwid'


class BannedIps(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    admin = models.CharField(max_length=45, blank=True, null=True)
    expiretime = models.PositiveIntegerField()
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'banned_ips'


class Bans(models.Model):
    account_name = models.CharField(max_length=45, blank=True, null=True)
    obj_id = models.PositiveIntegerField(db_column='obj_Id')  # Field name made lowercase.
    baned = models.CharField(max_length=20, blank=True, null=True)
    unban = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=200, blank=True, null=True)
    gm = models.CharField(db_column='GM', max_length=35, blank=True, null=True)  # Field name made lowercase.
    endban = models.PositiveIntegerField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bans'


class BbsLottery(models.Model):
    count = models.BigIntegerField()
    type = models.CharField(max_length=86)
    name = models.CharField(max_length=86)

    class Meta:
        managed = False
        db_table = 'bbs_lottery'


class BbsNews(models.Model):
    type = models.IntegerField()
    title_ru = models.TextField()
    title_en = models.TextField()
    text_ru = models.TextField()
    text_en = models.TextField()
    info_ru = models.CharField(max_length=32)
    info_en = models.CharField(max_length=32)
    author = models.CharField(max_length=32)
    date = models.DateField()

    class Meta:
        managed = False
        db_table = 'bbs_news'


class Bonus(models.Model):
    obj_id = models.IntegerField(primary_key=True)
    account = models.CharField(max_length=45)
    bonus_name = models.CharField(max_length=30)
    bonus_value = models.FloatField()
    bonus_expire_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bonus'
        unique_together = (('obj_id', 'bonus_name'),)


class Castle(models.Model):
    id = models.PositiveIntegerField()
    name = models.CharField(primary_key=True, max_length=25)
    taxpercent = models.PositiveIntegerField(db_column='taxPercent')  # Field name made lowercase.
    treasury = models.BigIntegerField()
    siegedate = models.PositiveIntegerField(db_column='siegeDate')  # Field name made lowercase.
    siegedayofweek = models.PositiveIntegerField(db_column='siegeDayOfWeek')  # Field name made lowercase.
    siegehourofday = models.PositiveIntegerField(db_column='siegeHourOfDay')  # Field name made lowercase.
    townid = models.PositiveIntegerField(db_column='townId')  # Field name made lowercase.
    skills = models.CharField(max_length=32)
    flags = models.CharField(max_length=32)
    owndate = models.IntegerField(db_column='ownDate')  # Field name made lowercase.
    dominionlord = models.IntegerField(db_column='dominionLord')  # Field name made lowercase.
    setsiege = models.IntegerField(db_column='setSiege')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'castle'


class CastleManorProcure(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    crop_id = models.PositiveSmallIntegerField()
    can_buy = models.BigIntegerField()
    start_buy = models.BigIntegerField()
    price = models.BigIntegerField()
    reward_type = models.PositiveIntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'castle_manor_procure'
        unique_together = (('castle_id', 'crop_id', 'period'),)


class CastleManorProduction(models.Model):
    castle_id = models.PositiveIntegerField(primary_key=True)
    seed_id = models.PositiveSmallIntegerField()
    can_produce = models.BigIntegerField()
    start_produce = models.BigIntegerField()
    seed_price = models.BigIntegerField()
    period = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'castle_manor_production'
        unique_together = (('castle_id', 'seed_id', 'period'),)


class CharTemplates(models.Model):
    classid = models.IntegerField(db_column='ClassId', primary_key=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=20)  # Field name made lowercase.
    raceid = models.IntegerField(db_column='RaceId')  # Field name made lowercase.
    parent = models.PositiveIntegerField(blank=True, null=True)
    level = models.PositiveIntegerField(blank=True, null=True)
    str = models.IntegerField(db_column='STR')  # Field name made lowercase.
    con = models.IntegerField(db_column='CON')  # Field name made lowercase.
    dex = models.IntegerField(db_column='DEX')  # Field name made lowercase.
    field_int = models.IntegerField(db_column='_INT')  # Field name made lowercase. Field renamed because it started with '_'.
    wit = models.IntegerField(db_column='WIT')  # Field name made lowercase.
    men = models.IntegerField(db_column='MEN')  # Field name made lowercase.
    p_atk = models.IntegerField(db_column='P_ATK')  # Field name made lowercase.
    p_def = models.IntegerField(db_column='P_DEF')  # Field name made lowercase.
    m_atk = models.IntegerField(db_column='M_ATK')  # Field name made lowercase.
    m_def = models.IntegerField(db_column='M_DEF')  # Field name made lowercase.
    p_spd = models.IntegerField(db_column='P_SPD')  # Field name made lowercase.
    m_spd = models.IntegerField(db_column='M_SPD')  # Field name made lowercase.
    acc = models.IntegerField(db_column='ACC')  # Field name made lowercase.
    critical = models.IntegerField(db_column='CRITICAL')  # Field name made lowercase.
    evasion = models.IntegerField(db_column='EVASION')  # Field name made lowercase.
    run_spd = models.IntegerField(db_column='RUN_SPD')  # Field name made lowercase.
    walk_spd = models.IntegerField(db_column='WALK_SPD')  # Field name made lowercase.
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    cancraft = models.IntegerField(db_column='canCraft')  # Field name made lowercase.
    m_unk1 = models.DecimalField(db_column='M_UNK1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    m_unk2 = models.DecimalField(db_column='M_UNK2', max_digits=8, decimal_places=6)  # Field name made lowercase.
    m_col_r = models.DecimalField(db_column='M_COL_R', max_digits=3, decimal_places=1)  # Field name made lowercase.
    m_col_h = models.DecimalField(db_column='M_COL_H', max_digits=4, decimal_places=1)  # Field name made lowercase.
    f_unk1 = models.DecimalField(db_column='F_UNK1', max_digits=4, decimal_places=2)  # Field name made lowercase.
    f_unk2 = models.DecimalField(db_column='F_UNK2', max_digits=8, decimal_places=6)  # Field name made lowercase.
    f_col_r = models.DecimalField(db_column='F_COL_R', max_digits=3, decimal_places=1)  # Field name made lowercase.
    f_col_h = models.DecimalField(db_column='F_COL_H', max_digits=4, decimal_places=1)  # Field name made lowercase.
    items1 = models.IntegerField()
    items2 = models.IntegerField()
    items3 = models.IntegerField()
    items4 = models.IntegerField()
    items5 = models.IntegerField()
    p_atk_mod = models.FloatField(blank=True, null=True)
    m_atk_mod = models.FloatField(blank=True, null=True)
    p_def_mod = models.FloatField(blank=True, null=True)
    m_def_mod = models.FloatField(blank=True, null=True)
    m_atk_spd_mod = models.FloatField(blank=True, null=True)
    p_atk_spd_mod = models.FloatField(blank=True, null=True)
    m_atk_crit_chance_mod = models.FloatField(blank=True, null=True)
    p_atk_crit_chance_mod = models.FloatField(blank=True, null=True)
    p_critical_damage_per_mod = models.FloatField(blank=True, null=True)
    p_critical_damage_diff_mod = models.IntegerField(blank=True, null=True)
    hp_mod = models.FloatField(blank=True, null=True)
    mp_mod = models.FloatField(blank=True, null=True)
    p_critical_rate_mod = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'char_templates'


class CharacterBlocklist(models.Model):
    obj_id = models.IntegerField(db_column='obj_Id', primary_key=True)  # Field name made lowercase.
    target_id = models.IntegerField(db_column='target_Id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_blocklist'
        unique_together = (('obj_id', 'target_id'),)


class CharacterBookmarks(models.Model):
    char_id = models.IntegerField(db_column='char_Id', primary_key=True)  # Field name made lowercase.
    idx = models.PositiveIntegerField()
    name = models.CharField(max_length=32)
    acronym = models.CharField(max_length=4)
    icon = models.PositiveIntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_bookmarks'
        unique_together = (('char_id', 'idx'),)


class CharacterEffectsSave(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    skill_id = models.PositiveIntegerField()
    skill_level = models.PositiveIntegerField()
    effect_count = models.PositiveIntegerField()
    effect_cur_time = models.IntegerField()
    duration = models.IntegerField()
    order = models.IntegerField()
    class_index = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'character_effects_save'
        unique_together = (('char_obj_id', 'skill_id', 'class_index'),)


class CharacterFriends(models.Model):
    char_id = models.IntegerField(primary_key=True)
    friend_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_friends'
        unique_together = (('char_id', 'friend_id'),)


class CharacterHennas(models.Model):
    char_obj_id = models.IntegerField()
    symbol_id = models.PositiveIntegerField()
    slot = models.PositiveIntegerField()
    class_index = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'character_hennas'


class CharacterMacroses(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    id = models.PositiveSmallIntegerField()
    icon = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    descr = models.CharField(max_length=80, blank=True, null=True)
    acronym = models.CharField(max_length=4, blank=True, null=True)
    commands = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_macroses'
        unique_together = (('char_obj_id', 'id'),)


class CharacterMail(models.Model):
    obj_id = models.IntegerField()
    letterid = models.AutoField(db_column='letterId', primary_key=True)  # Field name made lowercase.
    senderid = models.IntegerField(db_column='senderId', blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(max_length=45, blank=True, null=True)
    recipientnames = models.CharField(db_column='recipientNames', max_length=45)  # Field name made lowercase.
    subject = models.TextField()
    message = models.TextField()
    senddate = models.DecimalField(db_column='sendDate', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    deletedate = models.DecimalField(db_column='deleteDate', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    unread = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_mail'


class CharacterPass(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    obj_id = models.IntegerField()
    question = models.CharField(max_length=45)
    answer = models.CharField(max_length=45)
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'character_pass'
        unique_together = (('login', 'obj_id'),)


class CharacterPostFriends(models.Model):
    object_id = models.IntegerField(primary_key=True)
    post_friend = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_post_friends'
        unique_together = (('object_id', 'post_friend'),)


class CharacterPremiumItems(models.Model):
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    itemnum = models.IntegerField(db_column='itemNum')  # Field name made lowercase.
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    itemcount = models.BigIntegerField(db_column='itemCount')  # Field name made lowercase.
    itemsender = models.CharField(db_column='itemSender', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'character_premium_items'


class CharacterQuests(models.Model):
    char_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_quests'
        unique_together = (('char_id', 'name', 'var'),)


class CharacterRecipebook(models.Model):
    char_id = models.IntegerField()
    id = models.PositiveSmallIntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'character_recipebook'
        unique_together = (('id', 'char_id'),)


class CharacterSecondaryPassword(models.Model):
    account_name = models.CharField(primary_key=True, max_length=45)
    var = models.CharField(max_length=20)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_secondary_password'
        unique_together = (('account_name', 'var'),)


class CharacterShortcuts(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    slot = models.PositiveIntegerField()
    page = models.PositiveIntegerField()
    type = models.PositiveIntegerField(blank=True, null=True)
    shortcut_id = models.IntegerField(blank=True, null=True)
    level = models.SmallIntegerField(blank=True, null=True)
    class_index = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'character_shortcuts'
        unique_together = (('char_obj_id', 'slot', 'page', 'class_index'),)


class CharacterSkills(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    skill_id = models.PositiveSmallIntegerField()
    skill_level = models.PositiveSmallIntegerField()
    skill_name = models.CharField(max_length=100, blank=True, null=True)
    class_index = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills'
        unique_together = (('char_obj_id', 'skill_id', 'class_index'),)


class CharacterSkillsSave(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    skill_id = models.BigIntegerField()
    class_index = models.SmallIntegerField()
    end_time = models.BigIntegerField()
    reuse_delay_org = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_skills_save'
        unique_together = (('char_obj_id', 'skill_id', 'class_index'),)


class CharacterSubclasses(models.Model):
    char_obj_id = models.IntegerField(primary_key=True)
    class_id = models.PositiveIntegerField()
    level = models.PositiveIntegerField()
    exp = models.BigIntegerField()
    sp = models.BigIntegerField()
    curhp = models.DecimalField(db_column='curHp', max_digits=11, decimal_places=4)  # Field name made lowercase.
    curmp = models.DecimalField(db_column='curMp', max_digits=11, decimal_places=4)  # Field name made lowercase.
    curcp = models.DecimalField(db_column='curCp', max_digits=11, decimal_places=4)  # Field name made lowercase.
    maxhp = models.PositiveIntegerField(db_column='maxHp')  # Field name made lowercase.
    maxmp = models.PositiveIntegerField(db_column='maxMp')  # Field name made lowercase.
    maxcp = models.PositiveIntegerField(db_column='maxCp')  # Field name made lowercase.
    active = models.IntegerField()
    isbase = models.IntegerField(db_column='isBase')  # Field name made lowercase.
    death_penalty = models.IntegerField()
    certification = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'character_subclasses'
        unique_together = (('char_obj_id', 'class_id'),)


class CharacterVariables(models.Model):
    obj_id = models.IntegerField()
    type = models.CharField(max_length=86)
    name = models.CharField(max_length=86)
    value = models.CharField(max_length=500)
    expire_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'character_variables'
        unique_together = (('obj_id', 'type', 'name'),)


class CharacterVote(models.Model):
    type = models.IntegerField()
    vote_id = models.IntegerField()
    date = models.BigIntegerField()
    id = models.IntegerField()
    nick = models.CharField(max_length=255)
    multipler = models.IntegerField()
    has_reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'character_vote'


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
        managed = False
        db_table = 'characters'


class ClanData(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    clan_name = models.CharField(max_length=45, blank=True, null=True)
    clan_level = models.PositiveIntegerField()
    hascastle = models.PositiveIntegerField(db_column='hasCastle')  # Field name made lowercase.
    hasfortress = models.PositiveIntegerField(db_column='hasFortress')  # Field name made lowercase.
    hashideout = models.PositiveIntegerField(db_column='hasHideout')  # Field name made lowercase.
    ally_id = models.IntegerField()
    leader_id = models.IntegerField()
    crest = models.CharField(max_length=256, blank=True, null=True)
    largecrest = models.CharField(max_length=8192, blank=True, null=True)
    reputation_score = models.IntegerField()
    warehouse = models.IntegerField()
    expelled_member = models.PositiveIntegerField()
    leaved_ally = models.PositiveIntegerField()
    dissolved_ally = models.PositiveIntegerField()
    auction_bid_at = models.IntegerField()
    airship = models.SmallIntegerField()
    point = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_data'


class ClanNotices(models.Model):
    clanid = models.IntegerField(db_column='clanID', primary_key=True)  # Field name made lowercase.
    notice = models.CharField(max_length=512)
    enabled = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'clan_notices'


class ClanPrivs(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    rank = models.IntegerField()
    privilleges = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_privs'
        unique_together = (('clan_id', 'rank'),)


class ClanSkills(models.Model):
    clan_id = models.IntegerField(primary_key=True)
    skill_id = models.PositiveSmallIntegerField()
    skill_level = models.PositiveIntegerField()
    skill_name = models.CharField(max_length=26, blank=True, null=True)
    squad_index = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'clan_skills'
        unique_together = (('clan_id', 'skill_id', 'squad_index'),)


class ClanSubpledges(models.Model):
    clan_id = models.PositiveIntegerField(primary_key=True)
    type = models.SmallIntegerField()
    name = models.CharField(max_length=45)
    leader_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'clan_subpledges'
        unique_together = (('clan_id', 'type'),)


class ClanWars(models.Model):
    clan1 = models.IntegerField()
    clan2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clan_wars'


class Clanhall(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    ownerid = models.IntegerField(db_column='ownerId')  # Field name made lowercase.
    lease = models.IntegerField()
    desc = models.TextField()
    location = models.CharField(max_length=15)
    paiduntil = models.BigIntegerField(db_column='paidUntil')  # Field name made lowercase.
    grade = models.PositiveIntegerField(db_column='Grade')  # Field name made lowercase.
    price = models.BigIntegerField()
    deposit = models.IntegerField()
    indebt = models.IntegerField(db_column='inDebt')  # Field name made lowercase.
    skills = models.CharField(max_length=32)
    siegedate = models.PositiveIntegerField(db_column='siegeDate')  # Field name made lowercase.
    siegedayofweek = models.PositiveIntegerField(db_column='siegeDayOfWeek')  # Field name made lowercase.
    siegehourofday = models.PositiveIntegerField(db_column='siegeHourOfDay')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clanhall'
        unique_together = (('id', 'name'),)


class ClassList(models.Model):
    class_name = models.CharField(max_length=19)
    id = models.PositiveIntegerField(primary_key=True)
    parent_id = models.IntegerField()
    parent_id2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'class_list'


class CommunitySkillsave(models.Model):
    charid = models.IntegerField(db_column='charId', blank=True, null=True)  # Field name made lowercase.
    schameid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    skills = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'community_skillsave'


class Communitybuff(models.Model):
    skillid = models.IntegerField(db_column='skillID', blank=True, null=True)  # Field name made lowercase.
    skilllvl = models.IntegerField(db_column='skillLvl', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'communitybuff'


class Comteleport(models.Model):
    tpid = models.AutoField(db_column='TpId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=45)
    charid = models.IntegerField(db_column='charId')  # Field name made lowercase.
    xpos = models.IntegerField(db_column='xPos')  # Field name made lowercase.
    ypos = models.IntegerField(db_column='yPos')  # Field name made lowercase.
    zpos = models.IntegerField(db_column='zPos')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comteleport'


class Couples(models.Model):
    id = models.IntegerField(primary_key=True)
    player1id = models.IntegerField(db_column='player1Id')  # Field name made lowercase.
    player2id = models.IntegerField(db_column='player2Id')  # Field name made lowercase.
    maried = models.CharField(max_length=5, blank=True, null=True)
    affianceddate = models.BigIntegerField(db_column='affiancedDate', blank=True, null=True)  # Field name made lowercase.
    weddingdate = models.BigIntegerField(db_column='weddingDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'couples'


class Craftcount(models.Model):
    char_id = models.PositiveIntegerField()
    item_id = models.PositiveSmallIntegerField()
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'craftcount'
        unique_together = (('char_id', 'item_id'),)


class CursedWeapons(models.Model):
    item_id = models.PositiveSmallIntegerField(primary_key=True)
    player_id = models.PositiveIntegerField()
    player_karma = models.PositiveIntegerField()
    player_pkkills = models.PositiveIntegerField()
    nb_kills = models.PositiveIntegerField()
    x = models.IntegerField()
    y = models.IntegerField()
    z = models.IntegerField()
    end_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'cursed_weapons'


class DdosIps(models.Model):
    ip = models.CharField(primary_key=True, max_length=15)
    admin = models.CharField(max_length=45, blank=True, null=True)
    expiretime = models.PositiveIntegerField()
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ddos_ips'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DominionRewards(models.Model):
    id = models.IntegerField(primary_key=True)
    object_id = models.IntegerField()
    static_badges = models.IntegerField()
    kill_reward = models.IntegerField()
    online_reward = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dominion_rewards'
        unique_together = (('id', 'object_id'),)


class Doors(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    pts_name = models.CharField(max_length=28)
    hp = models.PositiveIntegerField()
    pdef = models.PositiveIntegerField()
    mdef = models.PositiveIntegerField()
    unlockable = models.PositiveIntegerField()
    key = models.IntegerField()
    level = models.IntegerField()
    showhp = models.PositiveIntegerField(db_column='showHp')  # Field name made lowercase.
    posx = models.IntegerField()
    posy = models.IntegerField()
    posz = models.IntegerField()
    ax = models.IntegerField()
    ay = models.IntegerField()
    bx = models.IntegerField()
    by = models.IntegerField()
    cx = models.IntegerField()
    cy = models.IntegerField()
    dx = models.IntegerField()
    dy = models.IntegerField()
    minz = models.IntegerField()
    maxz = models.IntegerField()
    siege_weapon = models.CharField(max_length=5)
    geodata = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'doors'


class Dropcount(models.Model):
    char_id = models.PositiveIntegerField()
    item_id = models.PositiveSmallIntegerField()
    count = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dropcount'
        unique_together = (('char_id', 'item_id'),)


class Droplist(models.Model):
    mobid = models.PositiveIntegerField(db_column='mobId')  # Field name made lowercase.
    itemid = models.PositiveIntegerField(db_column='itemId')  # Field name made lowercase.
    min = models.BigIntegerField()
    max = models.BigIntegerField()
    sweep = models.PositiveIntegerField()
    chance = models.PositiveIntegerField()
    category = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'droplist'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.ForeignKey(EasyThumbnailsThumbnail, models.DO_NOTHING, unique=True)
    width = models.PositiveIntegerField(blank=True, null=True)
    height = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class EpicBossSpawn(models.Model):
    bossid = models.PositiveSmallIntegerField(db_column='bossId', primary_key=True)  # Field name made lowercase.
    respawndate = models.IntegerField(db_column='respawnDate')  # Field name made lowercase.
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'epic_boss_spawn'


class Fish(models.Model):
    id = models.IntegerField(primary_key=True)
    level = models.IntegerField()
    name = models.CharField(max_length=40)
    hp = models.IntegerField()
    hpregen = models.IntegerField()
    fish_type = models.IntegerField()
    fish_group = models.IntegerField()
    fish_guts = models.IntegerField()
    guts_check_time = models.IntegerField()
    wait_time = models.IntegerField()
    combat_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fish'
        unique_together = (('id', 'level'),)


class Fishreward(models.Model):
    fishid = models.IntegerField(primary_key=True)
    rewardid = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()
    chance = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'fishreward'
        unique_together = (('fishid', 'rewardid'),)


class Forts(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    lastsiegedate = models.IntegerField(db_column='lastSiegeDate')  # Field name made lowercase.
    siegedate = models.IntegerField(db_column='siegeDate')  # Field name made lowercase.
    skills = models.CharField(max_length=32)
    owndate = models.IntegerField(db_column='ownDate')  # Field name made lowercase.
    state = models.PositiveIntegerField()
    castleid = models.PositiveIntegerField(db_column='castleId')  # Field name made lowercase.
    mercenaryid = models.IntegerField(db_column='mercenaryId')  # Field name made lowercase.
    mercenaryloc = models.CharField(db_column='mercenaryLoc', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'forts'


class Forums(models.Model):
    forum_id = models.IntegerField(unique=True)
    forum_name = models.CharField(max_length=255)
    forum_parent = models.IntegerField()
    forum_post = models.IntegerField()
    forum_type = models.IntegerField()
    forum_perm = models.IntegerField()
    forum_owner_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'forums'


class FourSepulchersSpawnlist(models.Model):
    location = models.CharField(max_length=19)
    count = models.IntegerField()
    npc_templateid = models.IntegerField()
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    randomx = models.IntegerField()
    randomy = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()
    key_npc_id = models.IntegerField()
    spawntype = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'four_sepulchers_spawnlist'


class GameLog(models.Model):
    serv_id = models.PositiveIntegerField()
    act_time = models.PositiveIntegerField()
    log_id = models.PositiveSmallIntegerField()
    actor = models.PositiveIntegerField()
    actor_type = models.CharField(max_length=75)
    target = models.PositiveIntegerField()
    target_type = models.CharField(max_length=75)
    location_x = models.IntegerField(blank=True, null=True)
    location_y = models.IntegerField(blank=True, null=True)
    location_z = models.SmallIntegerField(blank=True, null=True)
    etc_str1 = models.CharField(max_length=50, blank=True, null=True)
    etc_str2 = models.CharField(max_length=50, blank=True, null=True)
    etc_str3 = models.CharField(max_length=50, blank=True, null=True)
    etc_num1 = models.IntegerField()
    etc_num2 = models.IntegerField()
    etc_num3 = models.IntegerField()
    etc_num4 = models.IntegerField()
    etc_num5 = models.IntegerField()
    etc_num6 = models.IntegerField()
    etc_num7 = models.IntegerField()
    etc_num8 = models.IntegerField()
    etc_num9 = models.BigIntegerField()
    etc_num10 = models.BigIntegerField()
    str_actor = models.CharField(db_column='STR_actor', max_length=50, blank=True, null=True)  # Field name made lowercase.
    str_actor_account = models.CharField(db_column='STR_actor_account', max_length=50, blank=True, null=True)  # Field name made lowercase.
    str_target = models.CharField(db_column='STR_target', max_length=50, blank=True, null=True)  # Field name made lowercase.
    str_target_account = models.CharField(db_column='STR_target_account', max_length=50, blank=True, null=True)  # Field name made lowercase.
    item_id = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'game_log'


class Games(models.Model):
    id = models.IntegerField(primary_key=True)
    idnr = models.IntegerField()
    number1 = models.IntegerField()
    number2 = models.IntegerField()
    prize = models.BigIntegerField()
    newprize = models.BigIntegerField()
    prize1 = models.BigIntegerField()
    prize2 = models.BigIntegerField()
    prize3 = models.BigIntegerField()
    enddate = models.DecimalField(max_digits=20, decimal_places=0)
    finished = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'games'
        unique_together = (('id', 'idnr'),)


class GlobalTasks(models.Model):
    task = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    last_activation = models.IntegerField()
    param1 = models.CharField(max_length=100)
    param2 = models.CharField(max_length=100)
    param3 = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'global_tasks'


class GuardianGroupobjectpermission(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_groupobjectpermission'
        unique_together = (('group', 'permission', 'object_pk'),)


class GuardianUserobjectpermission(models.Model):
    object_pk = models.CharField(max_length=255)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'guardian_userobjectpermission'
        unique_together = (('user', 'permission', 'object_pk'),)


class HardwareLimits(models.Model):
    hardware = models.CharField(primary_key=True, max_length=255)
    windows_limit = models.SmallIntegerField()
    limit_expire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hardware_limits'


class Hellbound(models.Model):
    name = models.PositiveIntegerField(primary_key=True)
    hb_points = models.PositiveIntegerField()
    hb_level = models.PositiveIntegerField()
    unlocked = models.PositiveIntegerField()
    dummy = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'hellbound'
        unique_together = (('name', 'hb_points', 'hb_level', 'unlocked', 'dummy'),)


class Henna(models.Model):
    symbol_id = models.PositiveIntegerField(primary_key=True)
    symbol_name = models.CharField(max_length=15, blank=True, null=True)
    dye_id = models.PositiveSmallIntegerField()
    dye_amount = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    stat_int = models.IntegerField(db_column='stat_INT')  # Field name made lowercase.
    stat_str = models.IntegerField(db_column='stat_STR')  # Field name made lowercase.
    stat_con = models.IntegerField(db_column='stat_CON')  # Field name made lowercase.
    stat_mem = models.IntegerField(db_column='stat_MEM')  # Field name made lowercase.
    stat_dex = models.IntegerField(db_column='stat_DEX')  # Field name made lowercase.
    stat_wit = models.IntegerField(db_column='stat_WIT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'henna'


class HennaTrees(models.Model):
    class_id = models.SmallIntegerField(primary_key=True)
    symbol_id = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'henna_trees'
        unique_together = (('class_id', 'symbol_id'),)


class Heroes(models.Model):
    char_id = models.IntegerField(primary_key=True)
    count = models.PositiveIntegerField()
    played = models.IntegerField()
    active = models.IntegerField()
    message = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'heroes'


class HeroesDiary(models.Model):
    charid = models.PositiveIntegerField(db_column='charId')  # Field name made lowercase.
    time = models.BigIntegerField()
    action = models.PositiveIntegerField()
    param = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'heroes_diary'


class HwidLock(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    hwid = models.TextField()

    class Meta:
        managed = False
        db_table = 'hwid_lock'


class ItemAttributes(models.Model):
    itemid = models.IntegerField(db_column='itemId', primary_key=True)  # Field name made lowercase.
    augattributes = models.IntegerField(db_column='augAttributes')  # Field name made lowercase.
    augskillid = models.IntegerField(db_column='augSkillId')  # Field name made lowercase.
    augskilllevel = models.IntegerField(db_column='augSkillLevel')  # Field name made lowercase.
    elemtype = models.IntegerField(db_column='elemType')  # Field name made lowercase.
    elemvalue = models.IntegerField(db_column='elemValue')  # Field name made lowercase.
    elem0 = models.IntegerField()
    elem1 = models.IntegerField()
    elem2 = models.IntegerField()
    elem3 = models.IntegerField()
    elem4 = models.IntegerField()
    elem5 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'item_attributes'


class ItemAuction(models.Model):
    auctionid = models.IntegerField(db_column='auctionId', primary_key=True)  # Field name made lowercase.
    instanceid = models.IntegerField(db_column='instanceId')  # Field name made lowercase.
    auctionitemid = models.IntegerField(db_column='auctionItemId')  # Field name made lowercase.
    startingtime = models.BigIntegerField(db_column='startingTime')  # Field name made lowercase.
    endingtime = models.BigIntegerField(db_column='endingTime')  # Field name made lowercase.
    auctionstateid = models.IntegerField(db_column='auctionStateId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_auction'


class ItemAuctionBid(models.Model):
    auctionid = models.IntegerField(db_column='auctionId', primary_key=True)  # Field name made lowercase.
    playerobjid = models.IntegerField(db_column='playerObjId')  # Field name made lowercase.
    playerbid = models.BigIntegerField(db_column='playerBid')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_auction_bid'
        unique_together = (('auctionid', 'playerobjid'),)


class ItemMall(models.Model):
    ord = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    itemid = models.IntegerField(db_column='itemId')  # Field name made lowercase.
    count = models.IntegerField()
    price = models.IntegerField()
    icategory2 = models.IntegerField(db_column='iCategory2')  # Field name made lowercase.
    onsale = models.IntegerField(db_column='onSale')  # Field name made lowercase.
    istartsale = models.IntegerField(db_column='iStartSale')  # Field name made lowercase.
    iendsale = models.IntegerField(db_column='iEndSale')  # Field name made lowercase.
    istarthour = models.IntegerField(db_column='iStartHour')  # Field name made lowercase.
    istartmin = models.IntegerField(db_column='iStartMin')  # Field name made lowercase.
    iendhour = models.IntegerField(db_column='iEndHour')  # Field name made lowercase.
    iendmin = models.IntegerField(db_column='iEndMin')  # Field name made lowercase.
    istock = models.IntegerField(db_column='iStock')  # Field name made lowercase.
    imaxstock = models.IntegerField(db_column='iMaxStock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item_mall'
        unique_together = (('ord', 'itemid'),)


class Itemall(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    reuse = models.PositiveIntegerField()
    magic_weapon = models.SmallIntegerField()
    is_olympiad_can_use = models.PositiveIntegerField()
    immediate_effect = models.IntegerField()
    ex_immediate_effect = models.IntegerField()
    delay_share_group = models.IntegerField()
    is_premium = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'itemall'


class Items(models.Model):
    object_id = models.IntegerField(primary_key=True)
    owner_id = models.IntegerField()
    item_id = models.PositiveSmallIntegerField()
    visual_item_id = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=100, blank=True, null=True)
    count = models.BigIntegerField()
    enchant_level = models.PositiveSmallIntegerField()
    visual_enchant_level = models.SmallIntegerField()
    class_field = models.CharField(db_column='class', max_length=10)  # Field renamed because it was a Python reserved word.
    loc = models.CharField(max_length=13)
    loc_data = models.IntegerField(blank=True, null=True)
    custom_type1 = models.PositiveSmallIntegerField()
    custom_type2 = models.PositiveSmallIntegerField()
    shadow_life_time = models.IntegerField()
    flags = models.IntegerField()
    energy = models.PositiveIntegerField()
    temporal = models.CharField(max_length=5)
    enchant_time = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'items'


class ItemsDelayed(models.Model):
    payment_id = models.AutoField(primary_key=True)
    owner_id = models.IntegerField()
    item_id = models.PositiveSmallIntegerField()
    count = models.PositiveIntegerField()
    enchant_level = models.PositiveSmallIntegerField()
    attribute = models.SmallIntegerField()
    attribute_level = models.SmallIntegerField()
    elem0 = models.SmallIntegerField()
    elem1 = models.SmallIntegerField()
    elem2 = models.SmallIntegerField()
    elem3 = models.SmallIntegerField()
    elem4 = models.SmallIntegerField()
    elem5 = models.SmallIntegerField()
    flags = models.IntegerField()
    payment_status = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items_delayed'


class JfBanIp(models.Model):
    type = models.CharField(max_length=255)
    ip = models.CharField(max_length=20)
    time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jf_ban_ip'


class JfLog(models.Model):
    ip = models.CharField(max_length=255)
    date = models.DateTimeField()
    nick = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    param = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'jf_log'


class JfPlayerReuze(models.Model):
    type = models.CharField(max_length=45)
    player_id = models.CharField(max_length=20)
    time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'jf_player_reuze'


class JfReuzeIp(models.Model):
    type = models.TextField()
    ip = models.TextField()
    time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'jf_reuze_ip'


class Killcount(models.Model):
    char_id = models.IntegerField()
    npc_id = models.PositiveSmallIntegerField()
    count = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'killcount'
        unique_together = (('char_id', 'npc_id'),)


class LastimperialtombSpawnlist(models.Model):
    count = models.IntegerField()
    npc_templateid = models.IntegerField(primary_key=True)
    locx = models.IntegerField()
    locy = models.IntegerField()
    locz = models.IntegerField()
    heading = models.IntegerField()
    respawn_delay = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lastimperialtomb_spawnlist'
        unique_together = (('npc_templateid', 'locx', 'locy', 'locz'),)


class LevelRewards(models.Model):
    objectid = models.IntegerField(db_column='objectId', primary_key=True)  # Field name made lowercase.
    classid = models.IntegerField(db_column='classId')  # Field name made lowercase.
    classlevel = models.IntegerField(db_column='classLevel')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'level_rewards'
        unique_together = (('objectid', 'classid', 'classlevel'),)


class Locations(models.Model):
    loc_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    loc_x = models.IntegerField()
    loc_y = models.IntegerField()
    loc_zmin = models.IntegerField()
    loc_zmax = models.IntegerField()
    radius = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'locations'
        unique_together = (('loc_id', 'loc_x', 'loc_y'),)


class Lock(models.Model):
    login = models.CharField(primary_key=True, max_length=45)
    type = models.CharField(max_length=4)
    string = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'lock'
        unique_together = (('login', 'string'),)


class LoginservLog(models.Model):
    act_time = models.PositiveIntegerField()
    log_id = models.PositiveSmallIntegerField()
    etc_str1 = models.CharField(max_length=50, blank=True, null=True)
    etc_str2 = models.CharField(max_length=50, blank=True, null=True)
    etc_str3 = models.CharField(max_length=100, blank=True, null=True)
    etc_num1 = models.IntegerField()
    etc_num2 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'loginserv_log'


class Lvlupgain(models.Model):
    classid = models.IntegerField(primary_key=True)
    defaulthpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaulthpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaulthpmod = models.DecimalField(max_digits=4, decimal_places=2)
    defaultcpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaultcpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaultcpmod = models.DecimalField(max_digits=4, decimal_places=2)
    defaultmpbase = models.DecimalField(max_digits=5, decimal_places=1)
    defaultmpadd = models.DecimalField(max_digits=4, decimal_places=2)
    defaultmpmod = models.DecimalField(max_digits=4, decimal_places=2)
    class_lvl = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lvlupgain'


class Mail(models.Model):
    messageid = models.AutoField(db_column='messageId', primary_key=True)  # Field name made lowercase.
    sender = models.PositiveIntegerField()
    receiver = models.PositiveIntegerField()
    expire = models.DateTimeField()
    topic = models.CharField(max_length=30)
    body = models.TextField()
    attachments = models.PositiveIntegerField()
    needspayment = models.PositiveIntegerField(db_column='needsPayment')  # Field name made lowercase.
    price = models.BigIntegerField()
    system = models.PositiveIntegerField()
    unread = models.PositiveIntegerField()
    hidesender = models.PositiveIntegerField(db_column='hideSender')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mail'


class MailAttachments(models.Model):
    messageid = models.PositiveIntegerField(db_column='messageId', primary_key=True)  # Field name made lowercase.
    itemid = models.PositiveIntegerField(db_column='itemId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mail_attachments'
        unique_together = (('messageid', 'itemid'),)


class Mapregion(models.Model):
    y10_plus = models.IntegerField(primary_key=True)
    x11 = models.IntegerField()
    x12 = models.IntegerField()
    x13 = models.IntegerField()
    x14 = models.IntegerField()
    x15 = models.IntegerField()
    x16 = models.IntegerField()
    x17 = models.IntegerField()
    x18 = models.IntegerField()
    x19 = models.IntegerField()
    x20 = models.IntegerField()
    x21 = models.IntegerField()
    x22 = models.IntegerField()
    x23 = models.IntegerField()
    x24 = models.IntegerField()
    x25 = models.IntegerField()
    x26 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mapregion'


class MerchantAreasList(models.Model):
    merchant_area_id = models.PositiveIntegerField(primary_key=True)
    merchant_area_name = models.CharField(max_length=25)
    tax = models.FloatField()
    chaotic = models.IntegerField(db_column='Chaotic')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'merchant_areas_list'


class Minions(models.Model):
    boss_id = models.IntegerField(primary_key=True)
    minion_id = models.IntegerField()
    amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'minions'
        unique_together = (('boss_id', 'minion_id'),)


class MultisellLog(models.Model):
    id = models.PositiveIntegerField()
    date = models.CharField(max_length=2048)
    itemid = models.CharField(db_column='itemId', max_length=2048)  # Field name made lowercase.
    count = models.CharField(max_length=2048)
    ditemid = models.CharField(db_column='dItemId', max_length=2048)  # Field name made lowercase.
    dcount = models.CharField(db_column='dCount', max_length=2048)  # Field name made lowercase.
    name = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'multisell_log'


class NewsNews(models.Model):
    title = models.CharField(max_length=65)
    text = models.TextField()
    type = models.CharField(max_length=10)
    timestamp = models.DateTimeField()
    post_language = models.CharField(max_length=255, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    text_ka = models.TextField()
    text_ru = models.TextField()
    title_ka = models.CharField(max_length=65)
    title_ru = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'news_news'


class Npc(models.Model):
    ordinal = models.PositiveSmallIntegerField()
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=35)
    class_field = models.CharField(db_column='class', max_length=50, blank=True, null=True)  # Field renamed because it was a Python reserved word.
    race = models.CharField(max_length=45)
    collision_radius = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    collision_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    level = models.IntegerField()
    sex = models.CharField(max_length=6)
    type = models.CharField(max_length=30)
    ai_type = models.CharField(max_length=50)
    attackrange = models.IntegerField()
    hp = models.IntegerField()
    base_hp_regen = models.FloatField()
    mp = models.IntegerField()
    base_mp_regen = models.FloatField()
    str = models.IntegerField()
    con = models.IntegerField()
    dex = models.IntegerField()
    int = models.IntegerField()
    wit = models.IntegerField()
    men = models.IntegerField()
    exp = models.IntegerField()
    sp = models.IntegerField()
    patk = models.IntegerField()
    pdef = models.IntegerField()
    matk = models.IntegerField()
    mdef = models.IntegerField()
    atkspd = models.IntegerField()
    aggro = models.IntegerField()
    matkspd = models.IntegerField()
    rhand = models.IntegerField()
    lhand = models.IntegerField()
    armor = models.IntegerField()
    walkspd = models.IntegerField()
    runspd = models.IntegerField()
    faction_id = models.CharField(max_length=40)
    faction_range = models.IntegerField()
    displayid = models.IntegerField(db_column='displayId')  # Field name made lowercase.
    shield_defense_rate = models.IntegerField()
    shield_defense = models.IntegerField()
    corpse_time = models.IntegerField()
    base_rand_dam = models.IntegerField()
    base_critical = models.IntegerField()
    physical_hit_modify = models.IntegerField()
    base_reuse_delay = models.IntegerField()
    physical_avoid_modify = models.IntegerField()
    hit_time_factor = models.FloatField()
    isdropherbs = models.CharField(db_column='isDropHerbs', max_length=5)  # Field name made lowercase.
    shots = models.CharField(max_length=12)
    map_flag = models.IntegerField()
    boss_flag = models.IntegerField()
    agro_range = models.IntegerField()
    event_flag = models.IntegerField()
    can_be_attacked = models.IntegerField()
    undying = models.IntegerField()
    base_attack_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'npc'


class NpcBoss(models.Model):
    npc_db_name = models.CharField(primary_key=True, max_length=50)
    alive = models.SmallIntegerField(blank=True, null=True)
    hp = models.IntegerField()
    mp = models.IntegerField()
    pos_x = models.IntegerField()
    pos_y = models.IntegerField()
    pos_z = models.IntegerField()
    time_low = models.BigIntegerField()
    time_high = models.BigIntegerField()
    i0 = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npc_boss'


class NpcElement(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    atkelement = models.IntegerField(db_column='AtkElement')  # Field name made lowercase.
    elematkpower = models.IntegerField(db_column='elemAtkPower')  # Field name made lowercase.
    fireres = models.IntegerField(db_column='FireRes')  # Field name made lowercase.
    waterres = models.IntegerField(db_column='WaterRes')  # Field name made lowercase.
    windres = models.IntegerField(db_column='WindRes')  # Field name made lowercase.
    earthres = models.IntegerField(db_column='EarthRes')  # Field name made lowercase.
    holyres = models.IntegerField(db_column='HolyRes')  # Field name made lowercase.
    darkres = models.IntegerField(db_column='DarkRes')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'npc_element'


class Npcskills(models.Model):
    npcid = models.IntegerField(primary_key=True)
    skillid = models.IntegerField()
    level = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'npcskills'
        unique_together = (('npcid', 'skillid', 'level'),)
