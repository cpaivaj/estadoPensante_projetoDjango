from django.shortcuts import render

# Create your views here.
def cadastrar_compra(request):
    template_name = 'cadastrar_compra.html'

    context = {}

    return render(request, template_name, context)


def consultar_compra(request):
    template_name = 'consultar_compra.html'

    context = {}

    return render(request, template_name, context)