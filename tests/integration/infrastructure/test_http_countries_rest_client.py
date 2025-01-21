from expects import be_none, contain, expect, have_length

from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory


class TestHttpCountriesClientIntegration:
    def test_find_countries_by_flag(self) -> None:
        max = 1
        client = HttpCountriesRestClientFactory.make()

        flag, booleans = client.find_countries_by_flag(max)

        expect(flag).to(contain("https://flagcdn.com"))
        expect(booleans).to(have_length(max))

    def test_find_countries_by_capital(self) -> None:
        max = 1
        client = HttpCountriesRestClientFactory.make()

        capital, booleans = client.find_countries_by_capital(max)

        expect(capital).not_to(be_none)
        expect(booleans).to(have_length(max))
