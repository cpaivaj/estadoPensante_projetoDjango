from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('consultar/', views.consultar_produto, name='consultar_produto'),
]