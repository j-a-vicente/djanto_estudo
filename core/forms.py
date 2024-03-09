from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Name')
    email = forms.CharField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    