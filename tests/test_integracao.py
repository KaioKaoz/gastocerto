from unittest.mock import patch, MagicMock
import pytest
from gastos.services import buscar_cotacoes


# Teste 1: API responde corretamente → retorna cotações
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


# Teste 2: API fora do ar → retorna None sem quebrar o app
@patch("gastos.services.requests.get")
def test_buscar_cotacoes_falha_na_api(mock_get):
    mock_get.side_effect = Exception("Connection error")

    resultado = buscar_cotacoes()

    assert resultado is None


# Teste 3: A view principal continua funcionando mesmo sem cotações
@pytest.mark.django_db
@patch("gastos.views.buscar_cotacoes", return_value=None)
def test_lista_sem_cotacoes(mock_cotacoes, client):
    response = client.get("/")
    assert response.status_code == 200