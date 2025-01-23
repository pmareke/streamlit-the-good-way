from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.tabs import Tabs
from src.delivery.streamlit.tabs.capital import CapitalTab
from src.delivery.streamlit.tabs.flag import FlagTab
from src.domain.component import Component
from src.use_cases.find_countries_by_capital_query_handler import (
    FindCountriesByCapitalQueryHandler,
)
from src.use_cases.find_countries_by_flag_query_handler import (
    FindCountriesByFlagQueryHandler,
)


class App(Component):
    def __init__(
        self,
        flag_handler: FindCountriesByFlagQueryHandler,
        capital_handler: FindCountriesByCapitalQueryHandler,
    ) -> None:
        self.flag_handler = flag_handler
        self.capital_handler = capital_handler

    def render(self) -> None:
        header = Header("Fun with flags and capitals!")
        header.render()

        tabs = Tabs()

        flag_tab = FlagTab(self.flag_handler)
        tabs.add("Guess the country by the flag", flag_tab)

        capital_tab = CapitalTab(self.capital_handler)
        tabs.add("Guess the country by the capital", capital_tab)

        tabs.render()
