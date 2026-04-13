"""
Testes automatizados para os modelos do app gastos.
"""

import pytest
from django.core.exceptions import ValidationError

from gastos.models import Gasto


@pytest.mark.django_db
def test_criar_gasto_valido():
    """Caminho feliz: gasto válido é criado corretamente."""
    gasto = Gasto.objects.create(
        descricao="Almoço", valor=25.50, categoria="alimentacao"
    )
    assert gasto.pk is not None
    assert gasto.descricao == "Almoço"
    assert float(gasto.valor) == 25.50
    assert gasto.categoria == "alimentacao"


@pytest.mark.django_db
def test_str_gasto():
    """Representação string do model está correta."""
    gasto = Gasto.objects.create(
        descricao="Passagem", valor=4.50, categoria="transporte"
    )
    assert "Passagem" in str(gasto)
    assert "transporte" in str(gasto)


@pytest.mark.django_db
def test_valor_negativo_levanta_erro():
    """Valor negativo deve levantar ValidationError."""
    with pytest.raises(ValidationError):
        Gasto.objects.create(
            descricao="Teste", valor=-10.0, categoria="outros"
        )


@pytest.mark.django_db
def test_valor_zero_levanta_erro():
    """Valor zero deve levantar ValidationError."""
    with pytest.raises(ValidationError):
        Gasto.objects.create(
            descricao="Teste", valor=0, categoria="outros"
        )


@pytest.mark.django_db
def test_ordenacao_por_data_decrescente():
    """Gastos devem ser ordenados do mais recente para o mais antigo."""
    Gasto.objects.create(descricao="Primeiro", valor=10.0, categoria="outros")
    Gasto.objects.create(descricao="Segundo", valor=20.0, categoria="outros")
    gastos = list(Gasto.objects.all())
    assert gastos[0].descricao == "Segundo"


@pytest.mark.django_db
def test_categoria_padrao_e_outros():
    """Categoria padrão deve ser 'outros'."""
    gasto = Gasto.objects.create(descricao="Genérico", valor=5.0)
    assert gasto.categoria == "outros"
