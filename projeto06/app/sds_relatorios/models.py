from django.db import models
from django.db.models import Case, When, IntegerField


class VwRelSrvProducao(models.Model):
    id_serverhost = models.AutoField(primary_key=True)
    id_trilha = models.ForeignKey('Trilha', models.DO_NOTHING, db_column='id_trilha')
    trilha = models.CharField(max_length=60, blank=True, null=True)
    sigla = models.CharField(max_length=10, blank=True, null=True)    
    hostname = models.CharField(max_length=60, blank=True, null=True)
    fisicovm = models.CharField(max_length=20, blank=True, null=True)
    sistemaoperaciona = models.CharField(max_length=200, blank=True, null=True)
    cpu = models.BigIntegerField(blank=True, null=True)
    memoryram = models.BigIntegerField(blank=True, null=True)
    ipaddress = models.CharField(max_length=250, blank=True, null=True)
    zabbix = models.BooleanField(blank=True, null=True)
    origem = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_rel_srv_producao'
        app_label = 'sds_inventario' 

    @staticmethod
    def get_ordered_queryset():
        return VwRelSrvProducao.objects.annotate(
            order_field=Case(
                When(fisicovm='Servidor Virtual', then=1),
                When(fisicovm='Servidor Físico', then=2),
                When(fisicovm='Desktop', then=3),
                When(fisicovm='Notebook', then=4),
                default=5,
                output_field=IntegerField(),
            )
        ).order_by('id_trilha','order_field', 'zabbix')
