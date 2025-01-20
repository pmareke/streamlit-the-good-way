import streamlit as st

from src.domain.component import Component


class Image(Component):
    def __init__(self, url: str) -> None:
        self.url = url

    def render(self) -> None:
        st.image(self.url)
