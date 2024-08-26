from django.shortcuts import render
from django.http import JsonResponse
from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.db.models import Case, When, IntegerField, Count

from .models import VwRelSrvProducao

class RelOperacionaMensal_SO(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'rel_operacional_mensal_so.html'
    context_object_name = 'srv_prd'  # Nome da variável de contexto

    def get_queryset(self):
        txt_hostname = self.request.GET.get('hostname', '')

        queryset = VwRelSrvProducao.objects.annotate(
            order_field=Case(
                When(fisicovm='Servidor Virtual', then=1),
                When(fisicovm='Servidor Físico', then=2),
                When(fisicovm='Desktop', then=3),
                When(fisicovm='Notebook', then=4),
                default=5,
                output_field=IntegerField(),
            )
        ).order_by('id_trilha', 'order_field', 'hostname')

        if txt_hostname:
            queryset = queryset.filter(hostname__icontains=txt_hostname)

        return queryset

class RelOperacionaMensalSOimp(ListView):
    context_object_name = 'srv_prd'  
    template_name = 'rel_operacional_mensal_so_imp.html'
    

    def get_queryset(self):
        txt_hostname = self.request.GET.get('hostname', '')

        queryset = VwRelSrvProducao.objects.annotate(
            order_field=Case(
                When(fisicovm='Servidor Virtual', then=1),
                When(fisicovm='Servidor Físico', then=2),
                When(fisicovm='Desktop', then=3),
                When(fisicovm='Notebook', then=4),
                default=5,
                output_field=IntegerField(),
            )
        ).order_by('id_trilha', 'order_field', 'hostname')

        if txt_hostname:
            queryset = queryset.filter(hostname__icontains=txt_hostname)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Adicionando a soma total de servidores ao contexto
        context['total_servidores'] = self.get_queryset().count()
        return context



def sistema_operacional_chart(Grequest):
   
    # Consultar e agrupar os sistemas operacionais por quantidade
    data = (
        VwRelSrvProducao.objects
        .values('sistemaoperaciona')
        .annotate(count=Count('sistemaoperaciona'))
        .order_by('sistemaoperaciona')
    )

    labels = [entry['sistemaoperaciona'] for entry in data]
    counts = [entry['count'] for entry in data]

    # Preparar os dados para o JSON
    data_json = {
        'labels': labels,
        'counts': counts,
    }

    return JsonResponse(data_json)
