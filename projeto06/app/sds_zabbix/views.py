from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.http.response import HttpResponse, JsonResponse
from datetime import datetime, timedelta

from .models import VwItemsServerHost, Hists


def ZabbixHostCpuUlt30dias(request, server_host_value):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]    

    # Definir a data de início e fim (últimos 30 dias)
    data_final = datetime.now()
    data_inicial = data_final - timedelta(days=30)
    
    # Filtrar os itemids correspondentes ao server_host_value no VwItemsServerHost
    try:
        item_ids = VwItemsServerHost.objects.filter(server_host=server_host_value).values_list('itemid', flat=True)
    except VwItemsServerHost.DoesNotExist:
        return JsonResponse({'error': 'Server host not found'}, status=404)
    
    # Filtrar os valores em Hists correspondentes aos itemids e ao período dos últimos 30 dias
    hists = Hists.objects.filter(itemids__in=item_ids, clock__date__gte=data_inicial, clock__date__lte=data_final)
    
    data = []
    labels = []
    
    # Criar uma lista com os últimos 30 dias
    for i in range(30):
        dia_atual = data_final - timedelta(days=i)
        
        # Filtrar e somar os valores para o dia específico
        valores_do_dia = hists.filter(clock__date=dia_atual.date())
        total_do_dia = sum(valores_do_dia.values_list('value', flat=True))
        
        # Adicionar a soma diária e a data correspondente
        labels.append(dia_atual.strftime('%d/%m'))
        data.append(total_do_dia)
    
    # Preparar os dados para retorno como JSON
    data_json = {'data': data[::-1], 'labels': labels[::-1]}
    
    return JsonResponse(data_json)
