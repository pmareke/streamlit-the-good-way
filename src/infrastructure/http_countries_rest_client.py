import numpy as np
import requests
from retry import retry

from src.domain.countries_rest_client import CountriesRestClient


class HttpCountriesRestClient(CountriesRestClient):
    API_URL = "https://restcountries.com/v3.1/all"

    @retry(tries=3)
    def find_countries_by_flag(self, max: int = 3) -> dict:
        response = requests.get(f"{self.API_URL}?fields=name,flags")
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, max)
        countries = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            flag = country["flags"]["svg"]
            countries[name] = flag
        return countries

    @retry(tries=3)
    def find_countries_by_capital(self, max: int = 3) -> dict:
        response = requests.get(f"{self.API_URL}?fields=name,capital")
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, max)
        countries = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            capital = country["capital"][0]
            countries[name] = capital
        return countries


class HttpCountriesRestClientFactory:
    @staticmethod
    def make() -> HttpCountriesRestClient:
        return HttpCountriesRestClient()
