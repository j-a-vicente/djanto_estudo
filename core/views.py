from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

from .forms import ContatoForm, ProdutoModelForm
from .models import Produto

def index(reguest):
    return render(reguest, 'index.html')


def contato(reguest):
    form = ContatoForm(reguest.POST or None)

    if str(reguest.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(reguest, 'E-mail enviado com sucesso!')
            form = ContatoForm()
        else:
            messages.error(reguest, 'Erro ao enviar e-mail')
    context = {
        'form': form
    }
    return render(reguest, 'contato.html', context)


def produto(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()

                #prod = form.save(commit=False)
                #print(f'Nome: {prod.nome}')
                #print(f'Preço:{prod.preco}')
                #print(f'Estoque:{prod.estoque}')
                #print(f'imagem:{prod.imagem}')


                messages.success(request, 'Produto salvo com sucesso.')

                form = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar produto.')
        else:
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')