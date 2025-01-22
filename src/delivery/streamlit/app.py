from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.tabs import Tabs
from src.delivery.streamlit.tabs.capital import CapitalTab
from src.delivery.streamlit.tabs.flag import FlagTab
from src.domain.component import Component
from src.use_cases.find_countries_by_capital_query import (
    FindCountriesByCapitalQueryHandler,
)
from src.use_cases.find_countries_by_flag_query import FindCountriesByFlagQueryHandler


class App(Component):
    def __init__(
        self,
        find_countries_by_flag_query: FindCountriesByFlagQueryHandler,
        find_countries_by_capital_query: FindCountriesByCapitalQueryHandler,
    ) -> None:
        self.find_countries_by_flag_query = find_countries_by_flag_query
        self.find_countries_by_capital_query = find_countries_by_capital_query

    def render(self) -> None:
        header = Header("Fun with flags and capitals!")
        header.render()

        tabs = Tabs()

        flag = FlagTab(self.find_countries_by_flag_query)
        tabs.add("Guess the country by the flag", flag)

        capital = CapitalTab(self.find_countries_by_capital_query)
        tabs.add("Guess the country by the capital", capital)

        tabs.render()
