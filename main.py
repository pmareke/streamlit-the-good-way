import numpy as np
import requests
import streamlit as st

st.header("Fun with flags and capitals!")

tab_1, tab_2 = st.tabs(
    [
        "Guess the country by the flag",
        "Guess the country by the capital",
    ]
)

with tab_1:
    st.subheader("Which country does this flag belong to?")

    if not st.session_state.get("selected_countries"):
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, 3)
        selected_capitals = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            flag = country["flags"]["svg"]
            selected_capitals[name] = flag
        st.session_state.selected_countries = selected_capitals

        random_country = np.random.choice(list(selected_capitals.keys()))
        st.session_state.random_country = random_country
        countries = {}
        for idx, name in enumerate(selected_capitals.keys()):
            if name == random_country:
                countries[name] = True
            else:
                countries[name] = False
        st.session_state.countries = countries

    if st.session_state.get("random_country"):
        flag = st.session_state.selected_countries[st.session_state.random_country]
        st.image(flag)

    for idx, (name, is_ok) in enumerate(st.session_state.countries.items()):
        key = f"country_button_{name}"
        button = st.button(name, key=key)
        if button:
            if is_ok:
                st.success("Correct!")
            else:
                st.error("Incorrect!")

    st.divider()

    restart = st.button("Play again!", key="country_play_again")
    if restart:
        st.session_state.pop("selected_countries")
        st.session_state.pop("random_country")
        st.rerun()

with tab_2:
    st.subheader("Which country does this capital belong to?")

    if not st.session_state.get("selected_capitals"):
        response = requests.get(
            "https://restcountries.com/v3.1/all?fields=name,capital"
        )
        json_response = response.json()
        length = len(json_response)
        random_idx = np.random.randint(0, length, 3)
        selected_capitals = {}
        for idx in random_idx:
            country = json_response[idx]
            name = country["name"]["common"]
            capital = country["capital"][0]
            selected_capitals[name] = capital
        st.session_state.selected_capitals = selected_capitals

        random_capital = np.random.choice(list(selected_capitals.keys()))
        st.session_state.random_capital = random_capital
        capitals_countries = {}
        for idx, name in enumerate(selected_capitals.keys()):
            if name == random_capital:
                capitals_countries[name] = True
            else:
                capitals_countries[name] = False
        st.session_state.capitals_countries = capitals_countries

    if st.session_state.get("random_capital"):
        capital = st.session_state.selected_capitals[st.session_state.random_capital]
        st.title(capital)

    for idx, (name, is_ok) in enumerate(st.session_state.capitals_countries.items()):
        key = f"capital_button_{name}"
        button = st.button(name, key=key)
        if button:
            if is_ok:
                st.success("Correct!")
            else:
                st.error("Incorrect!")

    st.divider()

    restart = st.button("Play again!", key="capital_play_again")
    if restart:
        st.session_state.pop("selected_capitals")
        st.session_state.pop("random_capital")
        st.rerun()
