import requests

AWESOMEAPI_URL = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"


def buscar_cotacoes():
    """
    Busca cotações de USD e EUR em BRL na AwesomeAPI.
    Retorna dict com os dados ou None em caso de falha.
    """
    try:
        response = requests.get(AWESOMEAPI_URL, timeout=5)
        response.raise_for_status()
        dados = response.json()
        return {
            "usd": float(dados["USDBRL"]["bid"]),
            "eur": float(dados["EURBRL"]["bid"]),
        }
    except (requests.RequestException, KeyError, ValueError):
        return None