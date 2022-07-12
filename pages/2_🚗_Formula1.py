from enum import auto
import streamlit as st
import f1Functions as f1

st.set_page_config(
    page_title="Formula 1",
    page_icon="car",
    layout="wide", 
)

nextRace = f1.getNextRace()

st.title(nextRace.name)

st.text(nextRace.url)
st.text(nextRace.dateTime)
st.text(nextRace.country)