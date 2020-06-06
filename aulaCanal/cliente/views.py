from django.shortcuts import render
from .forms import NovoClienteForm, BuscaClienteForm

# Create your views here.
def cadastrar_cliente(request):
    template_name = 'cadastrar_cliente.html'

    cliente_form = NovoClienteForm()

    if request.POST:
        print('salva cliente')

    context = {
        'cliente_form': cliente_form
    }

    return render(request, template_name, context)


def consultar_cliente(request):
    template_name = 'consultar_cliente.html'

    busca_cliente_form = BuscaClienteForm()

    if request.POST:
        print('busca cliente')

    context = {
        'busca_cliente_form': busca_cliente_form
    }

    return render(request, template_name, context)


def deletar_cliente(request):
    template_name = 'deletar_cliente.html'

    context = {}

    return render(request, template_name, context)


def editar_cliente(request):
    template_name = 'editar_cliente.html'

    context = {}

    return render(request, template_name, context)