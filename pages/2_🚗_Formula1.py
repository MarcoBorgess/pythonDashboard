import pandas as pd
import streamlit as st
import controller.f1Controller as f1
import controller.globalController as globalController
from widgets import f1NextRacesCardWidget, f1NextEventsCardWidget, f1StandingsWidget

globalController.setConfig()

nextRace = f1.getNextRace()
afterRaces = f1.getAfterRaces()

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
st.markdown(f1NextEventsCardWidget.getEventCard(nextRace.events), unsafe_allow_html=True)

futureRaces, standings = st.tabs(["Next Races", "Standings"])

# Standings
with standings:
    standingsMd = f"""
        <style>
            h1 {{
                padding: 0;
            }}
            p {{
                margin-bottom: 0!important;
            }}
        </style>
        # <a href="#" style="text-decoration: none; color: white">Standings</a>
    """
    st.markdown(standingsMd, unsafe_allow_html=True)
    f1StandingsWidget.getStandings()

# Next Races
with futureRaces:
    nextRacesMd = f"""
        <style>
            h1 {{
                padding: 0;
            }}
            p {{
                margin-bottom: 0!important;
            }}
        </style>
        # <a href="#" style="text-decoration: none; color: white">Next Races</a>
    """
    st.markdown(nextRacesMd, unsafe_allow_html=True)
    st.markdown(f1NextRacesCardWidget.getF1Card(afterRaces), unsafe_allow_html=True)

