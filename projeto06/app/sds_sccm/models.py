from django.db import models

class Applications(models.Model):
    id_applications = models.AutoField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    ad_site_name0 = models.CharField(max_length=50, blank=True, null=True)
    user_name0 = models.CharField(max_length=250, blank=True, null=True)
    publisher0 = models.CharField(max_length=250, blank=True, null=True)
    displayname0 = models.TextField(blank=True, null=True)
    version0 = models.CharField(max_length=50, blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications'
        app_label = 'sds_sccm'
        db_tablespace = 'public'  


class Software(models.Model):
    id_software = models.AutoField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    companyname = models.CharField(max_length=250, blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    fileversion = models.CharField(max_length=250, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    lastupdateetl = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software'
        app_label = 'sds_sccm'
        db_tablespace = 'public'  


class ShApplications(models.Model):
    id_server_host = models.AutoField(primary_key=True)    
    hostname = models.CharField(max_length=256, blank=True, null=True)
    publisher0 = models.CharField(max_length=250, blank=True, null=True)
    displayname0 = models.TextField(blank=True, null=True)
    version0 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sh_applications'
        app_label = 'sds_sccm'
        db_tablespace = 'public'         
        ordering = ['publisher0', 'displayname0'] 