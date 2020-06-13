from django.shortcuts import render
from .forms import NovaCompraForm, BuscaCompraForm
from django.urls import reverse # permite usar url no formato de template tag ao inves de digitar a url completa
from django.http import HttpResponseRedirect


# Create your views here.
def cadastrar_compra(request):
    template_name = 'cadastrar_compra.html'

    compra_form = NovaCompraForm()

    if request.POST:
        compra_form = NovaCompraForm(data=request.POST)

        if compra_form.is_valid():
            compra_form.save()

        return HttpResponseRedirect(reverse('home'))

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