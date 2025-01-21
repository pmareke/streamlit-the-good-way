from src.delivery.streamlit.app import App
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient

countries_client = HttpCountriesRestClient()
app = App()
app.render(countries_client)
