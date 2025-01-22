from expects import be_none, expect
from streamlit.testing.v1 import AppTest


class TestDivider:
    def test_render(self) -> None:
        def create_app() -> None:
            from src.delivery.streamlit.components.divider import Divider

            internal_app = Divider()

            internal_app.render()

        app = AppTest.from_function(create_app)

        at = app.run()

        expect(at.divider[0]).not_to(be_none)
