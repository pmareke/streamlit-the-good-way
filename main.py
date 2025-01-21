from src.delivery.streamlit.app import App
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory
from src.use_cases.find_countries_by_capital_query import (
    FindCountriesByCapitalQueryHandler,
)
from src.use_cases.find_countries_by_flag_query import FindCountriesByFlagQueryHandler

countries_client = HttpCountriesRestClientFactory.make()
find_countries_by_flag_query = FindCountriesByFlagQueryHandler(countries_client)
find_countries_by_capital_query = FindCountriesByCapitalQueryHandler(countries_client)

app = App(
    find_countries_by_flag_query,
    find_countries_by_capital_query,
)

app.render()
