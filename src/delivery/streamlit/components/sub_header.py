import streamlit as st

from src.domain.component import Component


class SubHeader(Component):
    def __init__(self, message: str) -> None:
        self.message = message

    def render(self) -> None:
        st.subheader(self.message)
