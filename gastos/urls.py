"""
URLs do app gastos.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_gastos, name="lista_gastos"),
    path("adicionar/", views.adicionar_gasto, name="adicionar_gasto"),
    path("editar/<int:pk>/", views.editar_gasto, name="editar_gasto"),
    path("remover/<int:pk>/", views.remover_gasto, name="remover_gasto"),
]
