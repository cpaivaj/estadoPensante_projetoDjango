from django.db import models
from aulaCanal.cliente.models import Cliente
from aulaCanal.produto.models import Produto

# Create your models here.
class Compra(models.Model):
    descricao = models.TextField('Descrição', blank=False)
    
    cliente = models.ForeignKey(
        Cliente,
        related_name = 'cliente_compra',
        verbose_name = 'Cliente',
        on_delete = models.CASCADE,
        blank=False,
        null=False
    )

    produto = models.ForeignKey(
        Produto,
        related_name = 'produto_compra',
        verbose_name = 'Produto',
        on_delete = models.CASCADE,
        blank=False,
        null=False
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.descricao

    class Meta:
        db_table = 'COMPRA'
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'