# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_serverhost'
        app_label = 'sds_inventario' 