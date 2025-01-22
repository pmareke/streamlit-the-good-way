import streamlit as st

from src.domain.component import Component


class Title(Component):
    def __init__(self, message: str) -> None:
        self.message = message

    def render(self) -> None:
        st.title(self.message)
