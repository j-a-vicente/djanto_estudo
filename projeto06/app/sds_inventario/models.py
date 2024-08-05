# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdTbComputer(models.Model):
    id_ad_computer = models.IntegerField(blank=True, null=True)
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
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ad_tb_computer'
        app_label = 'sds_inventario' 


class Disk(models.Model):
    id_disk = models.AutoField(primary_key=True)
    id_serverhost = models.ForeignKey('Serverhost', models.DO_NOTHING, db_column='id_serverhost')
    diskpath = models.CharField(max_length=250, blank=True, null=True)
    disksize = models.FloatField(blank=True, null=True)
    freespace = models.FloatField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disk'
        app_label = 'sds_inventario' 


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'sds_inventario' 


class Portconect(models.Model):
    id_portconect = models.AutoField(primary_key=True)
    id_serverhost = models.ForeignKey('Serverhost', models.DO_NOTHING, db_column='id_serverhost')
    ipaddress = models.CharField(max_length=250, blank=True, null=True)
    numberport = models.CharField(max_length=250, blank=True, null=True)
    port = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portconect'
        app_label = 'sds_inventario' 


class SccmTbServerHost(models.Model):
    id_server_host = models.IntegerField(blank=True, null=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    fabricante = models.CharField(max_length=50, blank=True, null=True)
    modelo = models.CharField(max_length=50, blank=True, null=True)
    hostname = models.CharField(max_length=256, blank=True, null=True)
    dominio = models.TextField(blank=True, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    machinetype = models.CharField(max_length=50, blank=True, null=True)
    chassi = models.CharField(max_length=50, blank=True, null=True)
    bioserialnumber = models.CharField(max_length=100, blank=True, null=True)
    os = models.CharField(max_length=256, blank=True, null=True)
    ospkversao = models.CharField(max_length=50, blank=True, null=True)
    osversao = models.CharField(max_length=50, blank=True, null=True)
    nserie = models.CharField(max_length=256, blank=True, null=True)
    totalphysicalmemory = models.IntegerField(blank=True, null=True)
    cpufabricante = models.CharField(max_length=50, blank=True, null=True)
    cpumodelo = models.CharField(max_length=100, blank=True, null=True)
    cpusockets = models.IntegerField(blank=True, null=True)
    corespersocket = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)
    clientsccm = models.CharField(max_length=50, blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sccm_tb_server_host'
        app_label = 'sds_inventario' 


class Serverhost(models.Model):
    id_serverhost = models.AutoField(primary_key=True)
    id_trilha = models.ForeignKey('Trilha', models.DO_NOTHING, db_column='id_trilha')
    hostname = models.CharField(max_length=60, blank=True, null=True)
    fisicovm = models.CharField(max_length=20, blank=True, null=True)
    sistemaoperaciona = models.CharField(max_length=200, blank=True, null=True)
    ipaddress = models.CharField(max_length=250, blank=True, null=True)
    portconect = models.CharField(max_length=10, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    versao = models.CharField(max_length=350, blank=True, null=True)
    cpu = models.BigIntegerField(blank=True, null=True)
    memoryram = models.BigIntegerField(blank=True, null=True)
    ad = models.BooleanField(blank=True, null=True)
    or_ad = models.BooleanField(blank=True, null=True)
    sccm = models.BooleanField(blank=True, null=True)
    or_sccm = models.BooleanField(blank=True, null=True)
    hv = models.BooleanField(blank=True, null=True)
    or_hv = models.BooleanField(blank=True, null=True)
    nx = models.BooleanField(blank=True, null=True)
    or_nx = models.BooleanField(blank=True, null=True)
    vw = models.BooleanField(blank=True, null=True)
    or_vw = models.BooleanField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    id_origem = models.CharField(max_length=255, blank=True, null=True)
    vmm = models.BooleanField(blank=True, null=True)
    or_vmm = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverhost'
        app_label = 'sds_inventario' 


class Trilha(models.Model):
    id_trilha = models.AutoField(primary_key=True)
    trilha = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilha'
        app_label = 'sds_inventario' 


class VmmTbTblWlcVminstance(models.Model):
    id_tbl_wlc_vminstance = models.IntegerField()
    vminstanceid = models.CharField(max_length=256, blank=True, null=True)
    vmid = models.CharField(max_length=256, blank=True, null=True)
    machineid = models.CharField(max_length=256, blank=True, null=True)
    vmaddition = models.CharField(blank=True, null=True)
    startaction = models.CharField(max_length=256, blank=True, null=True)
    stopaction = models.CharField(max_length=256, blank=True, null=True)
    runguestaccount = models.CharField(max_length=256, blank=True, null=True)
    computername = models.CharField(max_length=256, blank=True, null=True)
    delaystart = models.IntegerField(blank=True, null=True)
    vmclocation = models.CharField(blank=True, null=True)
    vsvlocation = models.CharField(blank=True, null=True)
    vsvsize = models.BigIntegerField(blank=True, null=True)
    usehardwareassist = models.CharField(max_length=60, blank=True, null=True)
    vmconfigmodifiedtime = models.DateTimeField(blank=True, null=True)
    vsvprocessorarchitecture = models.SmallIntegerField(blank=True, null=True)
    vsvprocessorstepping = models.CharField(max_length=256, blank=True, null=True)
    vsvprocessormanufacturer = models.CharField(max_length=256, blank=True, null=True)
    vsvvirtualserverversion = models.CharField(max_length=256, blank=True, null=True)
    objectid = models.CharField(max_length=256, blank=True, null=True)
    vmtotalsize = models.BigIntegerField(blank=True, null=True)
    vmtotalmaxsize = models.BigIntegerField(blank=True, null=True)
    haspassthroughdisk = models.CharField(max_length=60, blank=True, null=True)
    virtualizationplatform = models.IntegerField(blank=True, null=True)
    sanstatus = models.TextField(blank=True, null=True)
    cpuutilization = models.IntegerField(blank=True, null=True)
    cputieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    memorytieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    diskbytesreadtieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    diskbyteswritetieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    networkbytesreadtieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    networkbyteswritetieredperfcounterid = models.CharField(max_length=256, blank=True, null=True)
    lunid = models.CharField(max_length=256, blank=True, null=True)
    vmresourcegroupid = models.CharField(max_length=256, blank=True, null=True)
    vmresourcegroup = models.CharField(blank=True, null=True)
    vmresource = models.CharField(blank=True, null=True)
    vmconfigresource = models.CharField(blank=True, null=True)
    diskresources = models.CharField(max_length=2048, blank=True, null=True)
    unsupportedreason = models.CharField(max_length=2048, blank=True, null=True)
    refreshererrors = models.CharField(max_length=2048, blank=True, null=True)
    virtualmachinestate = models.IntegerField(blank=True, null=True)
    drerrors = models.CharField(max_length=2048, blank=True, null=True)
    drstate = models.IntegerField()
    parentid = models.CharField(max_length=256, blank=True, null=True)
    creationsource = models.CharField(max_length=2048, blank=True, null=True)
    srcobjecttype = models.IntegerField(blank=True, null=True)
    rootvminstanceid = models.CharField(max_length=2048, blank=True, null=True)
    osshutdown = models.CharField(max_length=60, blank=True, null=True)
    timesynchronization = models.CharField(max_length=60, blank=True, null=True)
    dataexchange = models.CharField(max_length=60, blank=True, null=True)
    heartbeat = models.CharField(max_length=60, blank=True, null=True)
    backup = models.CharField(max_length=60, blank=True, null=True)
    guestserviceinterface = models.CharField(max_length=60, blank=True, null=True)
    checkpointlocation = models.CharField(blank=True, null=True)
    thumbnailimage = models.TextField(blank=True, null=True)
    vmwresourcepoolid = models.CharField(max_length=256, blank=True, null=True)
    lastrestoredcheckpointid = models.CharField(max_length=256, blank=True, null=True)
    binlocation = models.CharField(blank=True, null=True)
    binsize = models.BigIntegerField(blank=True, null=True)
    excludefrompro = models.CharField(max_length=60, blank=True, null=True)
    currentavailablememorypercent = models.SmallIntegerField(blank=True, null=True)
    availablememorybuffer = models.IntegerField(blank=True, null=True)
    computertierid = models.CharField(max_length=256, blank=True, null=True)
    upgradedomain = models.IntegerField(blank=True, null=True)
    protectionunitid = models.CharField(max_length=256, blank=True, null=True)
    appdeploymentstate = models.IntegerField(blank=True, null=True)
    vminguestcheckpointxml = models.TextField(blank=True, null=True)
    lastserviceerror = models.CharField(max_length=60, blank=True, null=True)
    guestagentversion = models.CharField(max_length=256, blank=True, null=True)
    isfaulttolerant = models.CharField(max_length=60, blank=True, null=True)
    allocatedgpu = models.CharField(max_length=256, blank=True, null=True)
    localusername = models.CharField(blank=True, null=True)
    localuserpassword = models.CharField(max_length=60, blank=True, null=True)
    ismodifiedafterexport = models.CharField(max_length=60, blank=True, null=True)
    sharedstorage = models.CharField(max_length=60, blank=True, null=True)
    biosguid = models.CharField(max_length=256, blank=True, null=True)
    vmroleid = models.CharField(max_length=256, blank=True, null=True)
    servicewarningdata = models.CharField(max_length=60, blank=True, null=True)
    iscloned = models.CharField(max_length=60, blank=True, null=True)
    hasvalidprocessorcompatibilityvectors = models.CharField(max_length=60, blank=True, null=True)
    functionallevel = models.CharField(max_length=256, blank=True, null=True)
    keyprotectorownerid = models.CharField(max_length=256, blank=True, null=True)
    securitysummary = models.IntegerField(blank=True, null=True)
    azuredata = models.CharField(max_length=60, blank=True, null=True)
    lastlogontimestamp = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmm_tb_tbl_wlc_vminstance'
        app_label = 'sds_inventario' 


class VmmTbTblWlcVobjectUp(models.Model):
    id_tbl_wlc_vobject = models.IntegerField()
    objectid = models.CharField(max_length=1024, blank=True, null=True)
    objecttype = models.IntegerField(blank=True, null=True)
    objectstate = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    enabled = models.CharField(max_length=16, blank=True, null=True)
    accessibility = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    owneridentifier = models.CharField(max_length=1024, blank=True, null=True)
    creationtime = models.DateTimeField(blank=True, null=True)
    modifiedtime = models.DateTimeField(blank=True, null=True)
    osprofileid = models.CharField(max_length=1024, blank=True, null=True)
    hwprofileid = models.CharField(max_length=1024, blank=True, null=True)
    perfcounternid = models.CharField(max_length=1024, blank=True, null=True)
    libserverid = models.CharField(max_length=1024, blank=True, null=True)
    location = models.CharField(blank=True, null=True)
    hostid = models.CharField(max_length=1024, blank=True, null=True)
    cloudid = models.CharField(max_length=1024, blank=True, null=True)
    tag = models.CharField(blank=True, null=True)
    quotapoint = models.IntegerField(blank=True, null=True)
    costcenter = models.CharField(blank=True, null=True)
    userroleid = models.CharField(max_length=1024, blank=True, null=True)
    vmcheckpointid = models.CharField(max_length=1024, blank=True, null=True)
    taskcheckpointxml = models.CharField(blank=True, null=True)
    failedjobid = models.CharField(max_length=1024, blank=True, null=True)
    osid = models.CharField(max_length=1024, blank=True, null=True)
    iscustomizable = models.CharField(max_length=1024, blank=True, null=True)
    sanclonecapable = models.CharField(max_length=1024, blank=True, null=True)
    sanclonecapableerror = models.CharField(max_length=1024, blank=True, null=True)
    updatemanagementprofileid = models.CharField(max_length=1024, blank=True, null=True)
    enhancedsession = models.CharField(max_length=1024, blank=True, null=True)
    lastlogontimestamp = models.DateTimeField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmm_tb_tbl_wlc_vobject_up'
        app_label = 'sds_inventario' 


class VmmVwServerhost(models.Model):
    id_tbl_wlc_vobject = models.IntegerField()
    name = models.CharField(max_length=1024, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    os = models.CharField(max_length=1204, blank=True, null=True)
    version = models.CharField(max_length=1204, blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmm_vw_serverhost'
        app_label = 'sds_inventario' 


class vw_ServerHost(models.Model):
    id_serverhost = models.AutoField(primary_key=True)
    id_trilha = models.ForeignKey('Trilha', models.DO_NOTHING, db_column='id_trilha')
    trilha = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)    
    hostname = models.CharField(max_length=60, blank=True, null=True)
    fisicovm = models.CharField(max_length=20, blank=True, null=True)
    sistemaoperaciona = models.CharField(max_length=200, blank=True, null=True)
    ipaddress = models.CharField(max_length=250, blank=True, null=True)
    portconect = models.CharField(max_length=10, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    versao = models.CharField(max_length=350, blank=True, null=True)
    cpu = models.BigIntegerField(blank=True, null=True)
    memoryram = models.BigIntegerField(blank=True, null=True)
    ad = models.BooleanField(blank=True, null=True)
    or_ad = models.BooleanField(blank=True, null=True)
    sccm = models.BooleanField(blank=True, null=True)
    or_sccm = models.BooleanField(blank=True, null=True)
    hv = models.BooleanField(blank=True, null=True)
    or_hv = models.BooleanField(blank=True, null=True)
    nx = models.BooleanField(blank=True, null=True)
    or_nx = models.BooleanField(blank=True, null=True)
    vw = models.BooleanField(blank=True, null=True)
    or_vw = models.BooleanField(blank=True, null=True)
    vmm = models.BooleanField(blank=True, null=True)
    or_vmm = models.BooleanField(blank=True, null=True)    
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_serverhost'
        app_label = 'sds_inventario' 