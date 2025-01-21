import streamlit as st

from src.domain.component import Component


class SolveButton(Component):
    def __init__(
        self,
        key: str,
        label: str,
    ) -> None:
        self.key = key
        self.label = label

    def render(self, is_ok: bool) -> None:
        _button = st.button(self.label, self.key)
        if _button:
            self._callback(is_ok)

    def _callback(self, is_ok: bool) -> None:
        if is_ok:
            st.success("Correct!")
            return
        st.error("Incorrect!")
