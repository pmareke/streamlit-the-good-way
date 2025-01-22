from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestPlayAgainButton:
    def test_click_button(self) -> None:
        key = "play_again_button"
        label = "Click me!"

        def create_app(key: str, label: str) -> None:
            from src.delivery.streamlit.components.play_again_button import (
                PlayAgainButton,
            )

            internal_app = PlayAgainButton(key, label)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(key, label))

        at = app.run()

        expect(at.button[0].label).to(equal(label))
