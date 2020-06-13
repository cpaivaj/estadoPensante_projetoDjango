from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('consultar/', views.consultar_cliente, name='consultar_cliente'),
    path('deletar/<int:pk>/', views.deletar_cliente, name='deletar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
]