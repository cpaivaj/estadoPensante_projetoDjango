from django.shortcuts import render
from .forms import NovaCompraForm, BuscaCompraForm

# Create your views here.
def cadastrar_compra(request):
    template_name = 'cadastrar_compra.html'

    compra_form = NovaCompraForm()

    if request.POST:
        print('salva compra')

    context = {
        'compra_form': compra_form
    }

    return render(request, template_name, context)


def consultar_compra(request):
    template_name = 'consultar_compra.html'

    busca_compra_form = BuscaCompraForm()

    if request.POST:
        print('busca compra')

    context = {
        'busca_compra_form': busca_compra_form
    }

    return render(request, template_name, context)