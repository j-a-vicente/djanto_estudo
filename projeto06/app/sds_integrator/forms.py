from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Modulo

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['modulo', 'descricao', 'ativo']

    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))

