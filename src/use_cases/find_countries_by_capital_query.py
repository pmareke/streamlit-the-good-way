from dataclasses import dataclass

import numpy as np

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient


@dataclass
class FindCountriesByCapitalQueryResponse:
    capital: str
    booleans: dict


class FindCountriesByCapitalQueryHandler:
    def __init__(self, countries_client: HttpCountriesRestClient):
        self.countries_client = countries_client

    def execute(self) -> FindCountriesByCapitalQueryResponse:
        countries = self.countries_client.find_countries_by_capital()
        capital = np.random.choice(list(countries.values()))
        booleans = {}
        for name in countries.keys():
            booleans[name] = True if countries[name] == capital else False
        return FindCountriesByCapitalQueryResponse(capital, booleans)
