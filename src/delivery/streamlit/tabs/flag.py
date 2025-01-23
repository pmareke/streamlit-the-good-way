import streamlit as st

from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.image import Image
from src.delivery.streamlit.components.play_again_button import PlayAgainButton
from src.delivery.streamlit.components.solve_button import SolveButton
from src.delivery.streamlit.components.sub_header import SubHeader
from src.domain.component import Component
from src.use_cases.find_countries_by_flag_query_handler import (
    FindCountriesByFlagQueryHandler,
)


class FlagTab(Component):
    def __init__(self, handler: FindCountriesByFlagQueryHandler) -> None:
        self.handler = handler

    def render(self) -> None:
        sub_header = SubHeader("Which country does this flag belong to?")
        sub_header.render()

        if not st.session_state.get("flag_countries"):
            response = self.handler.execute()
            st.session_state.flag = response.flag
            st.session_state.flag_countries = response.booleans

        if st.session_state.get("flag"):
            flag = st.session_state.flag
            image = Image(flag)
            image.render()

        self._render_game_buttons()

        divider = Divider()
        divider.render()

        restart = PlayAgainButton("country_play_again", "Play again!")
        restart.render()

    def _render_game_buttons(self) -> None:
        for name, is_ok in st.session_state.flag_countries.items():
            key = f"country_button_{name}"
            button = SolveButton(key, name, is_ok)
            button.render()
