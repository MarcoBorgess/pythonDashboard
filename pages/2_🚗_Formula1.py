from time import sleep
import streamlit as st
from apiRequests import updateF1Calendar
import f1Functions as f1
import globalFunctions

globalFunctions.setConfig()

nextRace = f1.getNextRace()

headerMd = f"""
    # <a href="{nextRace.url}" style="text-decoration: none; color: white">{nextRace.name}</a>
    Starting in {nextRace.timeUntil}
"""
# Title and Update Button
header, update = st.columns([9, 1.5])

with header:
    st.markdown(headerMd, unsafe_allow_html=True)

with update:
    st.text('')
    st.text('')
    updateContainer = st.empty()
    updateButton = updateContainer.button("Update Calendar")
    if updateButton:
        text = updateF1Calendar()
        updateContainer.empty()
        newUpdateButton = updateContainer.button(text)
        sleep(3)
        updateContainer.empty()

st.text(f'in {nextRace.timeUntil}')