import streamlit as st

from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.image import Image
from src.delivery.streamlit.components.sub_header import SubHeader
from src.domain.component import Component
from src.infrastructure.http_countries_rest_client import HttpCountriesRestClient


class FlagTab(Component):
    def render(self) -> None:
        sub_header = SubHeader("Which country does this flag belong to?")
        sub_header.render()

        if not st.session_state.get("flag_countries"):
            countries_client = HttpCountriesRestClient()
            flag, booleans = countries_client.find_countries_by_flag()
            st.session_state.flag = flag
            st.session_state.flag_countries = booleans

        if st.session_state.get("flag"):
            flag = st.session_state.flag
            image = Image(flag)
            image.render()

        for name, is_ok in st.session_state.flag_countries.items():
            key = f"country_button_{name}"
            button = Button(key, name, self._callback)
            button.render(is_ok)

        divider = Divider()
        divider.render()

        restart = Button("country_play_again", "Play again!", self._play_again_callback)
        restart.render()

    def _callback(self, is_ok: bool) -> None:
        if is_ok:
            st.success("Correct!")
        else:
            st.error("Incorrect!")

    def _play_again_callback(self) -> None:
        st.session_state.pop("flag_countries")
        st.session_state.pop("flag")
        st.rerun()
