from controller import globalController, bitsController
from widgets import bitsItemsWidget
import streamlit as st


globalController.setConfig()

bits, items = st.tabs(["Bits", "Items"])

with bits:
    rank = st.selectbox('Fame Rank', 
                ['New Player', 'Settler', 'Citizen', 'Contributor', 'Philanthropist', 'Patron', 'Famous Player', 'Attaché', 'Ambassador', 'Stateperson', 'Senator', 'Dignitary', 'Councilor', 'Minister', 'Premier', 'Chancellor', 'Supreme'],
                5
                )
    bitsItems = bitsItemsWidget.getBitsWidget(bitsController.getBitsItems(), rank)
    st.markdown(bitsItems, unsafe_allow_html=True)