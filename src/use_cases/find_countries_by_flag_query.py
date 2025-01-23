from dataclasses import dataclass

import numpy as np

from src.domain.countries_rest_client import CountriesRestClient


@dataclass
class FindCountriesByFlagQueryResponse:
    flag: str
    booleans: dict


class FindCountriesByFlagQueryHandler:
    def __init__(self, countries_client: CountriesRestClient):
        self.countries_client = countries_client

    def execute(self) -> FindCountriesByFlagQueryResponse:
        countries = self.countries_client.find_countries_by_flag()
        flag = np.random.choice(list(countries.values()))
        booleans = {}
        for name in countries.keys():
            booleans[name] = True if countries[name] == flag else False
        return FindCountriesByFlagQueryResponse(flag, booleans)
