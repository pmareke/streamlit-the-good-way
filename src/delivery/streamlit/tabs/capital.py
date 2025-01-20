import numpy as np
import requests
import streamlit as st

from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.sub_header import SubHeader
from src.delivery.streamlit.components.title import Title
from src.domain.component import Component


class CapitalTab(Component):
    def render(self) -> None:
        subheader = SubHeader("Which country does this capital belong to?")
        subheader.render()

        if not st.session_state.get("selected_capitals"):
            response = requests.get(
                "https://restcountries.com/v3.1/all?fields=name,capital"
            )
            json_response = response.json()
            length = len(json_response)
            random_idx = np.random.randint(0, length, 3)
            selected_capitals = {}
            for idx in random_idx:
                country = json_response[idx]
                name = country["name"]["common"]
                capital = country["capital"][0]
                selected_capitals[name] = capital
            st.session_state.selected_capitals = selected_capitals

            random_capital = np.random.choice(list(selected_capitals.keys()))
            st.session_state.random_capital = random_capital
            capitals_countries = {}
            for idx, name in enumerate(selected_capitals.keys()):
                if name == random_capital:
                    capitals_countries[name] = True
                else:
                    capitals_countries[name] = False
            st.session_state.capitals_countries = capitals_countries

        if st.session_state.get("random_capital"):
            capital = st.session_state.selected_capitals[
                st.session_state.random_capital
            ]
            title = Title(capital)
            title.render()

        for idx, (name, is_ok) in enumerate(
            st.session_state.capitals_countries.items()
        ):
            key = f"capital_button_{name}"
            button = Button(key, name, self._callback, is_ok)
            button.render()

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
        st.session_state.pop("selected_capitals")
        st.session_state.pop("random_capital")
        st.rerun()
