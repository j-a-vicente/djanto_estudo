from django.urls import path
from . import views

urlpatterns = [
    path('zabbix_host_cpu_30_dias/<str:server_host_value>/', views.ZabbixHostCpuUlt30dias, name='zabbix_host_cpu_30_dias'),
]
