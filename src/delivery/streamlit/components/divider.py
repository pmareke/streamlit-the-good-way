import streamlit as st

from src.domain.component import Component


class Divider(Component):
    def render(self) -> None:
        st.divider()
