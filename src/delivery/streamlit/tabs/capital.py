import streamlit as st

from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.play_again_button import PlayAgainButton
from src.delivery.streamlit.components.solve_button import SolveButton
from src.delivery.streamlit.components.sub_header import SubHeader
from src.delivery.streamlit.components.title import Title
from src.domain.component import Component
from src.use_cases.find_countries_by_capital_query_handler import (
    FindCountriesByCapitalQueryHandler,
)


class CapitalTab(Component):
    def __init__(self, handler: FindCountriesByCapitalQueryHandler) -> None:
        self.handler = handler

    def render(self) -> None:
        subheader = SubHeader("Which country does this capital belong to?")
        subheader.render()

        if not st.session_state.get("capital_countries"):
            response = self.handler.execute()
            st.session_state.capital = response.capital
            st.session_state.capital_countries = response.booleans

        if st.session_state.get("capital"):
            capital = st.session_state.capital
            title = Title(capital)
            title.render()

        self._render_game_buttons()

        divider = Divider()
        divider.render()

        restart = PlayAgainButton("capital_play_again", "Play again!")
        restart.render()

    def _render_game_buttons(self) -> None:
        for name, is_ok in st.session_state.capital_countries.items():
            key = f"capital_button_{name}"
            button = SolveButton(key, name, is_ok)
            button.render()
