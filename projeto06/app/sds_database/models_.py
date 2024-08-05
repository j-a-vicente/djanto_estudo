# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Basededados(models.Model):
    idbasededados = models.AutoField(primary_key=True)
    idinstancia = models.ForeignKey('Instancia', models.DO_NOTHING, db_column='idinstancia')
    idtrilha = models.IntegerField(blank=True, null=True)
    basededados = models.CharField(max_length=150, blank=True, null=True)
    dbowner = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'basededados'


class Bdtabela(models.Model):
    idbdtabela = models.AutoField(primary_key=True)
    idbasededados = models.ForeignKey(Basededados, models.DO_NOTHING, db_column='idbasededados')
    schema_name = models.CharField(max_length=128, blank=True, null=True)
    table_name = models.CharField(max_length=128, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bdtabela'


class Bdtamanho(models.Model):
    idbdtamanho = models.AutoField(primary_key=True)
    idbasededados = models.ForeignKey(Basededados, models.DO_NOTHING, db_column='idbasededados')
    tamanho = models.FloatField(blank=True, null=True)
    datatimer = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bdtamanho'


class Cluster(models.Model):
    idcluster = models.AutoField(primary_key=True)
    idclustertipo = models.ForeignKey('Clustertipo', models.DO_NOTHING, db_column='idclustertipo', blank=True, null=True)
    clustername = models.CharField(max_length=60, blank=True, null=True)
    ip = models.CharField(max_length=50, blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cluster'


class Clusterno(models.Model):
    idclusterno = models.AutoField(primary_key=True)
    id_serverhost = models.IntegerField()
    idcluster = models.ForeignKey(Cluster, models.DO_NOTHING, db_column='idcluster')
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clusterno'


class Clustertipo(models.Model):
    idclustertipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clustertipo'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Instancia(models.Model):
    idinstancia = models.AutoField(primary_key=True)
    id_serverhost = models.IntegerField()
    id_trilha = models.IntegerField()
    idcluster = models.ForeignKey(Cluster, models.DO_NOTHING, db_column='idcluster', blank=True, null=True)
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
        db_table = 'instancia'


class InstanciaPg(models.Model):
    idinstancia_pg = models.AutoField(primary_key=True)
    idinstancia = models.ForeignKey(Instancia, models.DO_NOTHING, db_column='idinstancia')
    name = models.TextField(blank=True, null=True)
    setting = models.TextField(blank=True, null=True)
    unit = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instancia_pg'


class Logins(models.Model):
    idlogins = models.AutoField(primary_key=True)
    idinstancia = models.ForeignKey(Instancia, models.DO_NOTHING, db_column='idinstancia')
    loginname = models.CharField(max_length=128, blank=True, null=True)
    tipo_login = models.CharField(max_length=30, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logins'


class LoginsDatabase(models.Model):
    idloginsdb = models.AutoField(primary_key=True)
    idlogins = models.ForeignKey(Logins, models.DO_NOTHING, db_column='idlogins')
    acessement = models.JSONField(blank=True, null=True)
    tipo_login = models.CharField(max_length=30, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logins_database'


class LoginsInstancia(models.Model):
    idloginsin = models.AutoField(primary_key=True)
    idlogins = models.ForeignKey(Logins, models.DO_NOTHING, db_column='idlogins')
    acessement = models.JSONField(blank=True, null=True)
    tipo_login = models.CharField(max_length=30, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'logins_instancia'


class Serverdb(models.Model):
    id_serverhost = models.IntegerField(blank=True, null=True)
    id_trilha = models.IntegerField(blank=True, null=True)
    trilha = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)
    hostname = models.CharField(max_length=60, blank=True, null=True)
    dep = models.CharField(max_length=20, blank=True, null=True)
    regiao = models.CharField(max_length=20, blank=True, null=True)
    estado = models.CharField(max_length=20, blank=True, null=True)
    unidade = models.TextField(blank=True, null=True)
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
    nx = models.BooleanField(blank=True, null=True)
    or_nx = models.BooleanField(blank=True, null=True)
    vw = models.BooleanField(blank=True, null=True)
    or_vw = models.BooleanField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serverdb'


class Tbcoluna(models.Model):
    idtbcoluna = models.AutoField(primary_key=True)
    idbdtabela = models.ForeignKey(Bdtabela, models.DO_NOTHING, db_column='idbdtabela')
    colunn_name = models.CharField(max_length=128, blank=True, null=True)
    ordenal_positon = models.IntegerField(blank=True, null=True)
    data_type = models.CharField(max_length=128, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbcoluna'


class Tbindex(models.Model):
    idtbindex = models.AutoField(primary_key=True)
    idbdtabela = models.ForeignKey(Bdtabela, models.DO_NOTHING, db_column='idbdtabela')
    index_name = models.CharField(max_length=255, blank=True, null=True)
    index_type = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbindex'


class Trilha(models.Model):
    id_trilha = models.IntegerField(blank=True, null=True)
    trilha = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trilha'
