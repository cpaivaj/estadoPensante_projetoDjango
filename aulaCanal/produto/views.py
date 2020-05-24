from django.shortcuts import render

# Create your views here.
def cadastrar_produto(request):
    template_name = 'cadastrar_produto.html'

    context = {}

    return render(request, template_name, context)


def consultar_produto(request):
    template_name = 'consultar_produto.html'

    context = {}

    return render(request, template_name, context)