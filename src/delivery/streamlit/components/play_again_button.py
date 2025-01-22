import streamlit as st

from src.domain.component import Component


class PlayAgainButton(Component):
    def __init__(self, key: str, label: str) -> None:
        self.key = key
        self.label = label

    def render(self) -> None:
        _button = st.button(self.label, self.key)
        if _button:
            self._play_again_callback()

    def _play_again_callback(self) -> None:
        st.session_state.clear()
        st.rerun()
