from django.db import models

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
