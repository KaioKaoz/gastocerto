import pytest
from unittest.mock import MagicMock, patch

from gastos.services import buscar_cotacoes


@patch("gastos.services.requests.get")
def test_buscar_cotacoes_sucesso(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {
        "USDBRL": {"bid": "5.25"},
        "EURBRL": {"bid": "5.80"},
    }
    mock_get.return_value = mock_response

    resultado = buscar_cotacoes()

    assert resultado is not None
    assert resultado["usd"] == 5.25
    assert resultado["eur"] == 5.80


@patch("gastos.services.requests.get", side_effect=Exception("Connection error"))
def test_buscar_cotacoes_falha_na_api(mock_get):
    resultado = buscar_cotacoes()

    assert resultado is None


@pytest.mark.django_db
@patch("gastos.services.buscar_cotacoes", return_value=None)
def test_lista_sem_cotacoes(mock_cotacoes, client):
    response = client.get("/")
    assert response.status_code == 200