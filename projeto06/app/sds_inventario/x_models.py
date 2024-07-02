from django.db import models


class TbDatabaseInstancia(models.Model):
    idinstancia = models.IntegerField()
    id_serverhost = models.IntegerField()
    id_trilha = models.IntegerField()
    idcluster = models.IntegerField(blank=True, null=True)
    instancia = models.CharField(max_length=255, blank=True, null=True)
    sgbd = models.CharField(max_length=30, blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True, null=True)
    conectstring = models.CharField(max_length=255, blank=True, null=True)
    porta = models.FloatField(blank=True, null=True)
    cluster = models.BooleanField(blank=True, null=True)
    versao = models.CharField(max_length=255, blank=True, null=True)
    productversion = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    funcaoserver = models.CharField(max_length=100, blank=True, null=True)
    sobreadministracao = models.CharField(max_length=100, blank=True, null=True)
    memoryconfig = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    cpu = models.IntegerField(blank=True, null=True)
    estanciaativo = models.BooleanField(blank=True, null=True)
    startinstancia = models.DateTimeField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    status_bd = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_db_instancia'  
        app_label = 'sds_inventario'  


class vw_ServerHost(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
    id_trilha = models.IntegerField()
    trilha = models.CharField(max_length=255)
    sigla = models.CharField(max_length=50)
    hostname = models.CharField(max_length=255)
    dep = models.CharField(max_length=255)
    regiao = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    unidade = models.CharField(max_length=255)
    fisicovm = models.CharField(max_length=50)
    sistemaoperaciona = models.CharField(max_length=255)
    ipaddress = models.CharField(max_length=50)
    portconect = models.IntegerField()
    descricao = models.TextField()
    versao = models.CharField(max_length=50)
    cpu = models.CharField(max_length=50)
    memoryram = models.CharField(max_length=50)
    ad = models.CharField(max_length=50)
    or_ad = models.CharField(max_length=50)
    sccm = models.CharField(max_length=50)
    or_sccm = models.CharField(max_length=50)
    nx = models.CharField(max_length=50)
    or_nx = models.CharField(max_length=50)
    vw = models.CharField(max_length=50)
    or_vw = models.CharField(max_length=50)
    origemdata = models.CharField(max_length=50)
    md_database = models.CharField(max_length=50)
    dhcriacao = models.DateTimeField()
    dhalteracao = models.DateTimeField()
    ativo = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'vw_serverhost'        
        app_label = 'sds_inventario'

    def __str__(self) -> str:
        return "{} ({})".format(self.hostname)


class TbAdComputer(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
    sid = models.CharField(max_length=100, blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    operatingsystem = models.TextField(blank=True, null=True)
    operatingsystemversion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_tb_ad_computer'
        app_label = 'sds_inventario'  



class TbNtVm(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
    vmname = models.CharField(max_length=256, blank=True, null=True)
    ipaddresses = models.CharField(max_length=100, blank=True, null=True)
    memorycapacityinbytes = models.TextField(blank=True, null=True)
    numvcpus = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_tb_nt_vm'  
        app_label = 'sds_inventario'        

class TbSccmDk(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
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
    
    class Meta:
        managed = False
        db_table = 'vw_tb_sccm_dk'    
        app_label = 'sds_inventario'

class TbSccmApp(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    ad_site_name0 = models.CharField(max_length=50, blank=True, null=True)
    user_name0 = models.CharField(max_length=250, blank=True, null=True)
    publisher0 = models.CharField(max_length=250, blank=True, null=True)
    displayname0 = models.TextField(blank=True, null=True)
    version0 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_tb_sccm_app'        
        app_label = 'sds_inventario'

class TbSccmSf(models.Model):
    id_serverhost = models.IntegerField(primary_key=True)
    resourceid = models.CharField(max_length=20, blank=True, null=True)
    name0 = models.CharField(max_length=150, blank=True, null=True)
    companyname = models.CharField(max_length=250, blank=True, null=True)
    productname = models.CharField(max_length=250, blank=True, null=True)
    filename = models.CharField(max_length=250, blank=True, null=True)
    fileversion = models.CharField(max_length=250, blank=True, null=True)
    filepath = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_tb_sccm_sf'   
        app_label = 'sds_inventario'     

