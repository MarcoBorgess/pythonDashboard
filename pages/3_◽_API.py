import globalFunctions
import streamlit as st
import apiRequests as api
from time import sleep


globalFunctions.setConfig()

# UpdateButton
updateButton = st.button("Update F1")
placeholder = st.empty()
if updateButton:
    text = api.updateF1Calendar()
    placeholder.text(text)
    sleep(3)
    placeholder.empty()