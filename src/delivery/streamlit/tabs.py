import streamlit as st

from src.domain.component import Component


class Tabs(Component):
    def __init__(self) -> None:
        self.items: dict[str, Component] = {}

    def add(self, name: str, component: Component) -> None:
        self.items[name] = component

    def render(self) -> None:
        tabs = st.tabs(list(self.items.keys()))

        for index, _tab in enumerate(tabs):
            with _tab:
                components = list(self.items.values())
                components[index].render()
