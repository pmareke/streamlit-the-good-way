from expects import equal, expect
from streamlit.testing.v1 import AppTest


class TestTabs:
    def test_tab(self) -> None:
        tab_name = "any-text"

        def create_app(tab_name: str) -> None:
            from src.delivery.streamlit.components.tabs import Tabs
            from src.delivery.streamlit.components.title import Title

            tabs = Tabs()

            title = Title("any-text")
            tabs.add(tab_name, title)

            tabs.render()

        app = AppTest.from_function(create_app, args=(tab_name,))

        at = app.run()

        expect(at.title[0].value).to(equal(tab_name))
