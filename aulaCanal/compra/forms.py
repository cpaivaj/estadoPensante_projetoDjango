from django import forms
from .models import Compra

class NovaCompraForm(forms.ModelForm):
    class Meta:
        model = Compra
        fields = [
            'descricao', 'cliente', 'produto'
        ]

class BuscaCompraForm(forms.Form):
    campo_busca = forms.CharField(
        label="Pesquisa", required=False
    )