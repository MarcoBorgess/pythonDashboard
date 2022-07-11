import apiRequests
import streamlit as st

st.set_page_config(
    page_title="Formula 1 Calendar",
    page_icon="car",
    layout="wide", 
)

racesJson = apiRequests.getF1Calendar()
racesList = racesJson.MRData.RaceTable.Races

nextRace = 4;

#Find next race
for race in racesList:
    if (True):
        print(race.round)

for race in racesList:
    if (int(race.round) == nextRace):
        st.text(race.date)
