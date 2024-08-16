from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage , PageNotAnInteger

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from ..sds_active_directory.models import AdComputer

from ..sds_sccm.models import VwSoftware, VwSoftwareFile

from .models import vw_ServerHost, TbDatabaseInstancia, TbAdComputer, TbNtVm, TbSccmDk, TbSccmApp, TbSccmSf


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

class ServerHostDetalhe(GroupRequiredMixin, LoginRequiredMixin, ListView):   
    login_url = reverse_lazy('login') 
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_detalhe.html'  
    model = vw_ServerHost
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Busca o ModuloConfig com a pk especificada
        modulo_config = vw_ServerHost.objects.get(pk=self.kwargs['pk'])

        context['ServerHost'] = modulo_config
        
        # Filtra as outras classes pelo id_modulo correspondente
        context['detalhe_ad'] = AdComputer.objects.filter(name__iexact=modulo_config.hostname)
        context['db_instancia'] = TbDatabaseInstancia.objects.filter(id_serverhost=modulo_config.id_serverhost)        
        context['db_activeDirectory'] = TbAdComputer.objects.filter(id_serverhost=modulo_config.id_serverhost)
        context['db_nutanix'] = TbNtVm.objects.filter(id_serverhost=modulo_config.id_serverhost)
        context['db_TbSccmDk'] = TbSccmDk.objects.filter(id_serverhost=modulo_config.id_serverhost) 


        # Paginação para VwSoftware
        tb_sccm_sf_list = VwSoftware.objects.filter(serverhost=modulo_config.hostname)
        paginator = Paginator(tb_sccm_sf_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            context['db_VwSoftware'] = paginator.page(page)
        except PageNotAnInteger:
            context['db_VwSoftware'] = paginator.page(1)
        except EmptyPage:
            context['db_VwSoftware'] = paginator.page(paginator.num_pages)


        # Paginação para VwSoftwareFile
        # Obtém uma lista dos id_software dos objetos em tb_sccm_sf_list
        id_software_list = [obj.id_software for obj in tb_sccm_sf_list]

        # Filtra VwSoftwareFile usando os id_software obtidos
        tb_sccm_app_list = VwSoftwareFile.objects.filter(id_software__in=id_software_list)        
        #tb_sccm_app_list = VwSoftwareFile.objects.filter(id_software=tb_sccm_sf_list.id_software)
        paginator = Paginator(tb_sccm_app_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            context['db_VwSoftwareFile'] = paginator.page(page)
        except PageNotAnInteger:
            context['db_VwSoftwareFile'] = paginator.page(1)
        except EmptyPage:
            context['db_VwSoftwareFile'] = paginator.page(paginator.num_pages)


#        context['db_TbSccmApp'] = TbSccmApp.objects.filter(id_serverhost=modulo_config.id_serverhost) 
#        context['db_TbSccmSf'] = TbSccmSf.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        
        return context    




    