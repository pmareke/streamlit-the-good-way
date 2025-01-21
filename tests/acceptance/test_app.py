from expects import equal, expect, have_length
from streamlit.testing.v1 import AppTest


class TestApp:
    def test_app(self) -> None:
        app = AppTest.from_file("main.py")

        at = app.run()

        expect(at.header[0].value).to(equal("Fun with flags and capitals!"))
        expect(at.subheader[0].value).to(
            equal("Which country does this flag belong to?")
        )
        expect(at.button).to(have_length(8))  # 4 in each tab
        expect(at.button[3].label).to(equal("Play again!"))
        expect(at.button[7].label).to(equal("Play again!"))
