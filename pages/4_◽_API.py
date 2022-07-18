import controller.globalController as globalController
import streamlit as st
import controller.f1Requests as api
from time import sleep


globalController.setConfig()

# UpdateButton
updateButton = st.button("Update F1")
placeholder = st.empty()
if updateButton:
    text = f'Calendar: {api.updateF1Calendar()}\nDriver Standings: {api.updateDriverStanding()}\nConstructor Standings: {api.updateConstructorStanding()}'
    placeholder.text(text)
    sleep(3)
    placeholder.empty()