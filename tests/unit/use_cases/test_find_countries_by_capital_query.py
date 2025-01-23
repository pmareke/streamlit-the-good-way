from doublex import Mimic, Stub
from expects import equal, expect

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient
from src.use_cases.find_countries_by_capital_query import (
    FindCountriesByCapitalQueryHandler,
)


class TestFindCountriesByCapitalQueryHandler:
    def test_find_countries_by_capital(self) -> None:
        capital = "Madrid"
        country = "Spain"
        booleans = {country: True}
        with Mimic(Stub, HttpCountriesRestClient) as countries_rest_client:
            countries = {country: capital}
            countries_rest_client.find_countries_by_capital().returns(countries)
        handler = FindCountriesByCapitalQueryHandler(countries_rest_client)

        response = handler.execute()

        expect(response.capital).to(equal(capital))
        expect(response.booleans).to(equal(booleans))
