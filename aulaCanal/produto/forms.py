from django import forms
from .models import Produto

class NovoProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome', 'tipo_produto'
        ]

class BuscaProdutoForm(forms.Form):
    campo_busca = forms.CharField(
        label="Pesquisa", required=False
    )