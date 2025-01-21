from expects import expect, have_length

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory


class TestHttpCountriesClientIntegration:
    def test_find_countries_by_flag(self) -> None:
        max = 1
        client = HttpCountriesRestClientFactory.make()

        countries = client.find_countries_by_flag(max)

        expect(countries).to(have_length(max))

    def test_find_countries_by_capital(self) -> None:
        max = 1
        client = HttpCountriesRestClientFactory.make()

        countries = client.find_countries_by_capital(max)

        expect(countries).to(have_length(max))
