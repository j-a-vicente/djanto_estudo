from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

from django.views.generic.list import ListView

from .models import vw_basededados

class DataBaseList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'database_list.html'  
    model = vw_basededados    
    context_object_name = 'list_database'
    
    paginate_by = 10

    def get_queryset(self):
        txt_basededados = self.request.GET.get('basededados')     
        parametro_page = self.request.GET.get('page','1')
        parametro_limit = self.request.GET.get('limit','25')
        

        if not(parametro_limit.isdigit() and int(parametro_limit) >0 ):
            parametro_limit = 10    

        if txt_basededados:
            context = vw_basededados.objects.filter(basededados__icontains=txt_basededados).order_by('basededados')
        else:
            # Retorna todos os registros
            context = vw_basededados.objects.all().order_by('-tamanho')

        srv_paginator = Paginator(context, parametro_limit)

        try:
            page = srv_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = srv_paginator.page(1)
        return page
