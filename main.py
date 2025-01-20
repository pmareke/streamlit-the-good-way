import streamlit as st

st.title("Fun with Flags")

button = st.button("Play again!")

if button:
    st.rerun()

st.write("Which country does this flag belong to?")


def _get_random_flag() -> tuple[str, dict]:
    countries = {
        "Spain": True,
        "France": False,
        "Germany": False,
    }
    return ("https://flagcdn.com/es.svg", countries)


flag, countries = _get_random_flag()

st.image(flag)

for idx, (name, is_ok) in enumerate(countries.items()):
    button = st.button(name, key=f"button_{name}")
    if button:
        if is_ok:
            st.write("Correct!")
        else:
            st.write("Incorrect, try again!")
