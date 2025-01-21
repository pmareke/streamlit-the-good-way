import numpy as np
import requests
from retry import retry


class HttpCountriesRestClient:
    def find_countries_by_flag(self, max: int = 3) -> tuple[str, dict]:
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, max)
        selected_countries = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            flag = country["flags"]["svg"]
            selected_countries[name] = flag
        flag = np.random.choice(list(selected_countries.keys()))

        booleans = {}
        for idx, name in enumerate(selected_countries.keys()):
            booleans[name] = True if name == flag else False
        return selected_countries[flag], booleans

    @retry(tries=3)
    def find_countries_by_capital(self, max: int = 3) -> tuple[str, dict]:
        response = requests.get(
            "https://restcountries.com/v3.1/all?fields=name,capital"
        )
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, max)
        selected_countries = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            capital = country["capital"][0]
            selected_countries[name] = capital

        capital = np.random.choice(list(selected_countries.keys()))
        booleans = {}
        for idx, name in enumerate(selected_countries.keys()):
            booleans[name] = True if name == capital else False
        return selected_countries[capital], booleans


class HttpCountriesRestClientFactory:
    @staticmethod
    def make() -> HttpCountriesRestClient:
        return HttpCountriesRestClient()
