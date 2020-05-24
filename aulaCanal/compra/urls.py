from django.urls import path, include
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_compra, name='cadastrar_compra'),
    path('consultar/', views.consultar_compra, name='consultar_compra'),
]