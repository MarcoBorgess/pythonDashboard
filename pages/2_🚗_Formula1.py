import streamlit as st
import f1Functions as f1
import globalFunctions
from widgets import f1CardWidget

globalFunctions.setConfig()

nextRace = f1.getNextRace()

headerMd = f"""
    <style>
        h1 {{
            padding: 0;
        }}
        p {{
            margin-bottom: 0!important;
        }}
    </style>
    🚩 Starting in <strong>{nextRace.timeUntil}</strong> ⬇️
    # <a href="{nextRace.url}" style="text-decoration: none; color: white">{nextRace.name}</a>
"""
# Title
st.markdown(headerMd, unsafe_allow_html=True)

st.markdown(f1CardWidget.getF1Card(nextRace.name, nextRace.mainRaceTime), unsafe_allow_html=True)

