
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView

from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Modulo
from .forms import ModuloForm

class ModuloList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'modulo_list.html'
    model = Modulo
    context_object_name = 'ct_modulo'
    paginate_by = 10  
    ordering = ['modulo'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Verifique se o `context['ct_modulo']` está preenchido corretamente
        modulos_forms = {modulo.pk: ModuloForm(instance=modulo) for modulo in context['ct_modulo']}
        context['modulos_forms'] = modulos_forms
        return context
  
class ModuloUpdateView(UpdateView):
    model = Modulo
    form_class = ModuloForm
    template_name = 'itg_dashboard.html'
    success_url = reverse_lazy('moduloList')  # ou qualquer página de sucesso

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return self.form_invalid(form)


#class ModuloUpdateView(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
#    login_url = reverse_lazy('login')
#    group_required = [u"Administradores"]
#    model = Modulo
#    form_class = ModuloForm
#    template_name = 'itg_modulo_form.html'
#    success_url = reverse_lazy('moduloList')  # Corrigido para o nome da URL de lista

def get_modulo_form(request):
    id_modulo = request.GET.get('id_modulo')
    modulo = get_object_or_404(Modulo, pk=id_modulo)
    form = ModuloForm(instance=modulo)

    # Renderiza o formulário como HTML
    formulario_html = render_to_string('modulos_form_partial.html', {
        'form': form,
        'modulo': modulo
    }, request=request)

    return JsonResponse({'formulario_html': formulario_html})

