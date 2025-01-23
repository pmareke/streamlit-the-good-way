from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTitle:
    def test_render(self) -> None:
        message = "Test message"

        def create_app(message: str) -> None:
            from src.delivery.streamlit.components.title import Title

            internal_app = Title(message)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(message,))

        at = app.run()

        expect(at.title[0].value).to(equal(message))