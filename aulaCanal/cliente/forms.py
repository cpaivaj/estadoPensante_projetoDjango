from django import forms
from .models import Cliente

class NovoClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'email'
        ]

class BuscaClienteForm(forms.Form):
    campo_busca = forms.CharField(
        label="Pesquisa", required=False
    )