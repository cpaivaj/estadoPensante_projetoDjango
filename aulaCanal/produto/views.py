from django.shortcuts import render
from .forms import NovoProdutoForm, BuscaProdutoForm

# Create your views here.
def cadastrar_produto(request):
    template_name = 'cadastrar_produto.html'

    produto_form = NovoProdutoForm()

    if request.POST:
        print('salva produto')

    context = {
        'produto_form': produto_form
    }

    return render(request, template_name, context)


def consultar_produto(request):
    template_name = 'consultar_produto.html'

    busca_produto_form = BuscaProdutoForm()

    if request.POST:
        print('busca produto')

    context = {
        'busca_produto_form': busca_produto_form
    }

    return render(request, template_name, context)