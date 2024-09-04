
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, UpdateView, CreateView

from braces.views import GroupRequiredMixin, LoginRequiredMixin
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.http import JsonResponse

from .models import Modulo, VwModuloDatafont, ModuloDatafont
from .forms import ModuloForm, ModuloDatafontForm

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

class ModuloDatafontList(GroupRequiredMixin, LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administradores", u"Monitor", u"Operador", u"Visitante"]
    template_name = 'modulo_data_font_list.html'
    model = VwModuloDatafont
    context_object_name = 'moduloDataFontList'
    paginate_by = 10  
    ordering = ['modulo','tipo_font'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        modulos_forms = {modulo.pk: ModuloForm(instance=modulo) for modulo in context['moduloDataFontList']}
        context['modulos_forms'] = modulos_forms
        return context
    

class ModuloDatafontUpdateView(UpdateView):
    model = ModuloDatafont
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

def get_datafont_form(request):
    id_modulo_datafont = request.GET.get('id_modulo_datafont')
    modulo_datafont = get_object_or_404(ModuloDatafont, pk=id_modulo_datafont)
    form = ModuloDatafontForm(instance=modulo_datafont)

    # Renderiza o formulário como HTML
    formulario_html = render_to_string('modulos_form_partial.html', {
        'form': form,
        'modulo_datafont': modulo_datafont
    }, request=request)

    return JsonResponse({'formulario_html': formulario_html})
 

# View para criar um novo registro
class ModuloDatafontCreateView(CreateView):
    model = ModuloDatafont
    form_class = ModuloDatafontForm
    template_name = 'datafont_form.html'
    success_url = reverse_lazy('modulo_datafont_list')

# View para atualizar um registro existente
class ModuloDatafontUpdateView(UpdateView):
    model = ModuloDatafont
    form_class = ModuloDatafontForm
    template_name = 'datafont_form.html'
    success_url = reverse_lazy('modulo_datafont_list')