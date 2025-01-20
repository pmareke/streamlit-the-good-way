from src.delivery.streamlit.components.header import Header
from src.delivery.streamlit.components.tabs import Tabs
from src.delivery.streamlit.tabs.capital import CapitalTab
from src.delivery.streamlit.tabs.flag import FlagTab
from src.domain.component import Component


class App(Component):
    def render(self) -> None:
        header = Header("Fun with flags and capitals!")
        header.render()

        tabs = Tabs()

        flag = FlagTab()
        tabs.add("Guess the country by the flag", flag)

        capital = CapitalTab()
        tabs.add("Guess the country by the capital", capital)

        tabs.render()
