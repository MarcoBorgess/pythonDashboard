import streamlit as st
from controllers import f1
from views import f1RacesList, f1EventsList, f1Standings

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
st.markdown(f1EventsList.getEventCard(nextRace.events), unsafe_allow_html=True)

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
    driverStandings = f1.getDriverStandings()
    constructorStandings = f1.getConstructorStandings()
    f1Standings.getStandings(driverStandings, constructorStandings)

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
    st.markdown(f1RacesList.getF1Card(afterRaces), unsafe_allow_html=True)

