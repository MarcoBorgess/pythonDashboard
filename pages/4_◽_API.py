import controller.globalController as globalController
import streamlit as st
import controller.f1Requests as f1api
import controller.binsController as bins
from time import sleep


globalController.setConfig()

# UpdateButton
updateButton = st.button("Update F1")
placeholder = st.empty()
if updateButton:
<<<<<<< HEAD
    text = f'Calendar: {f1api.updateF1Calendar()}\nDriver Standings: {f1api.updateDriverStanding()}'
    placeholder.text(text)
    sleep(3)
    placeholder.empty()

# Insert Bins
itemId = st.text_input('Item ID')
params = st.text_input('Parameters')
insertButton = st.button("Insert Value")
placeholder = st.empty()
if insertButton:
    text = bins.insertItem({itemId}, {params})
=======
    text = f'Calendar: {api.updateF1Calendar()}\nDriver Standings: {api.updateDriverStanding()}\nConstructor Standings: {api.updateConstructorStanding()}'
>>>>>>> 4e1b072396b4bf48367f036978968ae19642ca32
    placeholder.text(text)
    sleep(3)
    placeholder.empty()