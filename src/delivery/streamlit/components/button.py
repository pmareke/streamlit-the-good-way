from collections.abc import Callable

import streamlit as st

from src.domain.component import Component


class Button(Component):
    def __init__(
        self,
        key: str,
        label: str,
        callback: Callable,
    ) -> None:
        self.key = key
        self.label = label
        self.callback = callback

    def render(self, is_ok: bool | None = None) -> None:
        _button = st.button(self.label, self.key)
        if _button:
            if is_ok is None:
                self.callback()
            else:
                self.callback(is_ok)
