from typing import Any, Dict

import requests


class HttpRequester:
    def get(self, url: str, params: Dict[str, str]) -> Dict[str, Any]:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            return {}