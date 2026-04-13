"""
Testes automatizados para as views do app gastos.
"""

import pytest
from django.urls import reverse

from gastos.models import Gasto


@pytest.mark.django_db
def test_lista_gastos_retorna_200(client):
    """A página principal deve retornar status 200."""
    response = client.get(reverse("lista_gastos"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_lista_exibe_gastos_cadastrados(client):
    """Gastos criados devem aparecer na listagem."""
    Gasto.objects.create(descricao="Mercado", valor=150.0, categoria="alimentacao")
    response = client.get(reverse("lista_gastos"))
    assert "Mercado" in response.content.decode()


@pytest.mark.django_db
def test_adicionar_gasto_get_retorna_200(client):
    """Formulário de adição deve retornar status 200."""
    response = client.get(reverse("adicionar_gasto"))
    assert response.status_code == 200


@pytest.mark.django_db
def test_adicionar_gasto_post_valido_redireciona(client):
    """POST válido deve criar gasto e redirecionar para lista."""
    response = client.post(
        reverse("adicionar_gasto"),
        {"descricao": "Uber", "valor": "18.50", "categoria": "transporte"},
    )
    assert response.status_code == 302
    assert Gasto.objects.filter(descricao="Uber").exists()


@pytest.mark.django_db
def test_adicionar_gasto_post_invalido_nao_redireciona(client):
    """POST com valor inválido não deve criar gasto."""
    response = client.post(
        reverse("adicionar_gasto"),
        {"descricao": "Teste", "valor": "-5.00", "categoria": "outros"},
    )
    assert response.status_code == 200
    assert Gasto.objects.count() == 0


@pytest.mark.django_db
def test_remover_gasto_post_remove_e_redireciona(client):
    """POST na view de remoção deve deletar o gasto."""
    gasto = Gasto.objects.create(descricao="Cinema", valor=30.0, categoria="lazer")
    response = client.post(reverse("remover_gasto", args=[gasto.pk]))
    assert response.status_code == 302
    assert not Gasto.objects.filter(pk=gasto.pk).exists()


@pytest.mark.django_db
def test_remover_gasto_inexistente_retorna_404(client):
    """Tentar remover ID inexistente deve retornar 404."""
    response = client.post(reverse("remover_gasto", args=[9999]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_filtro_por_categoria(client):
    """Filtro deve exibir apenas gastos da categoria selecionada."""
    Gasto.objects.create(descricao="Almoço", valor=20.0, categoria="alimentacao")
    Gasto.objects.create(descricao="Ônibus", valor=4.5, categoria="transporte")
    response = client.get(reverse("lista_gastos") + "?categoria=alimentacao")
    content = response.content.decode()
    assert "Almoço" in content
    assert "Ônibus" not in content
