import streamlit as st
import controller.f1Controller as f1
import controller.globalController as globalController
from widgets import f1CardWidget

globalController.setConfig()

nextRace = f1.getNextRace()

# Title
headerMd = f"""
    <style>
        h1 {{
            padding: 0;
        }}
        p {{
            margin-bottom: 0!important;
        }}
    </style>
    🚩 Starting in <strong>{nextRace.getTimeUntil()}</strong> ⬇️
    # <a href="{nextRace.url}" style="text-decoration: none; color: white">{nextRace.name}</a>
"""
st.markdown(headerMd, unsafe_allow_html=True)

# st.text(nextRace.name)
# st.text(nextRace.url)
# st.text(nextRace.round)
# st.text(nextRace.raceDate)
# st.text(nextRace.raceTime)
# st.text('------')

for ev in nextRace.event:
    st.text(ev.name)
    st.text(ev.getDateTime())
    st.text(ev.getFormatedDateTime())
    st.text('----')

# Next Races
nextRacesMd = f"""
    <style>
        h1 {{
            padding: 0;
        }}
        p {{
            margin-bottom: 0!important;
        }}
    </style>
    # <a href="" style="text-decoration: none; color: white">Next Races</a>
"""
st.markdown(nextRacesMd, unsafe_allow_html=True)
st.markdown(f1CardWidget.getF1Card(nextRace), unsafe_allow_html=True)

