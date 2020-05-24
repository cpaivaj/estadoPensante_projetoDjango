from django.shortcuts import render

# Create your views here.
def cadastrar_cliente(request):
    template_name = 'cadastrar_cliente.html'

    context = {}

    return render(request, template_name, context)


def consultar_cliente(request):
    template_name = 'consultar_cliente.html'

    context = {}

    return render(request, template_name, context)


def deletar_cliente(request):
    template_name = 'deletar_cliente.html'

    context = {}

    return render(request, template_name, context)


def editar_cliente(request):
    template_name = 'editar_cliente.html'

    context = {}

    return render(request, template_name, context)