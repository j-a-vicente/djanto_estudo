from django.urls import path

# Views de lista
from .views import  RelOperacionaMensal_SO, RelOperacionaMensalSOimp
from . import views

urlpatterns = [
    path('rel_op_men_so/',RelOperacionaMensal_SO.as_view() , name='rel_op_men_so'),
    path('rel_op_men_so_imp/',RelOperacionaMensalSOimp.as_view() , name='rel_op_men_so_imp'),
    path('sistema_operacional_chart/', views.sistema_operacional_chart, name='sistema_operacional_chart'),
    path('servidor_tipo_chart/', views.servidor_tipo_chart, name='servidor_tipo_chart'),
    path('monito_zabbix_chart/', views.monito_zabbix_chart, name='monito_zabbix_chart'),
    #path('ServerHostDetalhe/<int:pk>/',ServerHostDetalhe.as_view() , name='ServerHostDetalhe'),
]