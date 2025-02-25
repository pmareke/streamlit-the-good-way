from src.delivery.streamlit.app import App
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory
from src.use_cases.find_countries_by_capital_query_handler import (
    FindCountriesByCapitalQueryHandler,
)
from src.use_cases.find_countries_by_flag_query_handler import (
    FindCountriesByFlagQueryHandler,
)

countries_client = HttpCountriesRestClientFactory.make()

flag_handler = FindCountriesByFlagQueryHandler(countries_client)
capital_handler = FindCountriesByCapitalQueryHandler(countries_client)

app = App(flag_handler, capital_handler)
app.render()
