from django.db import models


class Applications(models.Model):
    id_applications = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    ad_site_name0 = models.CharField(max_length=50, blank=True, null=True)
    user_name0 = models.CharField(max_length=250, blank=True, null=True)
    publisher0 = models.CharField(max_length=250, blank=True, null=True)
    displayname0 = models.TextField(blank=True, null=True)
    version0 = models.CharField(max_length=50, blank=True, null=True)
    dhupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applications'
        app_label = 'sds_sccm'  


class NetworkAdapter(models.Model):
    id_network_adapter = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    adaptertype0 = models.TextField(blank=True, null=True)
    productname0 = models.TextField(blank=True, null=True)
    macaddress0 = models.TextField(blank=True, null=True)
    dhcpenabled0 = models.BooleanField(blank=True, null=True)
    dhcpserver0 = models.TextField(blank=True, null=True)
    dnsdomain0 = models.TextField(blank=True, null=True)
    dnshostname0 = models.TextField(blank=True, null=True)
    ipaddress0 = models.TextField(blank=True, null=True)
    deviceid0 = models.IntegerField(blank=True, null=True)
    ipenabled0 = models.BooleanField(blank=True, null=True)
    ipsubnet0 = models.TextField(blank=True, null=True)
    servicename0 = models.TextField(blank=True, null=True)
    dhupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'network_adapter'
        app_label = 'sds_sccm'  


class ServerHost(models.Model):
    id_server_host = models.IntegerField(primary_key=True)
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
    dhupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'server_host'
        app_label = 'sds_sccm'  


class Software(models.Model):
    id_software = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    companyname = models.CharField(max_length=250, blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    fileversion = models.CharField(max_length=250, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)
    dhupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software'
        app_label = 'sds_sccm'  


class Vmdisk(models.Model):
    id_vmdisk = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    groupid = models.IntegerField(blank=True, null=True)
    agentid = models.IntegerField(blank=True, null=True)
    tmstamp = models.DateTimeField(blank=True, null=True)
    caption0 = models.CharField(max_length=150, blank=True, null=True)
    description0 = models.CharField(max_length=50, blank=True, null=True)
    deviceid0 = models.CharField(max_length=50, blank=True, null=True)
    index0 = models.IntegerField(blank=True, null=True)
    interfacetype0 = models.CharField(max_length=50, blank=True, null=True)
    manufacturer0 = models.CharField(max_length=50, blank=True, null=True)
    mediatype0 = models.CharField(max_length=50, blank=True, null=True)
    model0 = models.CharField(max_length=50, blank=True, null=True)
    name0 = models.CharField(max_length=100, blank=True, null=True)
    partitions0 = models.IntegerField(blank=True, null=True)
    pnpdeviceid0 = models.CharField(max_length=256, blank=True, null=True)
    scsibus0 = models.IntegerField(blank=True, null=True)
    scsilogicalunit0 = models.IntegerField(blank=True, null=True)
    scsiport0 = models.IntegerField(blank=True, null=True)
    scsitargetid0 = models.IntegerField(blank=True, null=True)
    size0 = models.FloatField(blank=True, null=True)
    systemname0 = models.CharField(max_length=50, blank=True, null=True)
    dhupdate = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vmdisk'
        app_label = 'sds_sccm'  


class VwSoftware(models.Model):
    id_software = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    serverhost = models.CharField(max_length=150, blank=True, null=True)
    fabricante = models.CharField(max_length=250, blank=True, null=True)
    software = models.CharField(max_length=250, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_software'
        app_label = 'sds_sccm'  

class VwSoftwareFile(models.Model):
    id_software = models.IntegerField(primary_key=True)
    fileexec = models.CharField(max_length=250, blank=True, null=True)
    version = models.CharField(max_length=250, blank=True, null=True)
    localinstall = models.TextField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'vw_software_file'
        app_label = 'sds_sccm'          