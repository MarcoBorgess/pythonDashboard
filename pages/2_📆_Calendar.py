import apiRequests
import streamlit as st
import json
from collections import namedtuple
from json import JSONEncoder

st.set_page_config(
    page_title="Formula 1 Calendar",
    page_icon="car",
    layout="wide", 
)

racesJson = apiRequests.getF1Calendar()

racesList = racesJson.MRData.RaceTable.Races

for race in racesList:
    st.text(race.round)
    time = race.date + ' ' + race.time
    st.text(time)
