from doublex import Mimic, Stub
from expects import equal, expect

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient
from src.use_cases.find_countries_by_flag_query_handler import (
    FindCountriesByFlagQueryHandler,
)


class TestFindFlagByCapitalQueryHandler:
    def test_find_countries_by_capital(self) -> None:
        flag = "https://flagcdn.com/es.svg"
        country = "Spain"
        booleans = {country: True}
        with Mimic(Stub, HttpCountriesRestClient) as countries_rest_client:
            countries = {country: flag}
            countries_rest_client.find_countries_by_flag().returns(countries)
        handler = FindCountriesByFlagQueryHandler(countries_rest_client)

        response = handler.execute()

        expect(response.flag).to(equal(flag))
        expect(response.booleans).to(equal(booleans))
