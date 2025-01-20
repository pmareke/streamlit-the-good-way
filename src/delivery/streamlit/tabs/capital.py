import streamlit as st

from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.sub_header import SubHeader
from src.delivery.streamlit.components.title import Title
from src.domain.component import Component
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient


class CapitalTab(Component):
    def render(self) -> None:
        subheader = SubHeader("Which country does this capital belong to?")
        subheader.render()

        if not st.session_state.get("capital_countries"):
            countries_client = HttpCountriesRestClient()
            capital, booleans = countries_client.find_countries_by_capital()
            st.session_state.capital = capital
            st.session_state.capital_countries = booleans

        if st.session_state.get("capital"):
            capital = st.session_state.capital
            title = Title(capital)
            title.render()

        for name, is_ok in st.session_state.capital_countries.items():
            key = f"capital_button_{name}"
            button = Button(key, name, self._callback)
            button.render(is_ok)

        divider = Divider()
        divider.render()

        restart = Button("capital_play_again", "Play again!", self._play_again_callback)
        restart.render()

    def _callback(self, is_ok: bool) -> None:
        if is_ok:
            st.success("Correct!")
        else:
            st.error("Incorrect!")

    def _play_again_callback(self) -> None:
        st.session_state.pop("capital")
        st.session_state.pop("capital_countries")
        st.rerun()
