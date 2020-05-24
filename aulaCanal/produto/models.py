from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    
    CHOICES_PRODUTO = (
        (0, 'Outros'),
        (1, 'Ferro'),
        (2, 'Madeira'),
        (3, 'Plástico')
    )

    tipo_produto = models.IntegerField(
        'Tipo de Produto',
        default=0,
        choices=CHOICES_PRODUTO,
        blank=True
    )

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'PRODUTO'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'