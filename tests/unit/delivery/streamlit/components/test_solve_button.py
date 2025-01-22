from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestSolveButton:
    def test_click_correct_button(self) -> None:
        key = "solve_button"
        label = "Click me!"

        def create_app(key: str, label: str) -> None:
            from src.delivery.streamlit.components.solve_button import SolveButton

            internal_app = SolveButton(key, label, True)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(key, label))

        at = app.run()

        expect(at.button[0].label).to(equal(label))

        at.button[0].click()

        app.run()

        expect(at.success[0].value).to(equal("Correct!"))

    def test_click_ibcorrect_button(self) -> None:
        key = "solve_button"
        label = "Click me!"

        def create_app(key: str, label: str) -> None:
            from src.delivery.streamlit.components.solve_button import SolveButton

            internal_app = SolveButton(key, label, False)

            internal_app.render()

        app = AppTest.from_function(create_app, args=(key, label))

        at = app.run()

        expect(at.button[0].label).to(equal(label))

        at.button[0].click()

        app.run()

        expect(at.error[0].value).to(equal("Incorrect!"))
