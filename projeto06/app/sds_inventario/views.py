from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.db.models import Case, When, IntegerField

from .models import vw_ServerHost
from ..sds_sccm.models import ShApplications
from ..sds_zabbix.models import VwItemsServerHost

class ServerHostList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_list.html'
    model = vw_ServerHost
    context_object_name = 'list_serverHost'
    paginate_by = 15  # Define a paginação padrão para 15 itens por página

    def get_queryset(self):
        txt_hostname = self.request.GET.get('hostname', '')
        parametro_limit = self.request.GET.get('limit', '15')

        # Verifica se parametro_limit é um número positivo
        if parametro_limit.isdigit() and int(parametro_limit) > 0:
            parametro_limit = int(parametro_limit)
        else:
            parametro_limit = 15

        queryset = vw_ServerHost.objects.annotate(
            order_field=Case(
                When(fisicovm='Servidor', then=1),
                When(fisicovm='Servidor Físico', then=2),
                When(fisicovm='Desktop', then=3),
                When(fisicovm='Notebook', then=4),
                default=5,
                output_field=IntegerField(),
            )
        ).order_by('order_field', 'hostname')

        if txt_hostname:
            queryset = queryset.filter(hostname__icontains=txt_hostname)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        txt_hostname = self.request.GET.get('hostname', '')
        page_number = self.request.GET.get('page', 1)
        parametro_limit = self.request.GET.get('limit', '15')

        if parametro_limit.isdigit() and int(parametro_limit) > 0:
            parametro_limit = int(parametro_limit)
        else:
            parametro_limit = 15

        queryset = self.get_queryset()
        paginator = Paginator(queryset, parametro_limit)
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj
        context['hostname'] = txt_hostname
        context['list_serverHost'] = page_obj.object_list

        return context



class ServerHostDetalhe(GroupRequiredMixin, LoginRequiredMixin, ListView):   
    login_url = reverse_lazy('login') 
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_detalhe.html'  
    model = vw_ServerHost
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Busca o ModuloConfig com a pk especificada
        modulo_config = vw_ServerHost.objects.get(pk=self.kwargs['pk'])

        context['ServerHost'] = modulo_config
        
        # Filtra as outras classes pelo id_modulo correspondente
        #context['detalhe_ad'] = AdComputer.objects.filter(name__iexact=modulo_config.hostname)
        #context['db_instancia'] = TbDatabaseInstancia.objects.filter(id_serverhost=modulo_config.id_serverhost)        
        #context['db_activeDirectory'] = TbAdComputer.objects.filter(id_serverhost=modulo_config.id_serverhost)
        #context['db_nutanix'] = TbNtVm.objects.filter(id_serverhost=modulo_config.id_serverhost)
        #context['db_TbSccmDk'] = TbSccmDk.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        context['detalhe_zabbix_items'] = VwItemsServerHost.objects.filter(id_server_host=modulo_config.id_serverhost)
        context['db_Software'] = ShApplications.objects.filter(hostname=modulo_config.hostname)

        # Paginação para VwSoftware
        #tb_sccm_sf_list = ShApplications.objects.filter(hostname=modulo_config.hostname)
        #paginator = Paginator(tb_sccm_sf_list, self.paginate_by)
        #page = self.request.GET.get('page')
        #try:
        #    context['db_Software'] = paginator.page(page)
        #except PageNotAnInteger:
        #    context['db_Software'] = paginator.page(1)
        #except EmptyPage:
        #    context['db_Software'] = paginator.page(paginator.num_pages)

        #context['db_TbSccmApp'] = TbSccmApp.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        #context['db_TbSccmSf'] = TbSccmSf.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        
        return context
