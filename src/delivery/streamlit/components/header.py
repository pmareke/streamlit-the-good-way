import streamlit as st

from src.domain.component import Component


class Header(Component):
    def __init__(self, message: str) -> None:
        self.message = message

    def render(self) -> None:
        st.header(self.message)
