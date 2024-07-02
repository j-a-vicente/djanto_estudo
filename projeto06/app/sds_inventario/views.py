from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger
from django.views.generic.list import ListView

from .models import vw_ServerHost


class ServerHostList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_list.html'  
    model = vw_ServerHost    
    context_object_name = 'list_serverHost'
    
    paginate_by = 10

    def get_queryset(self):
        txt_hostname = self.request.GET.get('hostname')     
        parametro_page = self.request.GET.get('page','1')
        parametro_limit = self.request.GET.get('limit','25')
        

        if not(parametro_limit.isdigit() and int(parametro_limit) >0 ):
            parametro_limit = 10    

        if txt_hostname:
            context = vw_ServerHost.objects.filter(hostname__icontains=txt_hostname).order_by('hostname')
        else:
            # Retorna todos os registros
            context = vw_ServerHost.objects.all().order_by('hostname')

        srv_paginator = Paginator(context, parametro_limit)

        try:
            page = srv_paginator.page(parametro_page)
        except (EmptyPage, PageNotAnInteger):
            page = srv_paginator.page(1)
        return page