import numpy as np
import requests
import streamlit as st

st.header("Fun with Flags")

st.subheader("Which country does this flag belong to?")

if not st.session_state.get("selected_countries"):
    response = requests.get("https://restcountries.com/v3.1/all?fields=name,flags")
    json_response = response.json()
    length = len(json_response)
    random_idx = np.random.randint(0, length, 3)
    selected_countries = {}
    for idx in random_idx:
        country = json_response[idx]
        name = country["name"]["common"]
        flag = country["flags"]["svg"]
        selected_countries[name] = flag
    st.session_state.selected_countries = selected_countries

    random_country = np.random.choice(list(selected_countries.keys()))
    st.session_state.random_country = random_country
    countries = {}
    for idx, (name, flag) in enumerate(selected_countries.items()):
        if name == random_country:
            countries[name] = True
        else:
            countries[name] = False
    st.session_state.countries = countries

if st.session_state.get("random_country"):
    flag = st.session_state.selected_countries[st.session_state.random_country]
    st.image(flag)


for idx, (name, is_ok) in enumerate(st.session_state.countries.items()):
    key = f"button_{name}"
    button = st.button(name, key=key)
    if button:
        if is_ok:
            st.success("Correct!")
        else:
            st.error("Incorrect!")

st.divider()

restart = st.button("Play again!")
if restart:
    st.session_state.pop("selected_countries")
    st.session_state.pop("random_country")
    st.session_state.pop("countries")
    st.rerun()
