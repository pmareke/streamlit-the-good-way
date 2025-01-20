import numpy as np
import requests
import streamlit as st

from src.delivery.streamlit.components.button import Button
from src.delivery.streamlit.components.divider import Divider
from src.delivery.streamlit.components.image import Image
from src.delivery.streamlit.components.sub_header import SubHeader
from src.domain.component import Component


class FlagTab(Component):
    def render(self) -> None:
        sub_header = SubHeader("Which country does this flag belong to?")
        sub_header.render()

        if not st.session_state.get("selected_countries"):
            response = requests.get(
                "https://restcountries.com/v3.1/all?fields=name,flags"
            )
            json_response = response.json()
            length = len(json_response)
            random_idx = np.random.randint(0, length, 3)
            selected_capitals = {}
            for idx in random_idx:
                country = json_response[idx]
                name = country["name"]["common"]
                flag = country["flags"]["svg"]
                selected_capitals[name] = flag
            st.session_state.selected_countries = selected_capitals

            random_country = np.random.choice(list(selected_capitals.keys()))
            st.session_state.random_country = random_country
            countries = {}
            for idx, name in enumerate(selected_capitals.keys()):
                if name == random_country:
                    countries[name] = True
                else:
                    countries[name] = False
            st.session_state.countries = countries

        if st.session_state.get("random_country"):
            flag = st.session_state.selected_countries[st.session_state.random_country]
            image = Image(flag)
            image.render()

        for idx, (name, is_ok) in enumerate(st.session_state.countries.items()):
            key = f"country_button_{name}"
            button = Button(key, name, self._callback, is_ok)
            button.render()

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
        st.session_state.pop("selected_countries")
        st.session_state.pop("random_country")
        st.rerun()
