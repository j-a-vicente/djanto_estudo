from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from .models import vw_ServerHost
from ..sds_sccm.models import ShApplications

class ServerHostList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_list.html'
    model = vw_ServerHost
    context_object_name = 'list_serverHost'
    paginate_by = 30

    def get_queryset(self):
        txt_hostname = self.request.GET.get('hostname')
        parametro_limit = self.request.GET.get('limit', '30')

        if not (parametro_limit.isdigit() and int(parametro_limit) > 0):
            parametro_limit = 30

        if txt_hostname:
            queryset = vw_ServerHost.objects.filter(hostname__icontains=txt_hostname).order_by('hostname')
        else:
            queryset = vw_ServerHost.objects.all().order_by('hostname')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hostname'] = self.request.GET.get('hostname', '')
        return context


class ServerHostDetalhe(GroupRequiredMixin, LoginRequiredMixin, ListView):   
    login_url = reverse_lazy('login') 
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'serverhost_detalhe.html'  
    model = vw_ServerHost
    paginate_by = 8

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


        # Paginação para VwSoftware
        tb_sccm_sf_list = ShApplications.objects.filter(hostname=modulo_config.hostname)
        paginator = Paginator(tb_sccm_sf_list, self.paginate_by)
        page = self.request.GET.get('page')
        try:
            context['db_Software'] = paginator.page(page)
        except PageNotAnInteger:
            context['db_Software'] = paginator.page(1)
        except EmptyPage:
            context['db_Software'] = paginator.page(paginator.num_pages)


        #context['db_TbSccmApp'] = TbSccmApp.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        #context['db_TbSccmSf'] = TbSccmSf.objects.filter(id_serverhost=modulo_config.id_serverhost) 
        
        return context    




    