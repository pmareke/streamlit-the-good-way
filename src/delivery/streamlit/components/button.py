from collections.abc import Callable

import streamlit as st

from src.domain.component import Component


class Button(Component):
    def __init__(
        self,
        key: str,
        label: str,
        callback: Callable,
        is_ok: bool | None = None,
    ) -> None:
        self.key = key
        self.label = label
        self.callback = callback
        self.is_ok = is_ok

    def render(self) -> None:
        _button = st.button(self.label, self.key)
        if _button:
            self.callback(self.is_ok)
