from django.shortcuts import render
from .forms import NovoClienteForm, BuscaClienteForm
from django.urls import reverse # permite usar url no formato de template tag ao inves de digitar a url completa
from django.http import HttpResponseRedirect
from .models import Cliente
from ..util.utils import get_object_or_none

# Create your views here.
def cadastrar_cliente(request):
    template_name = 'cadastrar_cliente.html'

    cliente_form = NovoClienteForm()

    if request.POST:
        cliente_form = NovoClienteForm(data=request.POST)

        if cliente_form.is_valid():
            cliente_form.save()

        return HttpResponseRedirect(reverse('home'))

    context = {
        'cliente_form': cliente_form
    }

    return render(request, template_name, context)


def consultar_cliente(request):
    template_name = 'consultar_cliente.html'

    lista_cliente = []
    busca_cliente_form = BuscaClienteForm()
    vazio = False

    if request.POST:
        busca_cliente_form = BuscaClienteForm(request.POST)

        if busca_cliente_form.is_valid():
            campo_busca = busca_cliente_form.cleaned_data['campo_busca']

            lista_cliente = Cliente.objects.all().filter(nome__icontains=campo_busca)
        
        if not lista_cliente:
            vazio = True

    context = {
        'busca_cliente_form': busca_cliente_form,
        'lista_cliente': lista_cliente,
        'vazio': vazio
    }

    return render(request, template_name, context)


def deletar_cliente(request, pk):
    template_name = 'deletar_cliente.html'

    cliente = get_object_or_none(Cliente, pk=pk)

    if request.POST:
        if cliente:
            cliente.delete()
        
        return HttpResponseRedirect(reverse('home'))

    context = {
        'cliente': cliente
    }

    return render(request, template_name, context)


def editar_cliente(request, pk):
    template_name = 'editar_cliente.html'

    cliente = get_object_or_none(Cliente, pk=pk)

    if cliente:
        cliente_editar_form = NovoClienteForm(instance=cliente)
    else:
        cliente_editar_form = NovoClienteForm()

    if request.POST:
        cliente_editar_form = NovoClienteForm(data=request.POST, instance=cliente)

        if cliente_editar_form.is_valid():
            cliente_editar_form.save()

        return HttpResponseRedirect(reverse('home'))

    context = {
        'cliente_editar_form': cliente_editar_form
    }

    return render(request, template_name, context)