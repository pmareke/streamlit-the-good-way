from src.delivery.streamlit.app import App
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClientFactory

app = App()

countries_client = HttpCountriesRestClientFactory.make()
app.render(countries_client)
