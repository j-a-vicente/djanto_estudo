# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
        app_label = 'sds_integrator'


class Modulo(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    modulo = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo'
        app_label = 'sds_integrator'
        


class ModuloDatafont(models.Model):
    id_modulo_datafont = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    tipo_font = models.CharField(max_length=20, blank=True, null=True, db_comment='Se a conexão e de Origem ou Destino')
    servername = models.CharField(max_length=150, blank=True, null=True)
    serverip = models.CharField(max_length=150, blank=True, null=True)
    sgbp = models.CharField(max_length=50, blank=True, null=True)
    databasename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    psw = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    stringconection = models.TextField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_datafont'
        app_label = 'sds_integrator'


class ModuloDb(models.Model):
    id_modulo_db = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    base_modulo = models.CharField(max_length=50, blank=True, null=True)
    base_name = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_db'
        app_label = 'sds_integrator'


class ModuloDbTable(models.Model):
    id_modulo_db_table = models.AutoField(primary_key=True)
    id_modulo_db = models.ForeignKey(ModuloDb, models.DO_NOTHING, db_column='id_modulo_db')
    name_table = models.CharField(max_length=50, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_db_table'
        app_label = 'sds_integrator'


class ModuloDbTableModuloEtl(models.Model):
    id_modulo_db_table_modulo_etl = models.AutoField(primary_key=True)
    id_modulo_db_table = models.ForeignKey(ModuloDbTable, models.DO_NOTHING, db_column='id_modulo_db_table')
    id_modulo_etl_script = models.ForeignKey('ModuloEtlScript', models.DO_NOTHING, db_column='id_modulo_etl_script')
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_db_table_modulo_etl'
        app_label = 'sds_integrator'


class ModuloEtl(models.Model):
    id_modulo_etl = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    etl_name = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_etl'
        app_label = 'sds_integrator'


class ModuloEtlDatafontOrigem(models.Model):
    id_modulo_etl_datafont_origem = models.AutoField(primary_key=True)
    id_modulo_datafont = models.ForeignKey(ModuloDatafont, models.DO_NOTHING, db_column='id_modulo_datafont')
    id_modulo_etl_script = models.ForeignKey('ModuloEtlScript', models.DO_NOTHING, db_column='id_modulo_etl_script')
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_etl_datafont_origem'
        app_label = 'sds_integrator'


class ModuloEtlScript(models.Model):
    id_modulo_etl_script = models.AutoField(primary_key=True)
    id_modulo_etl = models.ForeignKey(ModuloEtl, models.DO_NOTHING, db_column='id_modulo_etl')
    id_md_df_destino = models.ForeignKey(ModuloDatafont, models.DO_NOTHING, db_column='id_md_df_destino')
    filename = models.CharField(max_length=255, blank=True, null=True)
    codigofont = models.TextField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dependencia = models.IntegerField(blank=True, null=True)
    exec_paralelo = models.TextField(blank=True, null=True)  # This field type is a guess.
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)
    id_dependencia = models.ForeignKey('self', models.DO_NOTHING, db_column='id_dependencia', blank=True, null=True)
    order_exec = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_etl_script'
        app_label = 'sds_integrator'


class ModuloIntegridadeEtl(models.Model):
    id_modulo_integridade_etl = models.AutoField(primary_key=True)
    id_modulo_etl = models.ForeignKey(ModuloEtl, models.DO_NOTHING, db_column='id_modulo_etl', blank=True, null=True)
    id_modulo_db_table = models.ForeignKey(ModuloDbTable, models.DO_NOTHING, db_column='id_modulo_db_table')
    tl_registro_pl = models.IntegerField()
    tl_rg_ativos_pl = models.IntegerField()
    tl_rg_desativados_pl = models.IntegerField()
    tl_rg_novos_up = models.IntegerField()
    tl_rg_ativados_up = models.IntegerField()
    tl_rg_desativados_up = models.IntegerField()
    tl_rg_outras_up = models.IntegerField()
    tl_registro = models.IntegerField()
    tl_rg_ativos = models.IntegerField()
    tl_rg_desativados = models.IntegerField()
    dhcriacao = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_integridade_etl'
        app_label = 'sds_integrator'


class ModuloJobs(models.Model):
    id_modulo_jobs = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    id_modulo_etl = models.ForeignKey(ModuloEtl, models.DO_NOTHING, db_column='id_modulo_etl', blank=True, null=True)
    nomejobs = models.CharField(max_length=150, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_jobs'
        app_label = 'sds_integrator'


class ModuloJobsSchedule(models.Model):
    id_modulo_jobs_schedule = models.AutoField(primary_key=True)
    id_modulo_jobs = models.ForeignKey(ModuloJobs, models.DO_NOTHING, db_column='id_modulo_jobs')
    nomeschedule = models.CharField(max_length=150, blank=True, null=True)
    frequency = models.TextField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_jobs_schedule'
        app_label = 'sds_integrator'


class ModuloLogs(models.Model):
    id_modulo_logs = models.AutoField(primary_key=True)
    id_pai = models.ForeignKey('self', models.DO_NOTHING, db_column='id_pai', blank=True, null=True)
    id_modulo_jobs_schedule = models.ForeignKey(ModuloJobsSchedule, models.DO_NOTHING, db_column='id_modulo_jobs_schedule', blank=True, null=True)
    executado = models.CharField(max_length=255, blank=True, null=True)
    dt_start = models.DateTimeField(blank=True, null=True)
    dt_end = models.DateTimeField(blank=True, null=True)
    job_status = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    log_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_logs'
        app_label = 'sds_integrator'


class ModuloServerRun(models.Model):
    id_modulo_server_run = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    nomeconexao = models.CharField(max_length=150, blank=True, null=True)
    server = models.CharField(max_length=100, blank=True, null=True)
    port = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'modulo_server_run'
        app_label = 'sds_integrator'


class VwModuloDatafont(models.Model):
    id_modulo_datafont = models.AutoField(primary_key=True)
    id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING, db_column='id_modulo')
    modulo = models.CharField(max_length=100, blank=True, null=True)
    tipo_font = models.CharField(max_length=20, blank=True, null=True, db_comment='Se a conexão e de Origem ou Destino')
    servername = models.CharField(max_length=150, blank=True, null=True)
    serverip = models.CharField(max_length=150, blank=True, null=True)
    sgbp = models.CharField(max_length=50, blank=True, null=True)
    databasename = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True)
    psw = models.CharField(max_length=100, blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    stringconection = models.TextField(blank=True, null=True)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    dhcriacao = models.DateTimeField(blank=True, null=True)
    dhalteracao = models.DateTimeField(blank=True, null=True)
    ativo = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_modulo_datafont'
        app_label = 'sds_integrator'

        