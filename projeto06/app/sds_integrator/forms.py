from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Modulo, ModuloDatafont

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['modulo', 'descricao', 'ativo']

    def __init__(self, *args, **kwargs):
        super(ModuloForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Salvar'))


class ModuloDatafontForm(forms.ModelForm):
    class Meta:
        model = ModuloDatafont
        fields = [
            'id_modulo', 'tipo_font', 'servername', 'serverip', 'sgbp',
            'databasename', 'username', 'psw', 'port', 'stringconection', 
            'descricao', 'ativo'
        ]
        widgets = {
            'id_modulo': forms.Select(attrs={'class': 'form-control'}),
            'tipo_font': forms.TextInput(attrs={'class': 'form-control'}),
            'servername': forms.TextInput(attrs={'class': 'form-control'}),
            'serverip': forms.TextInput(attrs={'class': 'form-control'}),
            'sgbp': forms.TextInput(attrs={'class': 'form-control'}),
            'databasename': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'psw': forms.PasswordInput(attrs={'class': 'form-control'}),
            'port': forms.NumberInput(attrs={'class': 'form-control'}),
            'stringconection': forms.Textarea(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'ativo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['id_modulo'].queryset = Modulo.objects.filter(ativo=True)
