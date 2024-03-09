from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm


def index(reguest):
    return render(reguest, 'index.html')


def contato(reguest):
    form = ContatoForm(reguest.POST or None)

    if str(reguest.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            print('Mensagem envidada ')
            print(f'Nome: {nome}')
            print(f'Nome: {email}')
            print(f'Nome: {assunto}')
            print(f'Nome: {mensagem}')
            
            messages.success(reguest,  'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(reguest, 'Erro ao enviar o e-mail')            

    context = {
        'form': form
    }

    return render(reguest,'contato.html', context)


def produto(request):
    return render(request,'produto.html')

