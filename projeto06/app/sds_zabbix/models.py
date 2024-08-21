# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Hists(models.Model):
    id_hist = models.AutoField(primary_key=True)
    itemids = models.IntegerField(blank=True, null=True)
    clock = models.DateTimeField()
    value = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hists'
        app_label = 'sds_zabbix'

class HistsDia(models.Model):
    id_hist_dia = models.AutoField(primary_key=True)
    itemids = models.IntegerField(blank=True, null=True)
    clock = models.DateTimeField()
    value = models.FloatField(blank=True, null=True)
    num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hists_dia'
        app_label = 'sds_zabbix'


class Hosts(models.Model):
    hostid = models.IntegerField(primary_key=True)
    id_server_host = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hosts'
        app_label = 'sds_zabbix'


class Items(models.Model):
    itemid = models.IntegerField(primary_key=True)
    hostid = models.IntegerField()
    name = models.CharField(max_length=255)
    type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'items'
        app_label = 'sds_zabbix'


class MasterTbServerhost(models.Model):
    id_serverhost = models.IntegerField(blank=True, null=True)
    hostname = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'master_tb_serverhost'
        app_label = 'sds_zabbix'


class Trends(models.Model):
    id_trend = models.AutoField(primary_key=True)
    itemids = models.IntegerField(blank=True, null=True)
    clock = models.DateTimeField()
    num = models.IntegerField(blank=True, null=True)
    value_min = models.FloatField(blank=True, null=True)
    value_avg = models.FloatField(blank=True, null=True)
    value_max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trends'
        app_label = 'sds_zabbix'

class VwItemsServerHost(models.Model):
    itemid = models.IntegerField(primary_key=True)
    hostid = models.IntegerField()    
    id_server_host = models.IntegerField()    
    server_host = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    type = models.IntegerField()   
    monitor = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_items_host'
        app_label = 'sds_zabbix'    
        ordering = ['-monitor', 'name']