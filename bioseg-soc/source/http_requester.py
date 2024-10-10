import requests


class HttpRequester:
    def get_data(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()  
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro : {e}")
            return []

