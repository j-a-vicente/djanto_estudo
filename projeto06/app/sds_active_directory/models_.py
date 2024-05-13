# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdComputer(models.Model):
    id_ad_computer = models.AutoField()
    sid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    dnshostname = models.TextField(blank=True, null=True)
    samaccountname = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objectcategory = models.TextField(blank=True, null=True)
    objectclass = models.TextField(blank=True, null=True)
    operatingsystem = models.TextField(blank=True, null=True)
    operatingsystemversion = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    lastlogontimestamp = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_computer'
        app_label = 'sds_active_directory'


class AdComputerDns(models.Model):
    id_ad_computer_dns = models.AutoField()
    sid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    iphost = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_computer_dns'
        app_label = 'sds_active_directory'


class AdContact(models.Model):
    id_ad_contact = models.AutoField()
    name = models.CharField(max_length=100, blank=True, null=True)
    displayname = models.CharField(max_length=100, blank=True, null=True)
    mailnickname = models.CharField(max_length=100, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    memberof = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    objectcategory = models.TextField(blank=True, null=True)
    objectclass = models.TextField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_contact'
        app_label = 'sds_active_directory'


class AdDomainController(models.Model):
    id_ad_domain_controller = models.AutoField()
    name = models.CharField(max_length=100, blank=True, null=True)
    dnshostname = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    operatingsystem = models.CharField(max_length=100, blank=True, null=True)
    operatingsystemversion = models.TextField(blank=True, null=True)
    serverreferencebl = models.TextField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_domain_controller'
        app_label = 'sds_active_directory'


class AdGpo(models.Model):
    id_ad_gpo = models.AutoField()
    cn = models.CharField(max_length=100, blank=True, null=True)
    displayname = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    showinadvancedviewonly = models.TextField(blank=True, null=True)
    versionnumber = models.BigIntegerField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_gpo'
        app_label = 'sds_active_directory'


class AdGroup(models.Model):
    id_ad_group = models.AutoField()
    objectsid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    samaccountname = models.TextField(blank=True, null=True)
    member = models.TextField(blank=True, null=True)
    memberof = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    objectcategory = models.TextField(blank=True, null=True)
    objectclass = models.TextField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_group'
        app_label = 'sds_active_directory'


class AdGroupUser(models.Model):
    id_ad_group_user = models.AutoField()
    groupmember = models.TextField(blank=True, null=True)
    samaccountname = models.TextField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_group_user'
        app_label = 'sds_active_directory'


class AdOu(models.Model):
    id_ad_ou = models.AutoField()
    name = models.TextField(blank=True, null=True)
    objectcategory = models.TextField(blank=True, null=True)
    objectclass = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_ou'
        app_label = 'sds_active_directory'


class AdUser(models.Model):
    id_ad_user = models.AutoField()
    objectsid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    displayname = models.TextField(blank=True, null=True)
    samaccountname = models.TextField(blank=True, null=True)
    mail = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    department = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    objectcategory = models.TextField(blank=True, null=True)
    objectclass = models.TextField(blank=True, null=True)
    employeetype = models.TextField(blank=True, null=True)
    company = models.TextField(blank=True, null=True)
    physicaldeliveryofficename = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    distinguishedname = models.TextField(blank=True, null=True)
    memberof = models.TextField(blank=True, null=True)
    whencreated = models.DateTimeField(blank=True, null=True)
    whenchanged = models.DateTimeField(blank=True, null=True)
    accountexpires = models.DateTimeField(blank=True, null=True)
    badpasswordtime = models.DateTimeField(blank=True, null=True)
    pwdlastset = models.DateTimeField(blank=True, null=True)
    lastlogontimestamp = models.DateTimeField(blank=True, null=True)
    lastlogon = models.DateTimeField(blank=True, null=True)
    badpwdcount = models.BigIntegerField(blank=True, null=True)
    lockouttime = models.BigIntegerField(blank=True, null=True)
    enabled = models.TextField(blank=True, null=True)  # This field type is a guess.
    useraccountcontrol = models.BigIntegerField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_user'
        app_label = 'sds_active_directory'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'sds_active_directory'
