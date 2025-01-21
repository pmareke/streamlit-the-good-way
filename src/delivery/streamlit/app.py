from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.tabs import Tabs
from src.delivery.streamlit.tabs.capital import CapitalTab
from src.delivery.streamlit.tabs.flag import FlagTab
from src.domain.component import Component
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient


class App(Component):
    def render(self, countries_client: HttpCountriesRestClient) -> None:
        header = Header("Fun with flags and capitals!")
        header.render()

        tabs = Tabs()

        flag = FlagTab(countries_client)
        tabs.add("Guess the country by the flag", flag)

        capital = CapitalTab(countries_client)
        tabs.add("Guess the country by the capital", capital)

        tabs.render()
